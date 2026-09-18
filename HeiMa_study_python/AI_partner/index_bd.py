# 引入streamlit
import streamlit as st
# # 引入智谱大模型
# from zai import ZhipuAiClient
# ============================================================================
# 调用本地 Ollama 大模型：为什么用 urllib？
#   大模型服务本质上是一个"本地网站(HTTP服务器)"，地址 http://localhost:11434
#   我们的程序要像浏览器访问网站一样，给它"发请求"并"收响应"，这就是API调用。
#   urllib 是 Python 自带的标准库（装完Python就有，不用 pip install），
#   专门用来发起 HTTP 请求。这里导入两个子模块：
#     - urllib.request：负责"发请求、收响应"（相当于浏览器）
#     - urllib.error  ：负责接住网络相关的错误（比如服务器没开机）
#   之前用的 openai 第三方库需要额外安装，而且它的兼容接口无法关闭思考模式，
#   所以改为用标准库直接调用 Ollama 的原生接口。
# ============================================================================
import urllib.request
import urllib.error
# 引入os模块找环境变量ZAI_API_KEY的值
import os
# 获取当前系统时间
from datetime import datetime
# 引入json库
import json



# 验证重新加载页面
print("&&&页面已加载&&&")

# 设置页面配置
st.set_page_config(
    page_title="AI 智能伴侣", # 网页标签标题
    page_icon="🤖", # 网页标签logo
    #布局
    layout="wide", # 页面效果为整个区域
    # 侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("AI 智能伴侣")
# logo
st.logo("./media/logo.png", size="large") # 切记一定要在AI_parnter文件目录下运行streamli，cd进该文件夹


# 函数
# 保存会话信息
def save_session_data():
    # 构建一个会话信息对象
    session_data = {
        "current_session": st.session_state.current_session,
        "name": st.session_state.ai_information["iname"],
        "character":  st.session_state.ai_information["icharacter"],
        "message": st.session_state.message
    }
    # 如果文件夹不存在就创建一个文件夹储存它
    if not os.path.exists("session"):
        os.mkdir("session")
    # 保存数据
    with open(f"./session/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=4) # 序列化，把对象变为json文件

# 加载会话信息
def load_session_data(session:str):
    try:
        # 判断下json文件是否存在（可能你把json文件删掉了，但是没有刷新页面，点击之后会报错）
        if os.path.exists(f"./session/{session}.json"):
            # 保存当前信息
            if st.session_state.message: # 如果当前已有对话信息
                save_session_data()
            with open(f"./session/{session}.json", "r", encoding="utf-8") as f: # 通过传入的文件名找到对应json文件
                session_data = json.load(f) # 反序列化，把json文件变为对象
                # 将对象的信息覆盖现有的储存空间
                st.session_state.current_session = session_data["current_session"]
                st.session_state.ai_information["iname"] = session_data["name"]
                st.session_state.ai_information["icharacter"] = session_data["character"]
                st.session_state.message = session_data["message"]
                # st.rerun() # st.rerun()的底层实现就是"抛异常"，写到try用会报错被except捕捉，这里写到外边
    except:
        st.error("加载失败！", icon="⚠")

# 由于大模型回答的时候会有~符号，由于write语句会识别markdown格式，会变成两个~之间删除线，因此需要对其转义一下
def change(text:str):
    return text.replace("~", r"\~")

# 管理所有的会话列表（历史会话）
def load_session():
    session_list = [] # 用于储存session文件夹下的会话文件
    if os.path.exists("session"): # 当存在session文件夹时再进行判断
        file_list = os.listdir("session") # os.listdir("目录") 罗列出指定目录下的文件
        # for file_name in file_list: # 通过循环遍历出以.json结尾的文件
        #     if file_name.endswith(".json"): # .endswith方法：以什么结尾
        #         session_list.append(file_name.rstrip(".json")) # 使用去除右边字符操作去掉.json结尾
        # 用列表推导式
        session_list = [file_name.rstrip(".json") for file_name in file_list if file_name.endswith(".json")]
    session_list.sort(reverse=True) # 为了使最新的在上面，因此对列表进行一次反向排序 由于调用sort方法没有返回值，因此要先处理一下，再return
    return session_list # 无论有无文件都返回一个列表，如果文件不存在就返回空列表

# 删除会话
def delete_session(session):
    try:
        if os.path.exists(f"./session/{session}.json"):
            os.remove(f"./session/{session}.json") # 删除指令
    except:
        st.error("删除失败！", icon="⚠")


# 系统提示词 
prompt_system = f"""
    你叫%s，现在是用户的真实伴侣兼助手，请完全代入角色。
    规则：
        1. 每次只回复一条信息
        2. 禁止任何场景或状态描述性文字
        3. 回复简短，像微信聊天一样
        4. 有需要可以使用🤣💖😍等emoji表情
        5. 用符合伴侣性格的方式进行对话
        6. 回复的内容要充分体现伴侣的性格特征
        7. 匹配用户的语言
    伴侣性格：
        * %s
    你必须严格遵守上述规则来回复用户
"""


# 在session_state开辟储存空间
# 初始化聊天信息(相当于把聊天信息储存在一个储存空间)
if "message" not in st.session_state: # 如果没有就就新建一个储存空间
    st.session_state.message = [] # 把储存空间定义成一个空列表
# 初始化昵称，性格信息
if "ai_information" not in st.session_state:
    st.session_state.ai_information = {"iname": "", "icharacter": ""} # 用字典储存昵称和性格
# 初始化并记录会话标识(会话时间)
if "current_session" not in st.session_state:
    st.session_state.current_session = datetime.now().strftime("%Y-%m-%d_%H：%M：%S") # 拿到当前系统时间并格式化

# 展示当前会话名称
st.text(f"会话名称：{st.session_state.current_session}")
# 把存入的信息遍历展示出来(展示历史信息)
for message in st.session_state.message: # {"role": "user", "content": prompt}
    # if dic["role"] == "user": # 如果是用户的消息
    #     st.chat_message("user").write(dic["content"])
    # else: # 如果是大模型的消息
    #     st.chat_message("assistant").write(dic["content"])
    st.chat_message(message["role"]).write(message["content"]) # 直接输出，不用再判断是用户还是大模型的消息

# # 侧边栏 st.sidebar.侧边栏里面的组件 (所有在侧边栏中的组件都要加上st.sidebar.的前缀，这样代码过于松散)
# st.sidebar.subheader("伴侣信息")
# 用with语句 with是上下文管理器，定义在with中的语句都在with开辟的空间中
with st.sidebar:
    # 会话信息
    st.subheader("AI控制面板")
    # 新建会话 | width参数：content由内容撑开，stretch铺满整个容器 | 有会话内容的时候才保存(and之后的语句含义)
    if st.button("保存并新建会话", icon="✏️", width="stretch") and st.session_state.message:
        # 1. 保存当前会话数据
        save_session_data()
        # 2. 创建新的会话（清空当前会话记录）
        st.session_state.message = []
        st.session_state.current_session = datetime.now().strftime("%Y-%m-%d_%H：%M：%S") # 更新一下时间。否则新旧会话会相互覆盖
        print(datetime.now().strftime("%Y-%m-%d_%H：%M：%S")) # 终端输出一下保存时间
        st.rerun() # 重新加载一下页面，用上述新建的空的会话列表去覆盖原本已经有内容的列表

    # 展示历史会话信息
    st.text("历史会话")
    session_list = load_session() # 调用保存会话函数得到历史列表
    for session in session_list:
        col1, col2 = st.columns([4, 1]) # 把一行按照4：1分为两列
        # streamlit会给按钮生成唯一的内部ID，如果key一样（即下面的del按钮，如果没有key，有没有内容，无法区分导致内部ID重复），导致报错
        with col1: # 加载会话
            # 三元运算符：如果条件为真则返回第一个表达式，否则返回第二个；值1 if 条件 else 值2
            if st.button(session, icon="📄", width="stretch", key=f"load_{session}", type="primary" if session == st.session_state.current_session else "secondary"): # 如果点击了
                load_session_data(session)
                st.rerun() # 重新加载一下页面
        with col2: # 删除会话
            if st.button("", icon="❌", width="stretch", key=f"delete_{session}"):
                delete_session(session)
                # 如果删除的是当前会话，删除完之后应该变为新对话；如果删除的不是当前会话，当前会话信息不变
                if session == st.session_state.current_session:
                    # 创建新的会话（清空当前会话记录）
                    st.session_state.message = [] # 清除当前聊天记录
                    st.session_state.ai_information["iname"] = "" # 清除当前名称
                    st.session_state.ai_information["icharacter"] = "" # 清除当前性格
                    st.session_state.current_session = datetime.now().strftime("%Y-%m-%d_%H：%M：%S") # 更新一下时间。否则新旧会话会相互覆盖
                    print(datetime.now().strftime("%Y-%m-%d_%H：%M：%S")) # 终端输出一下保存时间
                st.rerun() # 重新加载一下页面

    # 分割线
    st.divider()

    # 伴侣信息
    st.subheader("伴侣信息")
    name = st.text_input("昵称", placeholder="请输入昵称", value=st.session_state.ai_information["iname"]) # value属性为，文本框上默认显示的值
    if name: # 把信息储存在session_state.ai_information中
        st.session_state.ai_information["iname"] = name
    
    character = st.text_area("性格", placeholder="请输入性格", value=st.session_state.ai_information["icharacter"]) # text_area表示文本域
    if character:
        st.session_state.ai_information["icharacter"] = character


# ============================================================================
# 【配置区】把容易变动的量集中放在文件顶部附近，方便以后修改（这叫"常量集中管理"）
#   接口地址说明：Ollama 提供两套接口——
#     1) /v1/chat/completions：OpenAI 兼容接口（方便给原本用 OpenAI 的程序平移）
#     2) /api/chat          ：Ollama 原生接口（支持 think 等自家参数）
#   实测在当前版本上，关闭"思考模式"的 think 参数只有走原生接口才生效，
#   qwen3.5 默认会先生成 2000+ token 的英文思考链，纯CPU推理要等一分半钟，
#   所以这里必须使用原生接口 /api/chat。
# ============================================================================
OLLAMA_URL = "http://localhost:11434/api/chat"
OLLAMA_MODEL = "qwen3.5:0.8b" # 本地模型名称，用 ollama list 可以查看已安装的模型
MAX_HISTORY = 20 # 每次请求最多携带的最近消息条数（防止历史过长撑爆上下文窗口）

# 消息输入框  不需要写循环语句，因为是streamlit框架的特点，每次输入后，会自动刷新页面，不会终止程序
prompt_user = st.chat_input("请输入您的消息：")
if prompt_user: # 字符串非空即真（空字符串""在if里会被当作False）
    st.chat_message("user").write(prompt_user) # 将用户输入的文字显示在聊天框中
    print("————> 这是用户输入的消息：", prompt_user)
    # 将信息封装成一个字典，存入列表中
    # 大模型对话用的统一消息格式：{"role": 角色, "content": 内容}
    #   role 三种取值：system(设定AI身份) / user(用户说的) / assistant(AI说的)
    st.session_state.message.append({"role": "user", "content": prompt_user}) # 先把用户消息存入历史

    # ------------------------------------------------------------------------
    # 【知识点：列表切片 list[-n:]】
    #   message[-20:] 表示"从倒数第20个元素一直取到末尾"，即最近的20条消息。
    # 为什么要裁剪？
    #   大模型每次回答都要重读全部历史，而它一次能读的长度有上限（上下文窗口）。
    #   历史太长时，Ollama 会丢弃最旧的内容——排在最前面的"角色设定(system)"
    #   最先被丢掉，AI 就会忘记自己是谁、性格是什么，表现为"聊着聊着变笨了"。
    # ------------------------------------------------------------------------
    recent_messages = st.session_state.message[-MAX_HISTORY:]

    # ------------------------------------------------------------------------
    # 【知识点：请求体 payload】
    #   调用API就是把一个字典按约定格式发给服务器。Ollama /api/chat 约定的字段：
    #     model   ：用哪个模型
    #     messages：完整对话（第1条必须是 system 身份设定，后面是历史记录）
    #     stream  ：True=流式(逐字返回) / False=非流式(等全部生成完一次性返回)
    #     think   ：False=关闭思考链（qwen3.x 混合思考模型特有，关键提速参数）
    #     options ：采样/运行参数
    # ------------------------------------------------------------------------
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {
                "role": "system",
                # prompt_system 里有两个 %s 占位符，% 后面的元组按顺序填入：昵称、性格
                "content": prompt_system % (st.session_state.ai_information["iname"], st.session_state.ai_information["icharacter"])
            },
            # 【知识点：*解包】*recent_messages 会把列表里的每个字典"摊开"，
            # 变成这个 messages 列表里一个个独立的元素，而不是嵌一个子列表进去。
            *recent_messages,
        ],
        "stream": True, # 流式输出：模型像挤牙膏一样边想边返回，界面可以逐字显示
        "think": False, # 关闭思考链。实测：开着→90秒/回复；关闭→几秒/回复
        "options": {
            # num_ctx = 上下文窗口大小（单位token，可以粗略理解为模型一次能"看见"的字数）
            # Ollama 默认 4096，这里扩到 8192，能记住更长的对话；0.8B小模型占用内存增加很小
            "num_ctx": 8192,
            # temperature(温度)这里故意不传，让模型用出厂调优值 1.0。
            # 温度越低回答越确定/保守，但小模型在低温下容易反复输出同一句话（重复退化）。
        },
    }

    # ------------------------------------------------------------------------
    # 【知识点：HTTP 请求四要素】 urllib.request.Request 用来组装一个请求对象：
    #   ① 网址 URL        ② 请求体 data   ③ 请求头 headers
    #   json.dumps()：把 Python 字典 → JSON 格式的字符串（网络只能传文本/字节）
    #   .encode("utf-8")：再把字符串 → 字节(bytes)，HTTP 传输的底层单位是字节
    #   请求头 Content-Type: application/json 是告诉服务器"我发的是JSON格式"
    # ------------------------------------------------------------------------
    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    raw_parts = [] # 专门收集"未经转义"的原始回复片段，最后拼接起来存入历史
    # ------------------------------------------------------------------------
    # 【知识点：try / except / else 异常处理结构】
    #   try   ：放可能出错的代码（网络请求最容易失败：服务没开、超时、返回坏数据）
    #   except：出错时执行，避免整个程序崩溃白屏，并给用户友好提示
    #   else  ：try 里"一点错都没出"时才执行（这里用来安全地保存回复到历史）
    # ------------------------------------------------------------------------
    try:
        # 【知识点：with 上下文管理器】
        #   urlopen 真正把请求发出去并拿到响应；with 保证用完后连接自动关闭，
        #   即使中途报错也不会泄漏资源（操作文件 open() 时也是同样的用法）。
        #   timeout=300 指"两个数据包之间最多等300秒"，不是总时长；
        #   流式输出会持续有数据包到来，所以不会因为整体耗时长而被误杀。
        with urllib.request.urlopen(request, timeout=300) as response:
            # ----------------------------------------------------------------
            # 【知识点：生成器函数 + yield（流式输出的核心）】
            #   普通函数用 return 返回一次就结束；生成器用 yield 可以"吐"出多次：
            #   每吐出一小块文本就暂停，等界面显示完，下次从暂停处继续——
            #   于是用户看到文字一个一个蹦出来，而不是干等几十秒。
            #   st.write_stream 会不断向这个生成器要数据，直到它结束。
            # ----------------------------------------------------------------
            def stream_generator():
                # Ollama 流式响应的格式叫 NDJSON：每一行就是一个独立的 JSON 数据包
                for raw_line in response: # 直接 for 一个响应对象，会逐行读到数据
                    line = raw_line.decode("utf-8").strip() # 字节→字符串，strip()去掉首尾空白/换行
                    if not line: # 偶尔会出现空行，跳过即可
                        continue
                    chunk = json.loads(line) # json.loads：把JSON字符串 → Python字典（与dumps相反）
                    # 数据包结构示例：{"message":{"role":"assistant","content":"你好"}, "done":false}
                    # 【知识点：dict.get 的安全取值】
                    #   直接写 chunk["message"]["content"]，万一某层键不存在会报 KeyError 崩溃；
                    #   .get("message", {}) 取不到时返回空字典，再链式 .get 就不会报错，
                    #   content 取不到时返回 None（等价于"这个包里没有正文"）。
                    content = chunk.get("message", {}).get("content")
                    if content: # 非空字符串才处理（思考链已关闭，但保险起见仍做判空）
                        raw_parts.append(content) # ① 原文存起来，留给历史记录用（保留真实的~）
                        yield change(content)      # ② 转义后再吐给界面显示（防止~被markdown当成删除线）
                    if chunk.get("done"): # 最后一个数据包会带 "done": true，表示生成完毕
                        break
            # st.chat_message("assistant")渲染出AI的聊天气泡；
            # with 表示内部输出的所有内容都落在这个气泡里
            with st.chat_message("assistant"):
                with st.spinner("对方正在输入…"): # 等待期间显示转圈提示，消除"界面卡死"的感觉
                    st.write_stream(stream_generator()) # 驱动生成器，把文本逐字写进气泡
    except urllib.error.URLError as e: # 专门处理网络连接类错误（最常见：Ollama没启动→端口拒绝连接）
        st.error("无法连接本地 Ollama 服务，请确认 Ollama 已启动后重试。", icon="⚠")
        print("Ollama连接失败：", e) # 同时在终端打印详细错误，方便自己排查
    except Exception as e: # 兜底：接住上面没覆盖到的其他所有异常，保证页面不崩
        st.error("大模型响应失败，请重试。", icon="⚠")
        print("Ollama响应异常：", e)
    else:
        # try 完整成功后才走到这里
        # "".join(列表)：把列表里的多个小字符串无缝拼成一个完整字符串，分隔符是空串
        full_response = "".join(raw_parts) # 注意：拼的是"原文"，不含显示用的 \~ 转义
        print("<———— 这是大模型返回结果：", full_response)
        # .strip()去掉首尾空白后再判空：防止把空回复/纯空格存进历史。
        # 若存了一条"AI没说话"的记录，下一轮模型会模仿这个模式，对话质量会恶化。
        if full_response.strip():
            st.session_state.message.append({"role": "assistant", "content": full_response})
        else:
            st.warning("模型没有返回有效内容，请重试。", icon="⚠")

# ## 二、HTTP / API 调用
# 1. API 的本质 ：大模型服务就是一个本地 HTTP 服务器（`localhost:11434` ），程序按约定格式发请求、收响应。
# 2. 请求三要素 ：网址 URL、请求体 data、请求头 headers（L273–277）。
# 3. GET vs POST ：这里用 POST（携带数据提交）。
# 4. 状态码/连接失败 ：服务没启动时操作系统直接拒绝连接，表现为`URLError` 。
# 5. 流式响应（SSE / NDJSON） ：响应不是一个完整大包，而是一行一个 JSON 持续到达；可以直接`for line in 响应对象` 逐行读。
# ## 三、JSON 数据处理
# - `json.dumps()` ：Python 字典 → JSON 字符串（发出去之前，L275）
# - `json.loads()` ：JSON 字符串 → Python 字典（收到之后，L306）
# - 记忆窍门： loads = load string（字符串变对象），dumps = dump to string（对象变字符串）
# ## 四、大模型核心概念（最重要的部分）
# 1. 三种消息角色 ：`system` （定人设）、`user` （用户）、`assistant` （AI），多轮对话就是把它们按顺序组成列表。
# 2. token ：模型处理文本的最小单位，可粗略理解为"字/词片段"；对话长度按 token 计。
# 3. 上下文窗口（num_ctx） ：模型一次能看到的最大内容量。超限会丢最旧内容，system 人设最先丢——这是"聊着聊着变笨"的根因。
# 4. 无状态特性 ：模型本身不记历史，所以每轮都要把历史记录重新整包发给它。
# 5. 思考模式（think） ：qwen3.x 这类混合推理模型会先生成一长串内部推理再回答；CPU 上极慢且界面不展示，用`think: False` 关闭（必须走原生接口）。
# 6. temperature（温度） ：控制随机性。低=保守确定（小模型易重复），高=发散有创意。
# 7. 流式 vs 非流式 ：流式边生成边返回体验好；非流式要干等全部完成。
# 8. 接口差异 ：Ollama 的 OpenAI 兼容接口与原生接口字段、返回结构不同——原生流式取`chunk["message"]["content"]` ，OpenAI 格式取`choices[0].delta.content` 。
# ## 五、Streamlit 框架相关
# - `st.chat_message(角色)` ：渲染聊天气泡；`st.write_stream()` ：驱动生成器逐字输出；`st.spinner()` ：等待转圈；`st.error/warning` ：界面级错误提示。
# - 脚本从上到下跑一遍就是一次页面刷新，没有传统的`while` 循环。