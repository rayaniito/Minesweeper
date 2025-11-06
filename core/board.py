from typing import List, Tuple
from core.cell import Cell
from core.interfaces import IBoardGenerator, IBoardLogic
from core.board_initializer import BoardInitializer
from core.board_adjacency import BoardAdjacencyCalculator
from core.board_revealer import BoardRevealer

class Board(IBoardLogic):
    """Coordinates the board and delegates responsibilities to specialized components."""

    def __init__(self, height: int, width: int, num_mines: int, generator: IBoardGenerator):
        """
        Creates a board and prepares the internal structure, but does not place mines yet.
        Mine placement is delayed until the first reveal to guarantee a safe first click.
        """
        if num_mines >= height * width:
            raise ValueError("Too many mines")

        self.height = height
        self.width = width
        self.num_mines = num_mines
        self.generator = generator

        # 2D grid of Cell objects
        self._cells: List[List[Cell]] = [
            [Cell() for _ in range(width)]
            for _ in range(height)
        ]

        self._mines = set()              # Stores mine coordinates once initialized
        self._initialized = False        # Indicates whether mines + adjacency are set
        self._remaining_safe = height * width - num_mines  # Used to detect victory

    def initialize(self, first_click: Tuple[int, int] = None):
        """
        It places mines (ensuring the first clicked cell is safe, if provided) and computes adjacency numbers for all cells
        """
        self._mines = BoardInitializer(self.generator).place_mines(
            self._cells, self.num_mines, first_click
        )
        BoardAdjacencyCalculator.compute_adjacency(self._cells)
        self._initialized = True

    def reveal(self, r: int, c: int):
        """
        Reveals a cell and returns a list of revealed cell coordinates
        """
        if not self._initialized:
            self.initialize(first_click=(r, c))

        # Delegate revealing and flood-fill logic to BoardRevealer
        revealed, self._remaining_safe = BoardRevealer.reveal(
            self._cells, self._mines, r, c, self._remaining_safe
        )
        return revealed

    def toggle_flag(self, r: int, c: int):
        """toggles a flag on a cell"""
        return self._cells[r][c].toggle_flag()

    def get_cell(self, r: int, c: int):
        """returns the requested cell object."""
        return self._cells[r][c]

    def get_board_size(self):
        """returns the board dimensions as a (height, width) tuple."""
        return self.height, self.width

    def get_num_mines(self) -> int:
        """Returns the number of mines on the board."""
        return self.num_mines
