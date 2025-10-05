# agents/human_feedback.py

from models.message import Message, AgentRole
from models.task import AgentState
from tools.async_utils import async_input

class HumanInTheLoop:
    """处理人类输入的中介类"""
    def __init__(self):
        self.role = AgentRole.HUMANFEEDBACK
        self.model = None
    async def process(self, observation: str = None, task_description: str = None) -> Message:
        """获取人类反馈"""
        self.state = AgentState.HUMANFEEDBACK
        print("请输入您的反馈 (输入'skip'跳过):")
        feedback = await async_input("您的反馈: ")
        if feedback.lower() == 'skip':
            return Message(self.role, "无反馈", {"state": self.state})
        return Message(self.role, feedback, {"state": self.state})