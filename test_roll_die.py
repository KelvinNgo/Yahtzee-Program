from unittest import TestCase
from unittest.mock import patch
from yahtzee import roll_die


class TestRollDie(TestCase):

    @patch("random.randint", side_effect=[5, 4, 3, 5, 1])
    def test_roll_die_5_rolls(self, mock_randint):
        actual = roll_die(5)
        self.assertEqual(actual, [5, 4, 3, 5, 1])

    @patch("random.randint", side_effect=[5, 4, 3, 5])
    def test_roll_die_4_rolls(self, mock_randint):
        actual = roll_die(4)
        self.assertEqual(actual, [5, 4, 3, 5])

    @patch("random.randint", side_effect=[5, 4, 3])
    def test_roll_die_3_rolls(self, mock_randint):
        actual = roll_die(3)
        self.assertEqual(actual, [5, 4, 3])

    @patch("random.randint", side_effect=[5, 4])
    def test_roll_die_2_rolls(self, mock_randint):
        actual = roll_die(2)
        self.assertEqual(actual, [5, 4])

    @patch("random.randint", side_effect=[5])
    def test_roll_die_1_rolls(self, mock_randint):
        actual = roll_die(1)
        self.assertEqual(actual, [5])
