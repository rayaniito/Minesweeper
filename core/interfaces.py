from abc import ABC, abstractmethod

class IBoardLogic(ABC):
    """Abstract interface defining the core board logic API."""

    @abstractmethod
    def reveal(self, r: int, c: int):
        """
        Reveals the cell at (r, c)
        """
        pass

    @abstractmethod
    def toggle_flag(self, r: int, c: int):
        """
        Toggles a flag on the cell at (r, c)
        """
        pass

    @abstractmethod
    def get_cell(self, r: int, c: int):
        """
        Returns the cell object at the given coordinates.
        """
        pass

    @abstractmethod
    def get_board_size(self):
        """
        Returns the board dimensions as a (height, width) tuple.
        """
        pass


class IBoardGenerator(ABC):
    """Interface for mine placement strategies"""

    @abstractmethod
    def place_mines(self, height: int, width: int, num_mines: int):
        """
        Returns an iterable or collection of coordinates where mines should be placed.
        """
        pass


class ICellRenderer(ABC):
    """
    Interface for UI cell rendering
    """

    @abstractmethod
    def update_cell(self, r: int, c: int, cell):
        """
        Updates the visual representation of the cell at (r, c) which is called when a cell is revealed, flagged, or changed.
        """
        pass

    @abstractmethod
    def show_message(self, title: str, message: str):
        """
        Displays a message to the user (Game Over ! / You win !)
        """
        pass
