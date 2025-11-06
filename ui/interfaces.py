from abc import ABC, abstractmethod

class ICellView(ABC):
    """
    Interface for a renderer that is independent of the concrete GUI implementation.
    This allows swapping the UI layer (Tkinter, console, web, etc.) without changing
    the core game logic.
    """

    @abstractmethod
    def update_cell(self, r: int, c: int, cell) -> None:
        """
        Update the visual representation of a single cell at (r, c).
        """
        pass

    @abstractmethod
    def show_message(self, title: str, message: str) -> None:
        """
        Display a message to the user for victory or defeat.
        """
        pass
