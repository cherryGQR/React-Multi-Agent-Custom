"""
数据模型模块
包含任务和消息的数据模型定义
"""

from .task import Task, AgentState
from .message import Message, AgentRole

all = [
    'Task',
    'AgentState',
    'Message',
    'AgentRole'
]
