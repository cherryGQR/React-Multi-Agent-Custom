from abc import ABC, abstractmethod
from typing import List, Dict, Any
from models.task import Task
from models.message import Message, AgentRole
from tools.llm_utils import async_llm_call

class BaseAgent(ABC):
    def __init__(self, role: AgentRole, model):
        self.role = role
        self.model = model
    @abstractmethod
    async def process(self, task: Task) -> Message:
        """处理输入并生成响应"""
        pass
    async def _call_llm(self, prompt: str, context: List[Dict] = None) -> str:
        """异步调用大语言模型"""
        return await async_llm_call(self.model, prompt, context)