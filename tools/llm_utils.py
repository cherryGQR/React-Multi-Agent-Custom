import asyncio
from typing import List, Dict, Any
from langchain_openai import ChatOpenAI

async def async_llm_call(model: ChatOpenAI, prompt: str, context: List[Dict] = None) -> str:
    """异步调用LLM"""
    messages = []
    if context:
        messages.extend(context)
    messages.append({"role": "user", "content": prompt})
    try:
        # 使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None, lambda: model.invoke(messages)
        )
        return response.content
    except Exception as e:
        return f"错误: {str(e)}"