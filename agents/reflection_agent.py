from typing import List
from models.message import Message, AgentRole
from models.task import AgentState, Task
from .base_agent import BaseAgent
from config.prompts import REFLECTION_AGENT_PROMPT

class ReflectionAgent(BaseAgent):
    def __init__(self, model):
        super().__init__(AgentRole.REFLECTION, model)
    async def process(self, task: Task, human_feedback: str = None) -> Message:
        self.state = AgentState.REFLECTING
        context = task.history
        # 从上下文中提取信息
        plan = next((msg.content for msg in context if msg.role == AgentRole.PLAN), "") if context else ""
        action_message = next((msg for msg in context if msg.role == AgentRole.ACTION), None) if context else None
        action = action_message.content if action_message else ""
        sub_agent = action_message.sub_agent if action_message else "未知子代理"
        observation = next((msg.content for msg in context if msg.role == AgentRole.OBSERVATION), "") if context else ""
        human_feedback = human_feedback or "无人类反馈"
        # 根据子代理类型获取评估标准
        sub_agent_evaluation_criteria = self._get_sub_agent_evaluation_criteria(sub_agent)
        # 构建提示词
        prompt = REFLECTION_AGENT_PROMPT.format(
            description=task.description,
            plan=plan,
            action=action,
            observation=observation,
            human_feedback=human_feedback,
            sub_agent=sub_agent,
            sub_agent_evaluation_criteria=sub_agent_evaluation_criteria
        )
        reflection = await self._call_llm(prompt)
        return Message(self.role, reflection, {"state": self.state})
    def _get_sub_agent_evaluation_criteria(self, sub_agent: str) -> str:
        """根据子代理类型返回相应的评估标准"""
        evaluation_criteria = {
            "query_understand_agent": """
            **query_understand_agent 评估标准**:
            - 理解用户对query_understand_agent执行结果的反馈是什么
            - 如果用户反馈query_understand_agent执行结果正确，则向plan agent推荐继续执行下一步(对应其他代理)
            - 如果用户反馈query_understand_agent执行结果不正确，并且给出了正确答案，则总结上下文，输出纠正后的正确答案给plan agent
            - 如果用户反馈query_understand_agent执行结果不正确，但没有给出正确答案，则总结上下文，输出给plan agent做下一步规划
            """,
            "other_agent": """

            """
        }
        return evaluation_criteria.get(sub_agent, "请基于通用标准评估代理执行效果。")