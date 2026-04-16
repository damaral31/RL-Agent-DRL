# 🛠️ Creating Custom Environments in RLGym v2

RLGym v2 is built on a highly modular architecture. While primarily used for Rocket League, the API allows you to build any custom environment (like a Grid World or a specialized training drill) by implementing seven core components.

## 🏗️ Core Architecture Components
To create a functional environment, you must define the following objects:

1.  **State Type:** A `dataclass` that holds all raw information about your world (e.g., coordinates, velocities, timers).
2.  **Transition Engine:** The "Physics Engine." It takes the parsed actions and updates the **State Type**. This is where the core logic of your world lives.
3.  **State Mutator:** Handles the setup during `env.reset()`. It places objects and players in their starting positions.
4.  **Observation Builder:** Converts the raw **State** into a numerical format (usually a NumPy array) that the agent can "see."
5.  **Action Parser:** Defines what actions are possible (e.g., Discrete 0-4 or Continuous -1 to 1) and translates them for the Engine.
6.  **Reward Function:** Calculates the numerical "score" for each step to guide the agent's learning.
7.  **Done Conditions:** * **Terminal:** Natural ends (e.g., scoring a goal).
    * **Truncated:** Forced ends (e.g., running out of time).



## 📝 Implementation Workflow

### 1. The Transition Engine
The Engine is the heart of the environment. You must implement the `step()` method to define how actions change the world:
```python
def step(self, actions: Dict[AgentID, ActionType], shared_info: Dict[str, Any]) -> StateType:
    # 1. Receive actions from agents
    # 2. Update positions/physics based on those actions
    # 3. Handle collisions or game rules
    # 4. Return the updated State object
```
---
- ***More in***: https://rlgym.org/Custom%20Environments/custom-environment