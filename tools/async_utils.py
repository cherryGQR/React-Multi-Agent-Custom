import asyncio
import aioconsole

async def async_input(prompt: str) -> str:
    """异步获取用户输入"""
    return await aioconsole.ainput(prompt)
tools/base_sub_agent.py
import re
from typing import Dict, List
from config.models import get_llm
from .llm_utils import async_llm_call
from models.message import Message, AgentRole

class SubAgentBase:
    """子代理基类"""
    def __init__(self, role: AgentRole, model_name: str = "DeepSeek-V3-fp8"):
        self.model = get_llm(model_name)
        self.model_name = model_name
        self.role = role
    async def _call_agent(self, prompt: str) -> str:
        """调用LLM并返回结果"""
        response = await async_llm_call(self.model, prompt)
        return response

    def _extract_xml_content(self, text: str, tag: str) -> str:
        """从文本中提取XML标签内容"""
        pattern = rf'<{tag}>(.*?)</{tag}>'
        match = re.search(pattern, text, re.DOTALL)
        return match.group(1).strip() if match else ""