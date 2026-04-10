# 🚗 Car Racing Dodge Game – Technical Documentation

---

## 1. 📌 Project Overview

This project is a **2D arcade-style car racing avoidance game** developed using the **Pygame** library. The primary objective is to control a player vehicle and avoid collisions with dynamically spawned enemy cars while the game progressively increases in difficulty.

The system is designed with a strong emphasis on:

* **Object-Oriented Programming (OOP)**
* **Modular architecture**
* **State-driven game flow**
* **Scalability and maintainability**

---

## 2. 🧱 System Architecture

The application follows a **layered modular architecture**, where each component is responsible for a specific domain:

### Core Layers:

1. **Game Engine Layer**

   * `game.py`
   * Controls execution and lifecycle

2. **State Management Layer**

   * `states.py`
   * Controls game flow (Menu, Play, Game Over)

3. **Entity Layer**

   * `player_car.py`
   * `enemy_car.py`
   * Defines game objects and behaviors

4. **Manager Layer**

   * `enemy_manager.py`
   * Handles collections of entities

5. **Rendering Layer**

   * `background.py`
   * Manages visual presentation

6. **Resource Layer**

   * `asset_manager.py`
   * `audio_manager.py`
   * Handles external resources

---

## 3. 🎮 Game Loop Design

The system implements a standard **real-time game loop**:

```python
while self.running:
    self.state.handle()
    self.state.update()
    self.state.render()
    pygame.display.update()
    self.clock.tick(60)
```

### Responsibilities:

* **handle()** → Processes input events
* **update()** → Updates game logic and physics
* **render()** → Draws all visual elements
* **tick(60)** → Maintains a stable 60 FPS

---

## 4. 📦 Asset Management (`asset_manager.py`)

### Purpose:

Centralized loading and storage of graphical assets.

### Design Considerations:

* Uses `pathlib.Path` for platform-independent paths
* Loads all assets once to avoid redundant disk I/O

### Key Components:

#### Path Initialization

```python
self.path = Path(__file__).parent
```

Ensures all asset paths are relative to the script location.

#### Image Loading

```python
self.player = pygame.image.load(img / "PLAYER_CAR19.png")
```

#### Enemy Variants

```python
self.enemy_cars = [
    pygame.transform.flip(pygame.image.load(img / f"CARE{i}.png"), False, True)
    for i in range(1, 20)
]
```

* Loads multiple enemy sprites
* Applies vertical flipping to standardize orientation

### Advantages:

* Reduces runtime loading overhead
* Improves performance and organization

---

## 5. 🔊 Audio Management (`audio_manager.py`)

### Purpose:

Handles all sound-related operations.

### Components:

#### Background Music

```python
pygame.mixer.music.load(self.lobby)
pygame.mixer.music.play(-1)
```

* Uses streaming playback
* Loop set to infinite

#### Sound Effects

```python
self.crash = pygame.mixer.Sound(...)
```

* Preloaded for low-latency playback

### Design Benefits:

* Separation of concerns
* Easy extensibility for additional sounds

---

## 6. 🛣️ Background System (`background.py`)

### Purpose:

Simulates continuous road movement using vertical scrolling.

### Technique:

**Dual-image scrolling system**

### Implementation:

#### Initial Positions

```python
self.y1 = 0
self.y2 = -self.image.get_height()
```

#### Update Logic

```python
self.y1 += self.speed
self.y2 += self.speed
```

#### Reset Mechanism

```python
if self.y1 >= height:
    self.y1 = self.y2 - self.image.get_height()
```

### Key Insight:

This creates the illusion of an **infinite scrolling track** without needing infinite assets.

---

## 7. 🚗 Player System (`player_car.py`)

### Purpose:

Defines player-controlled vehicle behavior.

### Features:

* Smooth acceleration/deceleration
* Dynamic speed scaling
* Boundary enforcement
* Pixel-perfect collision mask

### Input Handling:

```python
keys = pygame.key.get_pressed()
```

### Speed System:

```python
self.speed += 0.1
self.speed = max(self.min_speed, min(self.speed, self.max_speed))
```

### Dynamic Difficulty:

```python
self.max_speed = 10 + (score ** 0.5) * 0.08
```

* Uses square root scaling for balanced progression

### Boundary Constraints:

```python
if self.x > self.left:
```

Prevents player from leaving road bounds.

---

## 8. 🚙 Enemy System (`enemy_car.py`)

### Purpose:

Represents autonomous enemy vehicles.

### Behavior Model:

* Random spawn position
* Random speed assignment
* Probabilistic lane switching

### Lane Switching AI:

```python
if random.random() < 0.01:
    self.target_lane = random.choice(self.lanes)
```

### Smooth Transition:

```python
if self.x < self.target_lane:
    self.x += self.switch_speed
```

### Collision Detection:

```python
self.mask = pygame.mask.from_surface(self.image)
```

```python
player.mask.overlap(...)
```

### Benefit:

Provides **pixel-perfect collision detection**, improving gameplay accuracy.

---

## 9. 👾 Enemy Manager (`enemy_manager.py`)

### Purpose:

Manages lifecycle of all enemy entities.

### Responsibilities:

* Spawn control
* Update delegation
* Memory cleanup
* Collision aggregation

### Lane System:

```python
lane_width = (right - left) // 3
```

Creates three evenly spaced lanes.

### Spawn Control:

```python
pygame.time.get_ticks()
```

Ensures enemies spawn at controlled intervals.

### Memory Management:

```python
if enemy.y > height:
    self.enemies.remove(enemy)
```

Prevents memory overflow by removing off-screen objects.

---

## 10. 🧠 State Management (`states.py`)

### Design Pattern:

Implements the **State Pattern**.

### Base Class:

```python
class State:
```

Defines interface:

* `handle()`
* `update()`
* `render()`

---

### 🟢 Menu State

#### Responsibilities:

* Display title screen
* Handle game start input

#### Key Logic:

```python
if e.key == pygame.K_SPACE:
```

Transitions to gameplay.

---

### 🔵 Play State

#### Responsibilities:

* Core gameplay execution
* Score tracking
* Difficulty scaling
* Collision detection

#### Score System:

```python
self.score += 1
```

#### Difficulty Scaling:

```python
bg_speed = 6 + (self.score ** 0.5) * 0.25
enemy_speed = 5 + (self.score ** 0.5) * 0.1
```

#### Collision Handling:

```python
if self.enemies.check_collision(self.player):
```

Triggers:

* Sound effect
* Score saving
* State transition

---

### 🔴 Game Over State

#### Responsibilities:

* Display results
* Show leaderboard
* Restart flow

#### Transition:

```python
self.game.change_state("MENU")
```

---

## 11. 🎯 Core Game Controller (`game.py`)

### Purpose:

Central orchestration of all systems.

### Initialization:

```python
pygame.init()
pygame.mixer.init()
```

### State Registration:

```python
self.states = {
    "MENU": MenuState(self),
    "PLAY": PlayState(self),
    "GAMEOVER": GameOverState(self)
}
```

### State Transition:

```python
def change_state(self, name):
```

Ensures clean reinitialization of gameplay.

---

## 12. 💾 Persistence System (High Scores)

### Storage:

* File: `scores.txt`

### Load Logic:

```python
with open("scores.txt", "r")
```

### Save Logic:

```python
sorted(self.highscores, reverse=True)[:5]
```

### Features:

* Maintains top 5 scores
* Persistent across sessions

---

## 13. ▶️ Entry Point (`main.py`)

```python
if __name__ == "__main__":
    Game().run()
```

### Purpose:

* Launches the application
* Ensures modular execution

---

## 14. ⚙️ Performance Considerations

* **Asset preloading** reduces runtime lag
* **Object reuse and cleanup** prevents memory leaks
* **Frame rate control (60 FPS)** ensures smooth gameplay
* **Efficient collision detection (mask-based)** balances accuracy and performance

---

## 15. 🚀 Key Features Summary

* Real-time player control system
* Infinite scrolling background
* Dynamic enemy AI behavior
* Progressive difficulty scaling
* Pixel-perfect collision detection
* Persistent high score system
* Modular and extensible architecture

---

## 16. 🔮 Future Enhancements

Potential improvements include:

* Advanced enemy AI (path prediction)
* Power-up system (boost, shield)
* Multiple environments/maps
* UI enhancements (buttons, animations)
* Sound control settings
* Multiplayer functionality

---

## 17. 📌 Conclusion

This project demonstrates strong application of:

* Object-Oriented Design
* Game loop architecture
* State pattern implementation
* Real-time input handling
* Resource management

It provides a robust foundation for developing more advanced 2D or arcade-style games using Pygame.

---

**This is the end of our Technical Documentation**
