from unittest import TestCase
from unittest.mock import patch
from yahtzee import keep_die


class TestKeepDie(TestCase):

    @patch("builtins.input", side_effect=["6 3 4 5 1"])
    def test_keep_die_5(self, mock_input):
        rolled_die = [6, 3, 4, 5, 1]
        expected = [6, 3, 4, 5, 1]
        actual = keep_die(rolled_die)
        self.assertEquals(expected, actual)

    @patch("builtins.input", side_effect=["6 3 4 5"])
    def test_keep_die_4(self, mock_input):
        rolled_die = [6, 3, 4, 5, 1]
        expected = [6, 3, 4, 5]
        actual = keep_die(rolled_die)
        self.assertEquals(expected, actual)

    @patch("builtins.input", side_effect=["6 3 5"])
    def test_keep_die_3(self, mock_input):
        rolled_die = [6, 3, 4, 5, 1]
        expected = [6, 3, 5]
        actual = keep_die(rolled_die)
        self.assertEquals(expected, actual)

    @patch("builtins.input", side_effect=["6 3"])
    def test_keep_die_2(self, mock_input):
        rolled_die = [6, 3, 4, 5, 1]
        expected = [6, 3]
        actual = keep_die(rolled_die)
        self.assertEquals(expected, actual)

    @patch("builtins.input", side_effect=["6"])
    def test_keep_die_1(self, mock_input):
        rolled_die = [6, 3, 4, 5, 1]
        expected = [6]
        actual = keep_die(rolled_die)
        self.assertEquals(expected, actual)

    @patch("builtins.input", side_effect=[""])
    def test_keep_die_0(self, mock_input):
        rolled_die = [6, 3, 4, 5, 1]
        expected = []
        actual = keep_die(rolled_die)
        self.assertEquals(expected, actual)
