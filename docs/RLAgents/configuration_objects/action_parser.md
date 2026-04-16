# 🕹️ RLGym Action Parsers - Quick Reference

An `ActionParser` is the bridge between your agent's neural network and the game physics. It translates the raw mathematical output from the policy into the 8 specific controller inputs (Throttle, Steer, Jump, etc.) that Rocket League/RocketSim understands.

## ⚙️ Core Logic
Every Action Parser must implement three primary methods:
* `get_action_space(agent)`: Defines the shape and type of the output (Continuous vs. Discrete). This tells the learning algorithm how many neurons the output layer should have.
* `reset(initial_state, shared_info)`: Resets any internal state variables at the start of an episode.
* `parse_actions(actions, state, shared_info)`: The core logic that maps the agent's raw numbers into valid game controls.

## 🛠️ Common Parser Types

### 1. Continuous Action Parser
* **Input:** A vector of 8 floats (usually between -1 and 1).
* **Logic:** Maps the first 5 values directly to axes (Throttle, Steer, Pitch, Yaw, Roll) and converts the last 3 values into binary (0 or 1) for Jump, Boost, and Handbrake.
* **Best for:** Fine-grained control and advanced aerials.

### 2. Discrete Action Parser
* **Input:** A single integer or a set of discrete choices.
* **Logic:** Maps a specific number to a "pre-packaged" move. For example, `Action 5` might be mapped to `[Throttle=1, Jump=1]`.
* **Best for:** Simplifying the learning process for beginners or specific training tasks (like kickoffs).