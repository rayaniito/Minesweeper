from core.board import Board
from core.mine_generator import RandomMineGenerator
from core.interfaces import IBoardGenerator, IBoardLogic

class GameController:
    """Manages the creation of a board and exposes the Board interface to the UI."""

    def __init__(self, height: int, width: int, num_mines: int, generator: IBoardGenerator = None):
        """
        Creates a new game controller
        """
        self.height = height
        self.width = width
        self.num_mines = num_mines

        # Use a default RandomMineGenerator if none is provided
        self.generator = generator or RandomMineGenerator()

        # Create the initial board
        self.board = self._create_board()

    def _create_board(self) -> IBoardLogic:
        """
        instantiates a new Board using the configured generator and parameters
        """
        return Board(self.height, self.width, self.num_mines, self.generator)

    def get_board(self) -> IBoardLogic:
        """returns the current board instance"""
        return self.board

    def restart(self):
        """
        Creates a new board with the same configuration for restart the game
        """
        self.board = self._create_board()
        return self.board
