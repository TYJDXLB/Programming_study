# 引入streamlit
import streamlit as st


# 设置页面
st.set_page_config(
    page_title="Streamlit 入门学习", # 网页标签标题
    page_icon="🧊", # 网页标签logo
    #布局
    layout="wide", # 页面效果
    # 侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={ # 页面右上角几个选项的作用 不用可以注释掉
        # 'Get Help': "https://www.bilibili.com/",
        # 'Report a bug': "https://www.acfun.cn/v/list155/index.htm",
        # 'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# 标题
st.title("Streamlit 入门演示") #大标题
st.header("Streamlit 一级标题") #一级标题
st.subheader("Streamlit 二级标题") #二级标题

# 段落文字
st.write("""
这是一个大段文字的第一行
这是一个大段文字的第二行
这是一个大段文字的第三行
""")
st.write("这是一个大段文字第四行")

# 图片
st.image("./resource/北.jpeg", width=500)

# 音频
st.audio("./resource/斯芬克斯之谜-洛天依.mp3")

# 视频
st.video("./resource/斯芬克斯之谜-洛天依.mp4")

# logo
st.logo("./resource/logo.jpg")

# 表格
student_data = {
    "name": ["jack", "brown", "bob"],
    "age": [18, 21, 24],
    "gender": ["boy", "girl", "boy"]
}
st.table(student_data, hide_index=False)

# 输入框
# 普通输入框
name = st.text_input("请输入姓名：") #返回值为输入的内容
st.write(f"输入的姓名为：{name}")
# 密码输入框
password = st.text_input("请输入密码：", type="password")
st.write(f"密码为：{password}")
# 文本域
say = st.text_area("想说的话")
st.write(say)

# 单选按钮
gender = st.radio("请选择性别：", ["boy", "girl", "Uknown"], index=1) #index表示默认索引
st.write(f"您的性别为：{gender}")