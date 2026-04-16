# 📺 RLGym Renderers - Quick Reference

The `Renderer` interface in RLGym v2 allows you to visualize the game state during training or evaluation. While training usually happens "headless" (no graphics) to save speed, renderers are essential for debugging and watching your bot play.

## ⚙️ Core Logic
A Renderer must implement two primary methods:
* `render(state, shared_info)`: Called whenever you want to visualize the current frame. It receives the `GameState` and any shared info.
* `close()`: Called once when the environment is closed to perform cleanup (e.g., closing a window or saving a file).

## 🛠️ Usage Flow
To use a renderer, you pass it to the RLGym constructor and then manually call `.render()` in your training/evaluation loop.

```python
# 1. Initialize with a renderer
env = RLGym(
    # ... other config ...
    renderer=MyRenderer() 
)

# 2. Call render in your loop
obs = env.reset()
while True:
    actions = agent.predict(obs)
    obs, reward, done, info = env.step(actions)
    
    env.render()  # This triggers the renderer's logic
```

---

### ⚠️ Important Note
*- **Performance:** Calling **```.render()```** significantly slows down training because it adds overhead for data processing and display. It is best practice to only enable rendering during evaluation or for short periods of debugging.*