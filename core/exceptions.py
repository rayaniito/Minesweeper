class DefeatException(Exception):
    """Raised when the player reveals a mine (game over)."""
    pass

class VictoryException(Exception):
    """Raised when the player has successfully revealed all safe cells (win condition)."""
    pass
