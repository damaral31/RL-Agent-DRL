# 🏆 RLGym Reward Functions - Quick Reference

The `RewardFunction` is the "brain" of the reinforcement learning process. It defines the goal of the agent by assigning a numerical value (reward) to every action taken in a specific state.

## ⚙️ Core Logic
Every reward function must implement two methods:
* `reset(...)`: Called at the start of an episode to reset any accumulators or trackers.
* `get_rewards(...)`: Called every environment step. It returns a dictionary mapping each `AgentID` to a float value.

## 🧱 The Reward Loop
The agent's goal is to maximize the **Cumulative Reward**.
1. **Agent** performs an action.
2. **Environment** updates the physics.
3. **Reward Function** inspects the new state and says "That was good (+1)" or "That was bad (-0.1)".


## 🛠️ Common Reward Strategies

### 1. Velocity-Based
Rewards the agent for moving fast or moving toward the ball.
* *Example:* `VelocityBallReward` (higher reward if the car's velocity vector points toward the ball).

### 2. Event-Based
Rewards for specific game milestones.
* *Examples:* `GoalReward`, `SaveReward`, `ShotReward`.

### 3. Positioning-Based
Encourages the agent to stay behind the ball or face the opponent's goal.
* *Example:* `FaceBallReward`.

## ⚖️ Combining Rewards (The Weighted Sum)
In a real environment, you rarely use just one reward. You combine them using a weighted sum so the agent balances multiple objectives.

```python
from rlgym.rocket_league.reward_functions import CombinedReward, GoalReward, VelocityBallReward

# The agent gets 10 points for a goal, and a small constant reward for moving toward the ball.
reward_fn = CombinedReward(
    (GoalReward(), 10.0),
    (VelocityBallReward(), 0.1)
)
```