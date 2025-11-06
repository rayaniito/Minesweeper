from typing import List, Tuple
from core.cell import Cell
from core.interfaces import IBoardGenerator
from random import choice

class BoardInitializer:
    """Responsible only for placing mines on the game board."""

    def __init__(self, generator: IBoardGenerator):
        # The generator determines how mines are placed (strategy injected via interface)
        self.generator = generator

    def place_mines(self, cells: List[List[Cell]], num_mines: int, first_click: Tuple[int, int] = None):
        """
        Places mines on the board and returns a set of coordinates where mines have been placed.
        """
        height = len(cells)
        width = len(cells[0])

        # Generate mine positions using the injected generator strategy.
        mines = set(self.generator.place_mines(height, width, num_mines))

        # Ensure the first clicked cell is not a mine (standard Minesweeper rule).
        if first_click and first_click in mines:
            # Remove the mine from the first clicked position
            mines.remove(first_click)

            # Pick a new random valid position to place the mine
            choices = [
                (r, c) for r in range(height) for c in range(width)
                if (r, c) not in mines and (r, c) != first_click
            ]
            mines.add(choice(choices))

        # Mark selected cells as mines
        for (r, c) in mines:
            cells[r][c].is_mine = True

        return mines
