# 📥 RLGym Input/Output Schema (Data Flow)

In RLGym, the communication between the agent and the environment follows a strictly defined loop. The agent receives an **Observation**, processes it through a policy, and outputs an **Action**.

---

## 1. The Observation (Input to Agent)
The observation is a numerical representation of the game world. In RLGym v2, the `DefaultObs` usually provides a flattened vector or a structured object containing:

### 🏎️ Self and Other Players
Each car (your agent, teammates, and opponents) provides:
* **Position:** `[x, y, z]` coordinates.
* **Linear Velocity:** `[vx, vy, vz]` (how fast it's moving in which direction).
* **Angular Velocity:** `[rvx, rvy, rvz]` (how fast it's spinning).
* **Orientation:** Represented as a **Rotation Matrix** (9 values) or **Quaternion** (4 values).
* **Boost Level:** A scalar value from `0` to `1`.
* **Status Flags:** Is the car on the ground? Has it used its dodge? Is it supersonic?

### ⚽ The Ball
* **Position:** `[x, y, z]`.
* **Linear Velocity:** `[vx, vy, vz]`.
* **Angular Velocity:** `[rvx, rvy, rvz]`.

> **Note:** Most observation builders **normalize** these values. For example, the Y-position is divided by 5120 so the input to the neural network stays between -1 and 1.

---

## 2. The Action (Output from Agent)
The agent outputs a vector of **8 values**. These values correspond exactly to the inputs a human would provide via a controller.



| Index | Name | Range | Function |
| :--- | :--- | :--- | :--- |
| **0** | **Throttle** | `[-1, 1]` | -1 for reverse, 1 for forward. |
| **1** | **Steer** | `[-1, 1]` | -1 for left, 1 for right. |
| **2** | **Pitch** | `[-1, 1]` | Nose down (1) or Nose up (-1). |
| **3** | **Yaw** | `[-1, 1]` | Turn left (-1) or right (1) in the air. |
| **4** | **Roll** | `[-1, 1]` | Barrel roll left (-1) or right (1). |
| **5** | **Jump** | `[0, 1]` | Values > 0.5 trigger a jump. |
| **6** | **Boost** | `[0, 1]` | Values > 0.5 activate boost. |
| **7** | **Handbrake** | `[0, 1]` | Values > 0.5 activate powerslide. |

---

## 3. The Transformation Layers
Data rarely goes from the game to the agent raw. Two objects handle the conversion:

### 🛠️ Observation Builder
Converts the `GameState` (raw physical data) into the `Observation` (the format your neural network expects).
* *Example:* Adding a "Distance to Ball" feature manually.

### 🛠️ Action Parser
Converts the agent's mathematical output back into something the game understands.
* *Continuous:* Uses the raw floats (Standard).
* *Discrete:* Maps a single integer (e.g., Action 5) to a specific combination of buttons (e.g., Jump + Forward).

---

## 🔄 The Step Loop
1.  **Env** sends `Observation` to **Agent**.
2.  **Agent** processes data and returns an `Action` vector (8 floats).
3.  **Env** applies the `Action` for $N$ ticks (usually 8).
4.  **Env** calculates the **Reward** and sends the next `Observation`.