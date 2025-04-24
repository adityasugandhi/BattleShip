# BattleShips Game

A Python implementation of the classic Battleship game where players strategically position ships on a grid and take turns firing at opponent ships.

## 🎮 Overview

BattleShips is a turn-based strategy game where two players place ships on a grid and attempt to sink their opponent's fleet by guessing the coordinates of their ships. This implementation provides a command-line interface for playing the game.

## 🚢 Features

- Customizable map size
- Multiple ship sizes
- Turn-based gameplay
- Ship placement with coordinate specification
- Attack system with hit detection
- Player management system

## 🛠️ Technology Stack

- **Language**: Python 3.6+
- **Architecture**: Object-oriented design with clear class separation
- **Dependencies**: None (uses standard library only)

## 📁 Project Structure

```
battleShips/
├── classes/
│   ├── __init__.py
│   ├── constants.py   # Constants and configurations
│   ├── fire.py        # Handles hit detection and effects
│   ├── game.py        # Main game logic and turn management
│   ├── grid.py        # Represents the battle grid
│   ├── missiles.py    # Missile functionality for attacks
│   ├── ships.py       # Ship creation and management
│   └── Users.py       # Player data and actions
└── main.py            # Entry point for the application
```

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/battleShips.git
   cd battleShips
   ```

2. Run the game:
   ```bash
   python main.py
   ```

## 🎲 How to Play

1. When prompted, enter the desired map size.
2. Two players (Alice and Bob) are automatically created.
3. Ships are positioned on the grid.
4. Players take turns attacking each other's ships.
5. The game runs for 3 attack rounds by default.

## 📚 Class Documentation

### Users
Represents a player in the game with ships and attack capabilities.

### Ships
Manages a fleet of ships, including creation, positioning, and status tracking.

### Game
Controls the game flow, player turns, and attack resolution.

### Fire
Handles missile impacts and damage to ships.

### Missile
Represents an attack projectile with coordinates.

### Battlegrid
Provides the game board representation.

### Const
Manages game constants and configurations.

## 🔄 Game Flow

1. Players initialize with ships of specified sizes
2. Players take turns selecting coordinates to attack
3. Attacks are resolved with hit/miss notifications
4. Ships lose "lifetime" when hit
5. The game continues for the specified number of rounds

## 🛣️ Roadmap

- Add graphical user interface
- Implement ship orientation (horizontal/vertical)
- Add different ship types with special abilities
- Support for saving/loading games
- Multiplayer over network
- Advanced AI opponents

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/battleShips](https://github.com/yourusername/battleShips)
