import unittest
from core.game_controller import GameController
from core.exceptions import DefeatException, VictoryException

class TestBoard(unittest.TestCase):
    def setUp(self):
        """Create a 5x5 test board with 3 mines for all tests."""
        self.controller = GameController(height=5, width=5, num_mines=3)
        self.board = self.controller.get_board()

    def test_reveal_safe(self):
        """Test revealing safe cells does not trigger defeat."""
        # Reveal a safe starting cell
        revealed = self.board.reveal(0, 0)
        self.assertTrue(len(revealed) >= 1)

        # Revealing another safe cell should not raise DefeatException
        try:
            self.board.reveal(0, 1)
        except DefeatException:
            self.fail('Unexpected DefeatException raised when revealing a safe cell.')

    def test_defeat(self):
        """Test that revealing a mine triggers DefeatException."""
        # Ensure the board is initialized and mines are placed
        self.board.initialize()  

        # Find a cell containing a mine
        mines = [
            (r, c) for r in range(self.board.height)
            for c in range(self.board.width)
            if self.board.get_cell(r, c).is_mine
        ]
        self.assertEqual(len(mines), 3)

        # Revealing a mine should raise DefeatException
        with self.assertRaises(DefeatException):
            self.board.reveal(mines[0][0], mines[0][1])

    def test_victory(self):
        """Test that revealing all safe cells triggers VictoryException."""
        try:
            for r in range(self.board.height):
                for c in range(self.board.width):
                    cell = self.board.get_cell(r, c)
                    if not cell.is_mine and not cell.revealed:
                        self.board.reveal(r, c)
        except VictoryException:
            # Expected behavior: all safe cells revealed triggers victory
            pass

        # Verify all safe cells are indeed revealed
        safe_left = sum(
            1 for r in range(self.board.height)
            for c in range(self.board.width)
            if not self.board.get_cell(r, c).revealed and not self.board.get_cell(r, c).is_mine
        )
        self.assertEqual(safe_left, 0)

    def test_restart(self):
        """Verify that restart via GameController resets the board cleanly."""
        self.controller.restart()
        board = self.controller.get_board()

        # All cells should be unrevealed after restart
        unrevealed = sum(
            1 for r in range(board.height)
            for c in range(board.width)
            if not board.get_cell(r, c).revealed
        )
        self.assertEqual(unrevealed, board.height * board.width)


if __name__ == '__main__':
    unittest.main()
