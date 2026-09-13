# from math import fabs

import os
from zai import ZhipuAiClient

# 初始化客户端
# client = ZhipuAiClient(api_key="密钥") 直接这样写api暴露，可以把api放到一个系统变量中再引入os模块读取变量
client = ZhipuAiClient(api_key = os.getenv("ZAI_API_KEY"))  # os.getenv("ZAI_API_KEY")读取该变量的值；os.environ.get("ZAI_API_KEY")与其等价

# 创建聊天完成请求
response = client.chat.completions.create(
    model="glm-4.5-air",
    messages=[
        {
            "role": "system",
            "content": "你是一个有用的猫娘AI助手，回答任何问题时结尾都会带一个'喵~'，请用温柔可爱的语气回答用户的问题"
        },
        {
            "role": "user",
            "content": "请介绍一下自己吧。"
        }
    ],
    stream=False,
    temperature=0.6
)

# 获取回复 获取回复中的"choices"里面的第1个元素，再获取里面的message下的content里的内容
print(response.choices[0].message.content) #报错不影响使用



# # 测试是否安装成功
# import zai
# print(zai.__version__)