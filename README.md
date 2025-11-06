# Minesweeper MA5741 Project

Students : GE25Z211, GE25Z212, GE25Z213

Abstract :
This project aims to develop a Minesweeper game in Python using object-oriented programming (OOP) principles. The goal is to create a modular and extensible design, separating core game logic (mine generation, neighbor calculations, and win/lose conditions) from the graphical user interface. The game will feature recursive cell revelation, flag placement, and customizable grid sizes. We will emphasize clean code, reusability, and maintainability by applying SOLID principles, ensuring a robust and scalable implementation. The project will also include unit tests to validate functionality and demonstrate the effectiveness of our OOP design.

This project is a Python implementation of the classic Minesweeper game.  
It follows Object-Oriented Programming principles and applies the SOLID design principles to ensure clean architecture, easy maintenance, and scalability.

The game includes a graphical interface built using Tkinter, allowing users to play Minesweeper interactively.

---

## Features

- Safe first click (the first revealed cell is never a mine)
- Recursive reveal of empty cells
- Flag system to mark suspected mines
- Victory and defeat detection
- Restart option integrated in the UI
- Fully modular architecture based on SOLID principles
- Easy to extend (new UI, mine generator strategies, or game rules)

---

## Project Architecture

The project is structured to clearly separate responsibilities:

| Folder / File | Responsibility |
|----------------|----------------|
| `core/` | Contains all game logic and rules |
| `ui/` | Contains the Tkinter graphical interface |
| `interfaces/` | Contains abstractions (interfaces) |
| `main.py` | Application entry point |
| `report.pdf` | Report of the project in pdf |

### Main Components

- **GameController**: Manages the overall game flow and acts as a bridge between the UI and the game logic.
- **Board**: Contains the core logic of Minesweeper and delegates tasks to helper classes.
- **Cell**: Represents a single square of the game grid.
- **BoardInitializer**: Places mines and sets up the board, ensuring that the first click is always safe.
- **BoardAdjacencyCalculator**: Calculates the number of adjacent mines for each cell.
- **BoardRevealer**: Handles the recursive reveal of empty cells.
- **BoardRenderer**: Updates the graphical board display.
- **MinesweeperUI**: Tkinter-based graphical interface for user interaction.

---

## How to Run the Game

### Requirements

- Python 3.8 or higher
- Tkinter (usually included by default with Python)

### Launch the game

Run the following command:

```bash
python3 main.py
