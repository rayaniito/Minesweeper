import random
from core.interfaces import IBoardGenerator

class RandomMineGenerator(IBoardGenerator):
    """Random mine generator, fully compatible with DIP/OCP principles."""

    def __init__(self, seed=None):
        """
        Optional seed allows reproducible mine placement (for testing).
        """
        self.seed = seed

    def place_mines(self, height: int, width: int, num_mines: int):
        """
        Returns a set of mine coordinates randomly selected from the board grid.

        """
        # Use a seeded RNG if provided, otherwise use global random
        rnd = random.Random(self.seed) if self.seed is not None else random

        # Generate a list of all possible coordinates on the board
        all_coords = [(r, c) for r in range(height) for c in range(width)]

        # Randomly pick unique coordinates for mines
        mines = set(rnd.sample(all_coords, num_mines))
        return mines
