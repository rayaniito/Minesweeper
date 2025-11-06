import tkinter as tk
from core.game_controller import GameController
from ui.gui_tkinter import MinesweeperUI
from tkinter import messagebox

def main():
    """Configuration window for the game, then launches Minesweeper UI."""
    
    # Create the configuration window
    config = tk.Tk()
    config.title("Minesweeper settings")

    # Labels and entry fields for board height
    tk.Label(config, text="Height :").grid(row=0, column=0, padx=5, pady=5)
    entry_height = tk.Entry(config)
    entry_height.insert(0, "9")  # default value
    entry_height.grid(row=0, column=1)

    # Labels and entry fields for board width
    tk.Label(config, text="Width :").grid(row=1, column=0, padx=5, pady=5)
    entry_width = tk.Entry(config)
    entry_width.insert(0, "9")  # default value
    entry_width.grid(row=1, column=1)

    # Labels and entry fields for number of bombs
    tk.Label(config, text="Bombs :").grid(row=2, column=0, padx=5, pady=5)
    entry_mines = tk.Entry(config)
    entry_mines.insert(0, "10")  # default value
    entry_mines.grid(row=2, column=1)

    def start_game():
        """
        Read configuration values, validate them, create a GameController,
        and launch the main Minesweeper UI.
        """
        try:
            height = int(entry_height.get())
            width = int(entry_width.get())
            mines = int(entry_mines.get())

            # Validate mine count
            if mines >= height * width:
                messagebox.showerror("Error", "Too many bombs for this size!")
                return

            # Close the configuration window
            config.destroy()

            # Create GameController and inject it into the UI
            controller = GameController(height, width, mines)
            app = MinesweeperUI(controller)
            app.mainloop()

        except ValueError:
            # Handle non-integer inputs
            messagebox.showerror("Error", "Please enter valid numbers.")

    # Launch button
    tk.Button(config, text="Launch the game", command=start_game).grid(
        row=3, column=0, columnspan=2, pady=10
    )

    config.mainloop()


if __name__ == '__main__':
    main()
