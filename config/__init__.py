"""
配置模块
包含LLM配置和提示词模板
"""

from .models import LLM_CONFIGS, get_llm
from .prompts import (
    PLAN_AGENT_PROMPT,
    OBSERVATION_AGENT_PROMPT,
    REFLECTION_AGENT_PROMPT
)

from .query_understand_sub_agent_prompt import QUERY_EXTRECT_PROMPT

all = [
    'LLM_CONFIGS',
    'get_llm',
    'PLAN_AGENT_PROMPT',
    'OBSERVATION_AGENT_PROMPT',
    'REFLECTION_AGENT_PROMPT',
    'QUERY_EXTRECT_PROMPT'
]