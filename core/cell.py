from dataclasses import dataclass

@dataclass
class Cell:
    """represents the state of a single cell on the board."""
    is_mine: bool = False       # True if this cell contains a mine
    adjacent: int = 0           # Number of adjacent mines
    revealed: bool = False      # True if the cell has been revealed
    flagged: bool = False       # True if the player marked this cell with a flag

    def reveal(self):
        """
        If it is not flagged it returns True if the cell was successfully revealed, False otherwise
        """
        if self.flagged:
            return False
        self.revealed = True
        return True

    def toggle_flag(self):
        """
        toggles a flag on this cell if it has not been revealed
        """
        if self.revealed:
            return False
        self.flagged = not self.flagged
        return True
