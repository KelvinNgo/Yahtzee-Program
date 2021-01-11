from unittest import TestCase
from unittest.mock import patch
from yahtzee import return_die_to_board


class TestReturnDiceToBoard(TestCase):

    @patch("builtins.input", side_effect=["6"])
    def test_return_one_die_to_board(self, mock_input):
        rolled_die = [6, 3, 4, 5, 1]
        expected = [3, 4, 5, 1]
        actual = return_die_to_board(rolled_die)
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["6 3"])
    def test_return_two_dice_to_board(self, mock_input):
        rolled_die = [6, 3, 4, 5, 1]
        expected = [4, 5, 1]
        actual = return_die_to_board(rolled_die)
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["6 3 4 5 1"])
    def test_return_all_dice_to_board(self, mock_input):
        rolled_die = [6, 3, 4, 5, 1]
        expected = []
        actual = return_die_to_board(rolled_die)
        self.assertEqual(expected, actual)
