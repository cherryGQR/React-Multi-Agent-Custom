from dataclasses import dataclass, field
from typing import List, Any
from enum import Enum
from .message import Message

class AgentState(Enum):
    IDLE = "idle"
    PLANNING = "planning"
    ACTING = "acting"
    OBSERVING = "observing"
    HUMANFEEDBACK = "human_feedback"
    REFLECTING = "reflecting"
    COMPLETED = "completed"
    ERROR = "error"

@dataclass
class Task:
    id: str
    description: str
    status: AgentState = AgentState.IDLE
    result: Any = None
    history: List[Message] = field(default_factory=list)