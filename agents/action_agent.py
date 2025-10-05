# agents/base_agent.py

import re
from typing import List, Dict, Callable
from models.message import Message, AgentRole
from models.task import AgentState, Task
from .base_agent import BaseAgent

class ActionAgent(BaseAgent):
    def __init__(self, agents: Dict[str, Callable], model):
        super().__init__(AgentRole.ACTION, model)
        self.agents = agents
    async def process(self, task: Task) -> Message:
        self.state = AgentState.ACTING
        context = task.history
        # 从上下文中提取计划
        plan = next((msg.content for msg in context[-1:] if msg.role == AgentRole.PLAN), "") if context else ""
        # 使用正则表达式提取下一个代理
        pattern = r'<next_agent>(.*?)</next_agent>'
        match = re.search(pattern, plan)

        agent_decision = "未知代理"
        if match:
            agent_decision = match.group(1).strip()
            print(f"执行 {agent_decision}")
        else:
            print("未找到下一步代理")

        # 选择并执行代理
        selected_agent = None
        for agent_name in self.agents.keys():
            if agent_name in agent_decision:
                selected_agent = agent_name
                break
        # 执行工具
        result = "没有执行任何行动"
        if selected_agent:
            try:
                result = await self.agents[selected_agent](task)
            except Exception as e:
                result = f"执行工具 {selected_agent} 时出错: {str(e)}"
        return Message(self.role, f"行动: {agent_decision}\n结果: {result}", {"state": self.state}, sub_agent=selected_agent)

