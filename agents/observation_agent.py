from typing import List
from models.message import Message, AgentRole
from models.task import AgentState, Task
from .base_agent import BaseAgent
from config.prompts import OBSERVATION_AGENT_PROMPT

class ObservationAgent(BaseAgent):
    def __init__(self, model):
        super().__init__(AgentRole.OBSERVATION, model)
    async def process(self, task: Task) -> Message:
        self.state = AgentState.OBSERVING
        context = task.history
        # 从上下文中提取行动结果和子代理信息
        action_message = next((msg for msg in context[-1:] if msg.role == AgentRole.ACTION), None) if context else None
        action_result = action_message.content if action_message else ""
        sub_agent = action_message.sub_agent if action_message else "未知子代理"
        # 根据子代理类型选择不同的提示词内容
        sub_agent_context = self._get_sub_agent_context(sub_agent)

        # 构建提示词
        history_str = "\n".join([f"{msg.role.value}: {msg.content}" for msg in task.history[-5:]]) if task.history else "无"
        prompt = OBSERVATION_AGENT_PROMPT.format(
            description=task.description,
            history=history_str,
            action_result=action_result,
            sub_agent_obsveration = sub_agent_context
        )
        observation = await self._call_llm(prompt)
        return Message(self.role, observation, {"state": self.state,
                                                "requires_human_input": True,
                                                "sub_agent": sub_agent  }# 传递子代理信息
        )


    def _get_sub_agent_context(self, sub_agent: str) -> str:
        """根据子代理类型返回相应的上下文描述"""
        sub_agent_contexts = {
            "query_understand_agent": """
            当前执行的是问题理解代理(query_understand_agent)，主要负责：
            - 解析用户问题，提取相关参数
            - 理解问题的核心要素
            - 对问题进行改写，标准化问题描述格式
            请向用户确认问题理解代理结果是否正确，是否可以按照计划执行其他代理。
            输出示例：
            - 亲爱的小伙伴，请您确认我们对您的问题理解是否正确，是否可以按照计划进行其他代理。
            """,
            "other_agent": """
            
            """
        }
        return sub_agent_contexts.get(sub_agent, "当前执行的代理功能未知，请客观记录执行结果。")