
import asyncio
from typing import Dict
from config.models import get_llm
from models.task import Task, AgentState
from models.message import Message
from agents.plan_agent import PlanAgent
from agents.action_agent import ActionAgent
from agents.observation_agent import ObservationAgent
from agents.reflection_agent import ReflectionAgent
from agents.human_feedback import HumanInTheLoop
from tools import (
    get_query_analyse,
    get_fail_complete_analyse,
    get_fail_complete_resolve
)

class MultiAgentSystem:
    def __init__(self):
        # 初始化LLM
        llm = get_llm("DeepSeek-V3-fp8")
        # 初始化智能体
        self.plan_agent = PlanAgent(llm)
        self.action_agent = ActionAgent(
            agents={
                "query_understand_agent": get_query_analyse(),
            },
            model=llm
        )
        self.observation_agent = ObservationAgent(llm)
        self.reflection_agent = ReflectionAgent(llm)
        self.human_loop = HumanInTheLoop()
        self.tasks: Dict[str, Task] = {}
    def create_task(self, description: str) -> str:
        """创建新任务并返回任务ID"""
        task_id = f"task_{len(self.tasks) + 1}"
        self.tasks[task_id] = Task(
            id=task_id,
            description=description,
            status=AgentState.IDLE,
            history=[]
        )
        return task_id
    async def execute_task(self, task_id: str, max_iterations: int = 100) -> Task:
        """执行任务"""
        if task_id not in self.tasks:
            raise ValueError(f"任务 {task_id} 不存在")
        task = self.tasks[task_id]
        task.status = AgentState.PLANNING
        iterations = 0
        while task.status != AgentState.COMPLETED and iterations < max_iterations:
            iterations += 1
            print(f"\n--- 迭代 {iterations} ---")
            # 计划阶段
            if task.status == AgentState.PLANNING:
                plan_message = await self.plan_agent.process(task)
                print(plan_message.content)
                task.history.append(plan_message)
                task.status = AgentState.ACTING
            # 行动阶段
            if task.status == AgentState.ACTING:
                action_message = await self.action_agent.process(task)
                print(action_message.content)
                task.history.append(action_message)
                task.status = AgentState.OBSERVING
            # 观察阶段
            if task.status == AgentState.OBSERVING:
                observation_message = await self.observation_agent.process(task)
                print(observation_message.content)
                task.history.append(observation_message)
                task.status = AgentState.HUMANFEEDBACK

            # 人类介入环节
            if task.status == AgentState.HUMANFEEDBACK:
                human_feedback_message = await self.human_loop.process(
                    observation_message.content, #增加接口备用
                    task.description #增加接口备用
                )
                print(human_feedback_message.content)
                task.history.append(human_feedback_message)
                task.status = AgentState.REFLECTING

            # 反思阶段
            if task.status == AgentState.REFLECTING:
                reflection_message = await self.reflection_agent.process(
                    task, human_feedback_message.content
                )
                print(reflection_message.content)
                task.history.append(reflection_message)
                task.status = AgentState.PLANNING

            if iterations >= max_iterations:
                task.status = AgentState.ERROR
                task.result = "达到最大迭代次数但未完成任务，建议重新组织任务进行查询"
        return task

#示例使用
async def main():
    # 创建多Agent系统
    system = MultiAgentSystem()
    query = await async_input("您的问题: ")
    # 创建任务
    task_id = system.create_task(query)
    # 执行任务
    result = await system.execute_task(task_id)
    print(f"\n最终结果: {result.result if result.result else '任务完成'}")
    print(f"最终状态: {result.status}")

if name == "__main__":
    asyncio.run(main())