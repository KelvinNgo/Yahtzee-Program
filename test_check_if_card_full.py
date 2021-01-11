from unittest import TestCase
from yahtzee import check_if_card_full


class TestCheckIfCardFull(TestCase):

    def test_check_if_card_full_false(self):
        test_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = "Continue"
        actual = check_if_card_full(test_card)
        self.assertEqual(expected, actual)

    def test_check_if_card_full_true(self):
        test_card = {'Ones': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 6, '3 of a kind': 0,
                     '4 of a kind': 0, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0,
                     'Chance': 0, 'Sum': 21, 'Bonus': 0}
        expected = "Complete"
        actual = check_if_card_full(test_card)
        self.assertEqual(expected, actual)
