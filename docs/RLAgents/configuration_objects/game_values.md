# 🚀 Rocket League Game Values - RLGym Cheatsheet (Summary)

This guide contains the essential physical constants and arena dimensions for Rocket League, specifically for use within the RLGym/RocketSim ecosystem.

## 📏 Arena Dimensions (Coordinates)
The center of the field is the origin point `(0, 0, 0)`.

| Component | Axis | Values (Unreal Units) |
| :--- | :--- | :--- |
| **Length** | Y | +/- 5120 (Total 10240) |
| **Width** | X | +/- 4096 (Total 8192) |
| **Height (Ceiling)** | Z | 2044 |
| **Goal Width** | X | +/- 892.75 |
| **Goal Height** | Z | 642.775 |

## ⚽ Ball Physics
| Property | Value |
| :--- | :--- |
| **Ball Radius** | 91.25 uu |
| **Max Linear Velocity** | 6000 uu/s |
| **Max Angular Velocity** | 6.0 rad/s |

## 🏎️ Car Physics (Reference: Octane)
| Property | Value |
| :--- | :--- |
| **Max Velocity** | 2300 uu/s |
| **Boost Acceleration** | 991.667 uu/s² |
| **Throttle Acceleration** | 1600 uu/s² (when between 0-1400 speed) |
| **Gravity** | -650 uu/s² |
| **Supersonic Speed** | > 2200 uu/s |

## ⚡ Boost System
| Type | Reward | Respawn Time |
| :--- | :--- | :--- |
| **Small Pad** | 12.0% | 4 seconds |
| **Big Pad (Orb)** | 100.0% | 10 seconds |

## ⏱️ Time and Frequency Constants
* **Physics Tick Rate:** 120 Hz (Physics is calculated 120 times per second).
* **RLGym Step (Tick Skip 8):** 15 Hz (The agent makes a decision every 8 physics ticks).
* **Conversion:** 1 second in-game = 120 physics ticks.

---
*Compiled for technical reference in Reinforcement Learning training.*