# 用Ollama管理的本地模型从0跑通llm开发
---
---
## 模型选择
要求：可以识图，本地可跑（2080ti 22G显存）具备代码能力和较强的中文输出能力  
Gemini推荐的最均衡的模型：
* 大模型：qwen3.5:9b
* embedding模型：qwen3-embedding:4b
```bash
# 拉取模型（先运行ollama）
ollama pull qwen3.5:9b
ollama pull qwen3-embedding:4b
ollama list # 查看是否安装成功
```
### 设置推荐的环境变量（最好设置在用户变量中）
1. 开启Flash Attention，降低现存并提速    `OLLAMA_FLASH_ATTENTION=1`
2. 对上下文KV Cache进行8-bit量化（几乎不损失精度，可省下近一半长文本现存）`OLLAMA_KV_CACHE_TYPE=q8_0`
3. 允许同时在现存里驻留两个模型`OLLAMA_MAX_LOASED_MODELS=2`
4. 设置模型空闲5min后自动释放现存`OLLAMA_KEEP_ALIVE=5m`
### 验证显存加载状态
启动对话，另开一个终端运行：`ollama ps` 查看当前加载的模型，显存占用，是否百分之百运行在GPU上





