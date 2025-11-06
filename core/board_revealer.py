from typing import List, Tuple
from core.cell import Cell
from core.exceptions import DefeatException, VictoryException

class BoardRevealer:
    """Responsible only for revealing cells and performing the flood-fill logic."""

    @staticmethod
    def reveal(cells: List[List[Cell]], mines: set, r: int, c: int, remaining_safe: int):
        """
        Reveals a cell and performs flood-fill if the cell has no adjacent mines
        """
        cell = cells[r][c]

        # If the cell is already revealed or flagged, nothing happens
        if cell.revealed or cell.flagged:
            return [], remaining_safe

        # If a mine is revealed → reveal all mines and trigger defeat
        if cell.is_mine:
            for mr, mc in mines:
                cells[mr][mc].revealed = True
            raise DefeatException("Boom! You hit a mine.")

        to_reveal = []
        stack = [(r, c)]  # Stack used for flood-fill (DFS)
        height, width = len(cells), len(cells[0])

        # Iterative flood-fill to reveal empty areas
        while stack:
            cr, cc = stack.pop()
            ccell = cells[cr][cc]

            # Skip cells already processed or flagged
            if ccell.revealed or ccell.flagged:
                continue

            # Reveal the cell
            ccell.revealed = True
            to_reveal.append((cr, cc))
            remaining_safe -= 1

            # If cell has no adjacent mines, expand to its neighbors
            if ccell.adjacent == 0:
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < height and 0 <= nc < width:
                            ncell = cells[nr][nc]
                            # Add only non-revealed, non-mine neighbors to flood-fill
                            if not ncell.revealed and not ncell.is_mine:
                                stack.append((nr, nc))

        # If all safe cells are revealed → player wins
        if remaining_safe == 0:
            raise VictoryException("You win and cleared the board!")

        return to_reveal, remaining_safe
