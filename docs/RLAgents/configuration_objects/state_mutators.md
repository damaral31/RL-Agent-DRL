# 🎲 RLGym State Mutators - Quick Reference

A `StateMutator` is responsible for setting up or modifying the initial state of the game at the start of every episode (reset). They define where the cars start, where the ball is, and how much boost everyone has.

## ⚙️ Core Logic
A State Mutator has one primary method:
* `apply(state, shared_info)`: This method directly modifies the `GameState` object. It is called during `env.reset()` but before the first step of the episode is taken.

## 🧱 Mutator Sequence
In RLGym v2, you rarely use just one mutator. You use a `MutatorSequence` to apply multiple changes in order. For example:
1.  **Mutator A** creates the cars (e.g., `FixedTeamSizeMutator`).
2.  **Mutator B** places them in kickoff positions (e.g., `KickoffMutator`).
3.  **Mutator C** gives everyone 100% boost for a specific drill.


## 🛠️ Common Mutator Types

### 1. FixedTeamSizeMutator
Defines how many agents/cars are on the Blue and Orange teams (e.g., 1v1, 2v2, 3v3).

### 2. KickoffMutator
Resets the ball to the center and places cars in the standard Rocket League kickoff positions.

### 3. RandomStateMutator
Spawns the ball and cars in random positions, velocities, and rotations. 
* **Benefit:** Highly recommended for general training as it prevents the bot from only learning how to play from a kickoff.

## 🚀 Example: Custom Training Drill
You can create a mutator to practice specific scenarios, like defending a high ball:
```python
class DefenseDrillMutator(StateMutator):
    def apply(self, state: GameState, shared_info: Dict[str, Any]) -> None:
        # Put the ball high in the air moving toward the Blue goal
        state.ball.position = np.array([0, 2000, 1500])
        state.ball.linear_velocity = np.array([0, 1500, 0])
        
        # Put the agent in the goal with 0 boost
        for car in state.cars.values():
            car.physics.position = np.array([0, -5000, 17])
            car.boost = 0
```