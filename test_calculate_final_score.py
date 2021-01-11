from unittest import TestCase
from yahtzee import calculate_final_score


class TestCalculateFinalScore(TestCase):

    def test_calculate_final_score_all_filled_in(self):
        expected = 300
        test_card = {'Ones': 3, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 18, 'Sum': 63, 'Bonus': 35,
                     '3 of a kind': 17, '4 of a kind': 21, 'Full House': 25, 'Small Straight': 30,
                     'Large Straight': 40, 'Yahtzee': 50, 'Chance': 19}
        actual = calculate_final_score(test_card)

    def test_calculate_final_score_only_sums_and_chance_with_bonus(self):
        expected = 117
        test_card = {'Ones': 3, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 18, 'Sum': 63, 'Bonus': 35,
                     '3 of a kind': 0, '4 of a kind': 0, 'Full House': 0, 'Small Straight': 0,
                     'Large Straight': 0, 'Yahtzee': 0, 'Chance': 19}
        actual = calculate_final_score(test_card)

    def test_calculate_final_score_only_sums_and_chance_without_bonus(self):
        expected = 81
        test_card = {'Ones': 2, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 18, 'Sum': 62, 'Bonus': 0,
                     '3 of a kind': 0, '4 of a kind': 0, 'Full House': 0, 'Small Straight': 0,
                     'Large Straight': 0, 'Yahtzee': 0, 'Chance': 19}
        actual = calculate_final_score(test_card)

    def test_calculate_final_score_only_non_sum_and_chance(self):
        expected = 202
        test_card = {'Ones': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Sum': 0, 'Bonus': 0,
                     '3 of a kind': 17, '4 of a kind': 21, 'Full House': 25, 'Small Straight': 30,
                     'Large Straight': 40, 'Yahtzee': 50, 'Chance': 19}
        actual = calculate_final_score(test_card)
