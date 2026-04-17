from typing import List, Dict, Any

from rlgym.api import DoneCondition, AgentID
from rlgym.rocket_league.api import GameState
from rlgym.rocket_league.common_values import TICKS_PER_SECOND

class TimeoutCondition(DoneCondition[AgentID, GameState]):
    """
    A DoneCondition that is satisfied when a specified amount of time has elapsed.
    """
    def __init__(self, timeout_seconds: float):
        """
        Args:
            timeout_seconds: Timeout in seconds
        """
        
        self.timeout_seconds = timeout_seconds

    def reset(self, agents: List[AgentID], initial_state: GameState, shared_info: Dict[str, Any]) -> None:
        pass

    def is_done(self, agents: List[AgentID], state: GameState, shared_info: Dict[str, Any]) -> Dict[AgentID, bool]:
        time_elapsed = state.tick_count / TICKS_PER_SECOND
        done = time_elapsed >= self.timeout_seconds
        return {agent: done for agent in agents}