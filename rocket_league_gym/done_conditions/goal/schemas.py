from pydantic import BaseModel
from typing import List

from rlgym.api import AgentID

class GoalDoneConditionItem(BaseModel):
    """
    Represents a single goal done condition item.
    """
    agent_id: AgentID
    has_scored: bool

class GoalDoneConditionSchema(BaseModel):
    """
    Schema for the GoalDoneCondition configuration.
    """

    goals: List[GoalDoneConditionItem]