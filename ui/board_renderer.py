from ui.interfaces import ICellView

class BoardRenderer(ICellView):
    """
    Renderer for Tkinter UI.
    """

    def __init__(self, buttons):
        """
        Initialize the renderer with a 2D array of Tkinter Button widgets.
        """
        self.buttons = buttons

    def update_cell(self, r: int, c: int, cell):
        """
        Updates the visual representation of a single cell at (r, c)
        """
        b = self.buttons[r][c]

        if cell.revealed:
            if cell.is_mine:
                # Show mine and disable button
                b.config(text='*', relief='sunken', state='disabled')
            elif cell.adjacent > 0:
                # Show the number of adjacent mines
                b.config(text=str(cell.adjacent), relief='sunken', state='disabled')
            else:
                # Empty revealed cell
                b.config(text='', relief='sunken', state='disabled')
        else:
            # Cell not revealed: show flag or blank
            if cell.flagged:
                b.config(text='F')
            else:
                b.config(text=' ')

    def show_message(self, title: str, message: str):
        """
        Displays a popup message (e.g., for victory or defeat)..
        """
        import tkinter.messagebox as mb
        mb.showinfo(title, message)
