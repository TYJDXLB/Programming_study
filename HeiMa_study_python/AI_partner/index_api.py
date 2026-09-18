# 引入streamlit
import streamlit as st
# 引入智谱大模型
from zai import ZhipuAiClient
# # 使用OpenAI兼容写法调用本地大模型，引入OpenAI库
# from openai import OpenAI
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


# 以下实例化客户端，并调用；输出调用结果格式(response.choices[0].message.content) 都是使用的OpenAI兼容写法。因此，调用本地大模型的时候这里仍使用OpenAI兼容写法
# [如果直接使用Ollama官方SDK调用格式就是：response["message"]["content"]]

# 初始化客户端
client = ZhipuAiClient(api_key = os.getenv("ZAI_API_KEY")) # 调用智谱AI
# client = OpenAI(
#     base_url="http://localhost:11434/v1",
#     api_key="1234" # Ollama不需要真实的API_key，随便填
# )

# 消息输入框  不需要写循环语句，因为是streamlit框架的特点，每次输入后，会自动刷新页面，不会终止程序
prompt_user = st.chat_input("请输入您的消息：")
if prompt_user: # 字符串非空即真
    # st.write(f"您输入的消息为：{prompt}") # 这是直接显示输入的文字
    st.chat_message("user").write(prompt_user) # 这是将输入的文字显示在聊天框中
    print("————> 这是用户输入的消息：", prompt_user)
    # 将信息封装成一个字典，存入列表中
    st.session_state.message.append({"role": "user", "content": prompt_user}) # 存入用户的消息
    # 调用大模型
    response = client.chat.completions.create(
        model="glm-4.5-air", # 智谱AI的模型
        # model="qwen3.5:0.8b", # 本地模型
        messages=[
            {
                "role": "system",
                "content": prompt_system % (st.session_state.ai_information["iname"], st.session_state.ai_information["icharacter"])
            },
            # 把会话历史遍历输出到大模型中
            *st.session_state.message, #解包列表，将列表中的元素作为独立的参数传递给函数
            # { 因为在前面已经把用户的消息存入了列表中，所以这里不需要再存入
            #     "role": "user",
            #     "content": prompt_user
            # }
        ],
        stream=True, # 是否流式输出
        # temperature=0.6 # 采样温度，用来控制输出的随机性/创造性。数值越高回答的越发散
    )



    # # 输出大模型返回结果（非流式输出）流式输出和非流式输出解析方式不同
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # print("<———— 这是大模型返回结果：", response.choices[0].message.content)
    # # 存入大模型的消息
    # st.session_state.message.append({"role": "assistant", "content": response.choices[0].message.content})


    # 输出大模型返回结果（流式输出） 遍历response数据包，非流式输出只有一个数据包就不用遍历了
    # # __旧版流式输出方式__
    # response_message = st.empty() #empty是一个空容器，用来展示大模型返回结果(先占个位)
    # # 定义一个空字符串，用来存储所有数据包的内容
    # full_response= ""
    # for chunk in response: # [切记前面一定要把stream=改为true否则chunk会被封装成元组而非列表导致报错]
    #     if chunk.choices[0].delta.content is not None: # 因为流式输出最后一个数据包为[DONE]因此要判断一下
    #         content = chunk.choices[0].delta.content # 拿到该数据包的内容
    #         full_response += content # 把该数据包的内容加到full_response中
    #         response_message.chat_message("assistant").write(full_response) # 把内容添加到空容器中，每一次都比上次多一些内容，看起来像是逐渐增加的，其实是不断替换新的内容

    # __新版流式输出方式__
    # 采用生成器函数方式
    def stream_generator():
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                yield change(chunk.choices[0].delta.content) # yield：暂停函数，先吐出一小块数据出去；下次调用时，从暂停位置继续往下跑
    # 用with语句 st.chat_message("assistant")用来渲染出聊天气泡，with表示后续输出内容都在这个气泡中
    with st.chat_message("assistant"): # 不能用with语句直接代替前面的空容器，因为上边的for循环在外边，会产生很多聊天气泡
        full_response = st.write_stream(stream_generator())
    print("<———— 这是大模型返回结果：", full_response)

    # 存入大模型的消息
    st.session_state.message.append({"role": "assistant", "content": full_response})

