import asyncio, aiohttp, re, json, requests, logging
from tools.async_utils import async_input
from config.query_understand_sub_agent_prompt import QUERY_UNDERSTAND_PROMPT, QUERY_EXTRECT_PROMPT
from .llm_utils import async_llm_call
from .base_sub_agent import SubAgentBase
from models.message import Message, AgentRole
from typing import Dict, Any, List, Optional
from models.task import AgentState, Task

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QueryUnderstandAgent(SubAgentBase):
    """优化后的问题理解改写agent"""

    def __init__(self, model_name: str = "DeepSeek-V3-fp8"):
        super().__init__(model_name)
        self.parser = ModelOutputParser()
        self.db_searcher = AsyncDatabaseSearcher()

    async def process(self, query: str, context: List[Message] = None) -> str:
        """处理问题理解任务"""
        try:
            # 构建更智能的提示
            context_summary = ""
            if context:
                plan_messages = [msg for msg in context if msg.role.value == "plan_agent"]
                if plan_messages:
                    context_summary = f"\n当前计划: {plan_messages[-1].content}..."

            # # 1. 提取参数，进行类型分类
            # extract_response = await self._extract_parameters(query)
            # # 2. 解析参数
            # extract_result = self.parser.parse(extract_response)
            # logger.info(f"解析出的参数: {extract_result}")
            # # 3. 并行参数含义查询
            # db_search_result = await self._search_parameters(extract_result)
            # 4. 问题理解改写
            final_response = await self._understand_and_rewrite(query, db_search_result)
            return final_response
        except Exception as e:
            logger.error(f"处理查询时出错: {e}")
            return f"处理查询时出错: {str(e)}"

    async def _extract_parameters(self, query: str) -> str:
        """提取参数"""
        # 提取参数，进行类型分类
        EXTRECT_PROMPT = QUERY_EXTRECT_PROMPT(message=query)
        return await self._call_agent(EXTRECT_PROMPT)

    async def _search_parameters(self, extract_result: Dict[str, Any]) -> Dict[str, Any]:
        """搜索参数含义"""
        # 准备搜索数据（排除None值）
        search_data = {
            k: v for k, v in extract_result.items()
            if v is not None and k in self.parser.predefined_keys
        }
        # 批量并发搜索
        db_search_result = await self.db_searcher.batch_search_fields(search_data)
        # 格式化结果
        return json.dumps(db_search_result, ensure_ascii=False, indent=2)

    async def _understand_and_rewrite(self, query: str, db_search_results: str) -> str:
        """问题理解和改写"""
        # 这里替换为实际的理解提示词调用
        UNDERSTAND_PROMPT = QUERY_UNDERSTAND_PROMPT(description=query, parameters_definition=db_search_results)
        return await self._call_agent(UNDERSTAND_PROMPT)


async def query_analyse(task: Task) -> str:
    """问题理解改写agent"""
    query = task.description
    context = task.history
    query_understand_agent = QueryUnderstandAgent()
    return await query_understand_agent.process(query, context)