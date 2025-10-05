import re
from models.message import Message, AgentRole
from models.task import AgentState, Task
from .base_agent import BaseAgent
from config.prompts import PLAN_AGENT_PROMPT

class PlanAgent(BaseAgent):
    def __init__(self, model):
        super().__init__(AgentRole.PLAN, model)
    async def process(self, task: Task) -> Message:
        self.state = AgentState.PLANNING
        # 构建提示词
        history_str = "\n".join([f"{msg.role.value}: {msg.content}" for msg in task.history[-5:]]) if task.history else "无"
        prompt = PLAN_AGENT_PROMPT.format(
            history=history_str,
            description=task.description
        )
        plan = await self._call_llm(prompt)
        # 解析计划状态
        pattern = r'<plan_status>(.*?)</plan_status>'
        match = re.search(pattern, plan)
        if match:
            agent_decision = match.group(1)
            print(f"计划状态: {agent_decision}")
            # 判断任务是否完成
            if "completed" in agent_decision:
                task.status = AgentState.COMPLETED
            else:
                task.status = AgentState.PLANNING
        else:
            print("未找到计划状态")
            task.status = AgentState.PLANNING

        return Message(self.role, plan, {"state": self.state})