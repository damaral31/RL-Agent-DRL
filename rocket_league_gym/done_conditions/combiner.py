from rocket_league_gym.done_conditions.goal import GoalCondition
from rocket_league_gym.done_conditions.no_touch import NoTouchCondition
from rocket_league_gym.done_conditions.timeout import TimeoutCondition


from rlgym.rocket_league.done_conditions import AnyCondition, AllCondition


class ConditionCombiner():
    
    def __init__(self,
                 type: str,
                 goal: bool = True,
                 timeout_seconds: float = None,
                 no_touch_seconds: float = None) -> AnyCondition | AllCondition:
        
        assert type in ["any", "all"], "type must be either 'any' or 'all'"

        self.type = type
        self.timeout_seconds = timeout_seconds
        self.no_touch_seconds = no_touch_seconds
        self.goal = goal

        return self.create_combined_condition()


    def create_combined_condition(self):
        conditions = []
        if self.goal:
            conditions.append(GoalCondition())
        if self.timeout_seconds is not None:
            conditions.append(TimeoutCondition(self.timeout_seconds))
        if self.no_touch_seconds is not None:
            conditions.append(NoTouchCondition(self.no_touch_seconds))
        
        if len(conditions) == 1:
            return conditions[0]
        
        condition_class = AnyCondition if self.type == "any" else AllCondition
        return condition_class(conditions)
