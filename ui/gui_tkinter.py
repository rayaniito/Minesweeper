import tkinter as tk
from core.exceptions import DefeatException, VictoryException
from ui.board_renderer import BoardRenderer
from core.game_controller import GameController

class MinesweeperUI(tk.Tk):

    def __init__(self, controller: GameController):
        """
        Initialize the UI and link it with a GameController.
        """
        super().__init__()
        self.title("Minesweeper")

        self.controller = controller
        self.board = controller.get_board()
        self.height, self.width = self.board.get_board_size()

        # Create a 2D list of Button widgets
        self.buttons = [[None for _ in range(self.width)] for _ in range(self.height)]

        # Renderer decouples UI update logic from game logic
        self.renderer = BoardRenderer(self.buttons)

        self._build_ui()

    def _build_ui(self):
        """Create grid of buttons and restart control button."""
        # Frame for the grid of cells
        self.frame_grid = tk.Frame(self)
        self.frame_grid.pack(padx=10, pady=10)

        for r in range(self.height):
            for c in range(self.width):
                # Create each button
                b = tk.Button(
                    self.frame_grid, text=' ', width=3, height=1,
                    command=lambda rr=r, cc=c: self._on_left(rr, cc)  # Left-click
                )
                # Right-click binding for flag toggle
                b.bind('<Button-3>', lambda e, rr=r, cc=c: self._on_right(rr, cc))
                b.grid(row=r, column=c)
                self.buttons[r][c] = b

        # Frame for the restart button
        self.frame_controls = tk.Frame(self)
        self.frame_controls.pack(pady=5)
        self.restart_button = tk.Button(
            self.frame_controls, text="Restart", command=self._restart
        )
        self.restart_button.pack()

    def _on_left(self, r, c):
        """
        Handle left-click: reveal the cell.
        Updates all revealed cells and handles defeat/victory exceptions.
        """
        try:
            revealed = self.board.reveal(r, c)
            for rr, cc in revealed:
                self.renderer.update_cell(rr, cc, self.board.get_cell(rr, cc))
        except DefeatException as e:
            # Reveal all cells and show defeat message
            self._update_all()
            self.renderer.show_message("Defeat", str(e))
        except VictoryException as e:
            # Reveal all cells and show victory message
            self._update_all()
            self.renderer.show_message("Victory", str(e))

    def _on_right(self, r, c):
        """Handle right-click: toggle flag and update the cell visually."""
        self.board.toggle_flag(r, c)
        self.renderer.update_cell(r, c, self.board.get_cell(r, c))

    def _update_all(self):
        """Refresh the display of all cells (after defeat/victory)."""
        for r in range(self.height):
            for c in range(self.width):
                self.renderer.update_cell(r, c, self.board.get_cell(r, c))

    def _restart(self):
        """
        Restart the game via GameController.
        Resets the UI buttons to initial state.
        """
        self.board = self.controller.restart()
        self.height, self.width = self.board.get_board_size()

        # Reset all button visuals
        for r in range(self.height):
            for c in range(self.width):
                b = self.buttons[r][c]
                b.config(text=' ', state='normal', relief='raised')
