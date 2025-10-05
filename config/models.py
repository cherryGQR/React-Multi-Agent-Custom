from langchain_openai import ChatOpenAI

LLM_CONFIGS = {
    "DeepSeek-V3-fp8": {
        "max_retries": 2,
        "model": "DeepSeek-V3-fp8",
        "api_key": " ",
        "temperature": 0.7,
        "base_url": ""
    },
    "DeepSeek-R1-fp8": {
        "model": "DeepSeek-R1-fp8",
        "api_key": "",
        "base_url": ""
    },
    "other model": {
        "model": "",
        "api_key": "",
        "base_url": ""
    },

}

def get_llm(model_name: str) -> ChatOpenAI:
    """根据配置名称获取LLM实例"""
    if model_name not in LLM_CONFIGS:
        raise ValueError(f"未知的模型配置: {model_name}")
    config = LLM_CONFIGS[model_name]
    return ChatOpenAI(**config)