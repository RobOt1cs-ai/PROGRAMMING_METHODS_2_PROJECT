# 🚗 Car Racing Dodge Game (Python + Pygame)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A fast-paced **arcade-style car dodging game** built with **Python** and **Pygame**. Avoid incoming traffic, survive as long as possible, and climb the high score leaderboard.

---

## 🎮 Features

* Smooth player movement with acceleration & deceleration
* Dynamic enemy spawning with lane-switching AI
* Progressive difficulty scaling based on score
* Background music and crash sound effects
* High score system (top 5 saved locally)
* Clean game architecture using state management
* Organized asset handling system

---

## 🗂️ Project Structure

```
PM2_PROJECT/
│
├── assets/
│   ├── img/
│   ├── audio/
│   ├── asset_manager.py
│   └── audio_manager.py
│
├── background.py
├── enemy_car.py
├── enemy_manager.py
├── player_car.py
├── states.py
├── game.py
├── main.py
├── scores.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/car-racing-game.git
cd car-racing-game
```

### Create Virtual Environment

```bash
python -m venv env
```

Activate:

* Windows:

```bash
env\Scripts\activate
```

* Mac/Linux:

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install pygame
```

---

## ▶️ Run the Game

```bash
python main.py
```

---

## 🎮 Controls

| Key     | Action         |
| ------- | -------------- |
| ⬅️ / A  | Move Left      |
| ➡️ / D  | Move Right     |
| ⬆️ / W  | Accelerate     |
| ⬇️ / S  | Decelerate     |
| SPACE   | Start Game     |
| ANY KEY | Return to Menu |

---

## 🧠 Gameplay

* Drive within 3 lanes and avoid enemy cars
* Enemy cars randomly spawn and may switch lanes
* Speed increases as score increases
* Game ends on collision
* Scores are saved automatically

---

## 🖼️ Screenshots (How to Add Real Ones)

### 📸 Step-by-step

1. Run your game:

```bash
python main.py
```

2. Take screenshots:

* Press **Windows + Shift + S** (Windows)
* Or **Cmd + Shift + 4** (Mac)

3. Save images in:

```
assets/screenshots/
```

4. Add them below:

```
![Menu](assets/screenshots/menu.png)
![Gameplay](assets/screenshots/gameplay.png)
![Game Over](assets/screenshots/gameover.png)
```

---

## 🎥 Demo Video (How to Create One)

### 🎬 Quick Recording

Use:

* OBS Studio (recommended)
* Xbox Game Bar (Windows: `Win + Alt + R`)

### 📌 What to Show (Script)

**Scene 1 – Intro (3–5 sec)**

* Show menu screen
* Text: *"Python Car Racing Game"*

**Scene 2 – Gameplay (10–20 sec)**

* Start game
* Show movement (left/right, speed control)
* Show enemies spawning

**Scene 3 – Difficulty Scaling**

* Let score increase
* Show faster gameplay

**Scene 4 – Crash**

* Hit an enemy car
* Show Game Over screen

**Scene 5 – High Scores**

* Highlight leaderboard

### Upload

* Upload to YouTube or Google Drive
* Add link here:

```
https://your-video-link.com
```

---

## 🧪 Code Highlights

### State Management

Clean separation of:

* MenuState
* PlayState
* GameOverState

### Enemy AI

* Random lane switching
* Smooth transitions

### Difficulty Scaling

```python
enemy_speed = 5 + (score ** 0.5) * 0.08
```

---

## 🧾 Git Best Practices (Evidence)

### ✅ Commit Examples

```
feat: add enemy spawning system
fix: correct collision detection bug
refactor: improve state management structure
```

### ✅ Branching Strategy

* `main` → stable version
* `feature/*` → new features
* `fix/*` → bug fixes

### ✅ Workflow

```bash
git checkout -b feature/enemy-ai
git add .
git commit -m "feat: implement enemy lane switching"
git push origin feature/enemy-ai
```

### 📸 Add Git Proof (IMPORTANT)

Take screenshots of:

* Your commit history (VS Code / GitHub)
* Your branches
* Pull requests (if any)

Add here:

```
![Commits](assets/screenshots/git_commits.png)
![Branches](assets/screenshots/git_branches.png)
```

---

## 🚀 Future Improvements

* Add animations (explosions, particles)
* Online leaderboard
* Pause system
* Mobile version
* More sound effects

---

## 🐞 Known Issues

* Collision may feel strict at high speed
* No pause feature yet

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Your Name
https://github.com/your-username

---

⭐ If you like this project, give it a star!
