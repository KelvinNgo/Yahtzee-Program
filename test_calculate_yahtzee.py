from unittest import TestCase
from yahtzee import calculate_yahtzee


class TestCalculateYahtzee(TestCase):

    def test_calculate_yahtzee_ones(self):
        test_result = [1, 1, 1, 1, 1]
        test_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = 50
        actual = calculate_yahtzee(test_result, test_card)
        self.assertEqual(expected, actual)

    def test_calculate_yahtzee_twos(self):
        test_result = [2, 2, 2, 2, 2]
        test_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = 50
        actual = calculate_yahtzee(test_result, test_card)
        self.assertEqual(expected, actual)

    def test_calculate_yahtzee_sixes(self):
        test_result = [6, 6, 6, 6, 6]
        test_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = 50
        actual = calculate_yahtzee(test_result, test_card)
        self.assertEqual(expected, actual)

    def test_calculate_yahtzee_second_yahtzee(self):
        test_result = [2, 2, 2, 2, 2]
        test_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': 50,
                     'Chance': -1}
        expected = 100
        actual = calculate_yahtzee(test_result, test_card)
        self.assertEqual(expected, actual)

    def test_calculate_yahtzee_third_yahtzee(self):
        test_result = [2, 2, 2, 2, 2]
        test_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': 100,
                     'Chance': -1}
        expected = 100
        actual = calculate_yahtzee(test_result, test_card)
        self.assertEqual(expected, actual)

    def test_calculate_yahtzee_not_yahtzee(self):
        test_result = [1, 2, 2, 2, 2]
        test_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = 0
        actual = calculate_yahtzee(test_result, test_card)
        self.assertEqual(expected, actual)
