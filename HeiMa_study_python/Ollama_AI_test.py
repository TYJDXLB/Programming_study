# # 学习使用OpenAI模式调用Ollama管理的本地大模型
# from openai import OpenAI

# # 输入问题
# User_Q= input("请输入问题：")

# client = OpenAI(
#     api_key="OLLAMA_API_KEY",
#     base_url="http://localhost:11434/v1") # 大模型服务本质上是一个"本地网站(HTTP服务器)"，地址 http://localhost:11434 由于地址都挂在v1接口，因此要加上

# response = client.chat.completions.create(
#     model="qwen3.5:9b", # 本地Ollama模型名称
#     messages=[
#         {"role": "system", "content": "你是一个有用的猫娘助手，每句话结尾都需要加上'喵~'"},
#         {"role": "user", "content": f"{User_Q}"},
#     ],
#     stream=False
# )

# print(response.choices[0].message.content)



# 学习使用HTTP原生调用Ollama管理的本地大模型（流失输出）

# urllib子模块：1.request：发送请求，获取网页内容 2.parse：URL编码、拼接、解析链接 3.error：捕获请求异常 4.robotparser：读取robot.txt，判断是否允许使用爬虫
import json
import requests

# 输入问题
User_Q= input("User：")

# ============================================================================
# 【配置区】把容易变动的量集中放在文件顶部附近，方便以后修改（这叫"常量集中管理"）
#   接口地址说明：Ollama 提供两套接口——
#     1) /v1/chat/completions：OpenAI 兼容接口（方便给原本用 OpenAI 的程序平移）
#     2) /api/chat          ：Ollama 原生接口（支持 think 等自家参数）
#   实测在当前版本上，关闭"思考模式"的 think 参数只有走原生接口才生效，
#   所以这里必须使用原生接口 /api/chat。
# ============================================================================
# 变量配置区
OLLAMA_URL = "http://localhost:11434/api/chat"
OLLAMA_MODEL = "qwen3.5:9b"

payload = {
    "model": OLLAMA_MODEL,
    "messages": [
        {
            "role": "system",
            "content": "你是一个有用的猫娘助手，每句话结尾都需要加上'喵~'" # 系统提示词
        },
        {
            "role": "user",
            "content": f"{User_Q}"
        }
    ],
    "stream": True, # 流式输出：模型像挤牙膏一样边想边返回，界面可以逐字显示
    "think": False  # 关闭思考链，开启思考链太慢了
}

try:
    resp = requests.post( # requests.post:发送POST请求给ollama服务
        OLLAMA_URL,
        json=payload, # 自动把python字典转化为json请求体
        stream=True,
        timeout=120   # 最长等待120s 
    )
    resp.raise_for_status() # 检测HTTP状态码，抛出错误直接进入except
    print("AI：", end="")
    for line in resp.iter_lines(): # iter_lines()一行一行读取http返回的字节流
        if line:
            chunk = json.loads(line.decode("utf-8").strip()) # json.loads：把JSON字符串 → Python字典（与dumps相反）; decode("utf-8")字节→字符串，strip()去掉首尾空白/换行
            content = chunk["message"]["content"]
            print(content, end="", flush=True)
    print()
except requests.exceptions.RequestException as e:
        print(f"\n请求异常：{e}")