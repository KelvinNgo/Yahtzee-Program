from unittest import TestCase
from yahtzee import check_for_bonus


class TestCheckForBonus(TestCase):

    def test_check_for_bonus_sum_63(self):
        expected = {'Ones': 3, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 18, 'Sum': 63, 'Bonus': 35,
                    '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1,
                    'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1}
        test_card = {'Ones': 3, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 18,
                     '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1,
                     'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1}
        actual = check_for_bonus(test_card)
        self.assertEquals(expected, actual)

    def test_check_for_bonus_sum_greater_than_63(self):
        expected = {'Ones': 4, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 18, 'Sum': 64, 'Bonus': 35,
                    '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1,
                    'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1}
        test_card = {'Ones': 4, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 18,
                     '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1,
                     'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1}
        actual = check_for_bonus(test_card)
        self.assertEquals(expected, actual)

    def test_check_for_bonus_sum_62(self):
        expected = {'Ones': 2, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 18, 'Sum': 62, 'Bonus': 0,
                    '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1,
                    'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1}
        test_card = {'Ones': 2, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 18,
                     '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1,
                     'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1}
        actual = check_for_bonus(test_card)
        self.assertEquals(expected, actual)

    def test_check_for_bonus_too_low(self):
        expected = {'Ones': 1, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 6, 'Sum': 49, 'Bonus': 0,
                    '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1,
                    'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1}
        test_card = {'Ones': 1, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 6,
                     '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1,
                     'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1}
        actual = check_for_bonus(test_card)
        self.assertEquals(expected, actual)
