# 🏁 RLGym Done Conditions - Quick Reference

A `DoneCondition` determines exactly when a training episode should end. In RLGym v2, these conditions can signal either a **Terminal** state (natural end) or a **Truncated** state (early exit for efficiency).

## ⚙️ Core Logic
To create a custom condition, you must implement two methods:
* `reset(...)`: Called at the start of every episode to initialize variables.
* `is_done(...)`: Called every step. It returns a dictionary mapping each `AgentID` to a boolean (`True` if the episode should end).

## 📋 Common Types of Conditions

### 1. Goal Condition (Terminal)
Ends the episode immediately after a goal is scored. This is the most basic requirement for a match environment.
* **Trigger:** `state.goal_scored == True`.

### 2. Timeout Condition (Truncated)
Ends the episode after a fixed amount of time (e.g., 30 seconds) regardless of what is happening.
* **Purpose:** Prevents the agent from getting stuck in infinite loops where nothing happens.

### 3. No-Touch Timeout (Truncated)
Ends the episode if no player has touched the ball for a specific duration.
* **Purpose:** Forces the agent to learn to interact with the ball rather than just driving in circles.

## 🖇️ Combining Conditions
Usually, you want multiple conditions active at once (e.g., end if someone scores **OR** if the timer runs out). RLGym provides wrappers for this:

* **`AnyCondition([cond1, cond2])`**: Returns `True` if **at least one** condition is met (Logical OR). Most common for training.
* **`AllCondition([cond1, cond2])`**: Returns `True` only if **all** conditions are met (Logical AND).