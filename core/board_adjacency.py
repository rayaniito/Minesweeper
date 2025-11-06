from typing import List
from core.cell import Cell

class BoardAdjacencyCalculator:
    """Responsible only for calculating the number of adjacent mines for each cell"""

    @staticmethod
    def compute_adjacency(cells: List[List[Cell]]):
        """
        Computes the number of mines adjacent to each non-mine cell on the board
        """
        height = len(cells)
        width = len(cells[0])

        for r in range(height):
            for c in range(width):
                # Only compute adjacency for non-mine cells
                if not cells[r][c].is_mine:
                    cells[r][c].adjacent = BoardAdjacencyCalculator._count_adjacent(cells, r, c)

    @staticmethod
    def _neighbors(cells: List[List[Cell]], r: int, c: int):
        """ 
        Returns the list of valid neighbor coordinates around a given cell
        """
        height = len(cells)
        width = len(cells[0])
        result = []

        # Loop through surrounding directions: (-1, 0, 1) for rows and columns
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                # Skip the cell itself
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc

                # Only include neighbors that fall within the board limits
                if 0 <= nr < height and 0 <= nc < width:
                    result.append((nr, nc))

        return result

    @staticmethod
    def _count_adjacent(cells: List[List[Cell]], r: int, c: int):
        """
        Counts how many of the neighboring cells contain a mine.
        """
        # Sum +1 for each neighbor that is a mine
        return sum(
            1 for nr, nc in BoardAdjacencyCalculator._neighbors(cells, r, c)
            if cells[nr][nc].is_mine
        )
