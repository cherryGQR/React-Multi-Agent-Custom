#models/message.py
from dataclasses import dataclass
from typing import Dict, Any, Optional
from enum import Enum

class AgentRole(Enum):
    PLAN = "plan_agent"
    ACTION = "action_agent"
    OBSERVATION = "observation_agent"
    HUMANFEEDBACK = "human_feedback"
    REFLECTION = "reflection_agent"

@dataclass
class Message:
    role: AgentRole
    content: str
    metadata: Dict[str, Any] = None
    sub_agent: Optional[str] = None  # 新增：记录具体执行的子代理名称

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}
