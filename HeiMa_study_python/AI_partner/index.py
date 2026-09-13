# 引入streamlit
import streamlit as st
# 引入智谱大模型
from zai import ZhipuAiClient
# 引入os模块找环境变量ZAI_API_KEY的值
import os


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
st.logo("./AI_partner/media/logo.png", size="large")

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

# 初始化聊天信息(相当于把聊天信息储存在一个储存空间)
if "message" not in st.session_state: # 如果没有就就新建一个储存空间
    st.session_state.message = [] # 把储存空间定义成一个空列表
# 初始化昵称，性格信息
if "ai_information" not in st.session_state:
    st.session_state.ai_information = {"iname": "", "icharacter": ""} # 用字典储存昵称和性格

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
    st.subheader("伴侣信息")
    name = st.text_input("昵称", placeholder="请输入昵称")
    if name: # 把信息储存在session_state.ai_information中
        st.session_state.ai_information["iname"] = name
    
    character = st.text_area("性格", placeholder="请输入性格") # text_area表示文本域
    if character:
        st.session_state.ai_information["icharacter"] = character


# 初始化客户端
client = ZhipuAiClient(api_key = os.getenv("ZAI_API_KEY"))

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
        model="glm-4.5-air",
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
        stream=True,
        temperature=0.6
    )


    # # 输出大模型返回结果（非流式输出）流式输出和非流式输出解析方式不同
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # print("<———— 这是大模型返回结果：", response.choices[0].message.content)
    # # 存入大模型的消息
    # st.session_state.message.append({"role": "assistant", "content": response.choices[0].message.content})

    # 由于大模型回答的时候会有~符号，由于write语句会识别markdown格式，会变成两个~之间删除线，因此需要对其转义一下
    def change(text:str):
        return text.replace("~", r"\~")

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

    # 存入大模型的消息
    st.session_state.message.append({"role": "assistant", "content": full_response})

