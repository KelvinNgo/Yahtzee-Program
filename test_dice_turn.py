from unittest import TestCase
from unittest.mock import patch
from yahtzee import dice_turn


class TestDiceTurn(TestCase):

    @patch("random.randint", side_effect=[5, 4, 3, 5, 1])
    @patch("builtins.input", side_effect=["", ""])
    def test_dice_turn_re_roll_all(self, mock_input, mock_randint):
        expected = [5, 4, 3, 5, 1]
        actual = dice_turn([5, 5, 3, 3, 3])
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[1, 2, 3, 4])
    @patch("builtins.input", side_effect=["6", ""])
    def test_dice_manager_roll_keep_single_6_and_roll(self, mock_input, mock_randint):
        expected = [1, 2, 3, 4, 6]
        actual = dice_turn([6, 5, 3, 3, 2])
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[1, 2, 3, 4, 5])
    @patch("builtins.input", side_effect=["6", "6"])
    def test_dice_manager_roll_keep_single_6_and_remove_single_6(self, mock_input, mock_randint):
        expected = [1, 2, 3, 4, 5]
        actual = dice_turn([6, 5, 3, 3, 2])
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[])
    @patch("builtins.input", side_effect=["6 5 3 3 2", ""])
    def test_dice_manager_roll_keep_all(self, mock_input, mock_randint):
        expected = [6, 5, 3, 3, 2]
        actual = dice_turn([6, 5, 3, 3, 2])
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[5, 3, 5, 3, 3])
    @patch("builtins.input", side_effect=["6 5 3 3 2", "6 5 3 3 2"])
    def test_dice_manager_roll_keep_all_remove_all(self, mock_input, mock_randint):
        expected = [5, 3, 5, 3, 3]
        actual = dice_turn([6, 5, 3, 3, 2])
        self.assertEqual(expected, actual)
