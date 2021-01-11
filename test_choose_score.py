from unittest import TestCase
from unittest.mock import patch
from yahtzee import choose_score


class TestChooseScore(TestCase):

    @patch("builtins.input", side_effect=["1"])
    def test_choose_score_first_option(self, mock_input):
        test_dict = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = "Ones"
        actual = choose_score(test_dict)
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["13"])
    def test_choose_score_last_option(self, mock_input):
        test_dict = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = "Chance"
        actual = choose_score(test_dict)
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["9"])
    def test_choose_score_full_house_option(self, mock_input):
        test_dict = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = "Full House"
        actual = choose_score(test_dict)
        self.assertEqual(expected, actual)
