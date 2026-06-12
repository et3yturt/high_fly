🚀 High fly - Pygame Arcade Game

A simple 2D arcade-style flying game built with Python and Pygame. Control your jet, collect coins and health packs, and survive as long as possible while avoiding enemies and obstacles.





🎮 Gameplay

You pilot a jet across the sky while different objects move toward you:

Collect
🪙 Coins → Increase your score
❤️ Health Packs → Restore health
Avoid
👾 Enemies → -10 health
☁️ Clouds → -5 health
🚀 Spacecrafts → -40 health

The game ends when your health reaches 0.

📸 Features
Real-time sprite movement
Collision detection
Health system
Score tracking
Random object spawning
Game Over screen
Restart functionality
Multiple obstacle and collectible types
🕹 Controls
Key	Action
↑	Move Up
↓	Move Down
←	Move Left
→	Move Right
R	Restart after Game Over
ESC	Quit Game
📂 Project Structure
project/
│
├── main.py
├── jet.png
├── cloud.png
├── coin.png
├── health.png
├── fog.png
├── spacecraft.png
├── Image20251219175548.png
└── README.md
⚙️ Installation
1. Clone the repository
git clone https://github.com/yourusername/sky-adventure.git
cd sky-adventure
2. Install dependencies
pip install pygame
3. Run the game
python main.py
🎯 Game Mechanics
Health System
Object	Effect
Enemy	-10 HP
Cloud	-5 HP
Spacecraft	-40 HP
Health Pack	+20 HP

Starting Health:

live = 100
Score System

Collecting coins increases your score:

score += 1
🔄 Object Spawn Rates
Object	Spawn Time
Enemy	300 ms
Coin	500 ms
Cloud	1000 ms
Spacecraft	3000 ms
Health Pack	6000 ms
Fog	100000 ms
🛠 Built With
Python
Pygame
🐛 Known Issues
ESC key currently contains a typo (RUNING instead of running) and may not quit correctly.
Player can move outside screen boundaries.
Restart creates a new player object without clearing all existing sprites.
📜 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Created as a Python/Pygame learning project to explore:

Sprite systems
Collision detection
Event timers
<img width="1194" height="792" alt="image" src="https://github.com/user-attachments/assets/ed9adc63-a005-42b4-94dc-2c7aee7f38d2" />

Game loops
Object-oriented programming

Feel free to fork, improve, and contribute!
