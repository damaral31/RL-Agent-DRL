# 🧠 Reinforcement Learning Terms - RLGym Cheatsheet

This document outlines the core concepts and mathematical definitions used in the RLGym environment to help you understand how agents learn.

## 1. The Basics
* **Environment ($P$):** The decision process characterized by states, actions, and transition probabilities.
* **State ($S$):** The complete physical state of the game (e.g., exact physics of all objects).
* **Observation ($O$):** The specific representation of the state that the agent actually "sees" (often normalized or filtered).
* **Policy ($\pi$):** The "strategy" or function that maps an observation to an action.
* **Reward ($R$):** A scalar value given to the agent after an action to indicate success or failure.
* **Timestep:** A single interaction cycle consisting of `(state, action, reward, next_state)`.


## 2. Trajectories and Returns
* **Trajectory ($\tau$):** Any sequence of timesteps from one state to another.
* **Episode:** A trajectory that starts at the initial state ($s_0$) and ends at a terminal state ($s_T$).
* **Return ($G$):** The total cumulative reward from a specific timestep until the end of the episode.
* **Discount Factor ($\gamma$):** A value between 0 and 1 that determines how much the agent cares about future rewards vs. immediate rewards.
    * *Closer to 0:* Short-term focus.
    * *Closer to 1:* Long-term strategy.

## 3. Value Functions (The "Quality" Measures)
* **State Value Function ($V(s)$):** The expected return if the agent starts in state $s$ and follows its current policy forever.
* **Action Value Function ($Q(s, a)$):** The expected return if the agent takes action $a$ in state $s$, and then follows its policy.
* **Advantage Function ($A(s, a)$):** The difference between the $Q$ value and the $V$ value ($Q - V$). It measures how much *better* a specific action is compared to the average action chosen by the policy.

## 4. The Learning Process
* **Objective Function ($J$):** What the agent tries to maximize (usually the expected total return).
* **Gradient Ascent:** The iterative process of adjusting the policy's parameters (weights) in the direction that increases the reward.
* **Learning Rate ($\eta$):** A small multiplier that determines how big of a "step" the agent takes during each update.


---
*Reference: RLGym Reinforcement Learning Background Cheatsheet*