"""
工具函数模块
包含各种工具函数和子代理实现
"""

from tools.llm_utils import async_llm_call
from tools.async_utils import async_input


def get_query_analyse():
    from tools.sub_agents_query_understand import query_analyse
    return query_analyse


def get_fail_complete_analyse():
    from tools.sub_agents_fail_complete_analyse import fail_complete_analyse
    return fail_complete_analyse


def get_fail_complete_resolve():
    from tools.sub_agents_fail_complete_resolve import fail_complete_resolve
    return fail_complete_resolve


from .sub_agents_query_understand import query_analyse
from .sub_agents_fail_complete_analyse import fail_complete_analyse
from .sub_agents_fail_complete_resolve import fail_complete_resolve

all = [
    'async_llm_call',
    'async_input',
    'query_analyse',
    'fail_complete_analyse',
    'fail_complete_resolve',
    # 'fail_background_analyse',
]