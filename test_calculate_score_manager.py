from unittest import TestCase
from yahtzee import calculate_score_manager


class TestCalculateScoreManager(TestCase):

    def test_calculate_score_manager_sum_ones_to_sixes(self):
        test_result = [2, 2, 2, 3, 4]
        test_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = 6
        actual = calculate_score_manager(test_result, test_card, "Twos")
        self.assertEqual(expected, actual)

    def test_calculate_score_manager_calculate_4_of_a_kind(self):
        test_result = [4, 4, 4, 4, 1]
        test_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = 17
        actual = calculate_score_manager(test_result, test_card, "4 of a kind")
        self.assertEqual(expected, actual)

    def test_calculate_score_manager_calculate_3_of_a_kind(self):
        test_result = [3, 3, 3, 2, 1]
        test_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = 12
        actual = calculate_score_manager(test_result, test_card, "3 of a kind")
        self.assertEqual(expected, actual)

    def test_calculate_score_manager_calculate_full_house(self):
        test_result = [3, 3, 3, 2, 2]
        test_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = 25
        actual = calculate_score_manager(test_result, test_card, "Full House")
        self.assertEqual(expected, actual)

    def test_calculate_score_manager_calculate_large_straight(self):
        test_result = [1, 2, 3, 4 ,5]
        test_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = 40
        actual = calculate_score_manager(test_result, test_card, "Large Straight")
        self.assertEqual(expected, actual)

    def test_calculate_score_manager_calculate_small_straight(self):
        test_result = [1, 2, 3, 4, 6]
        test_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = 30
        actual = calculate_score_manager(test_result, test_card, "Small Straight")
        self.assertEqual(expected, actual)

    def test_calculate_score_manager_calculate_yahtzee(self):
        test_result = [6, 6, 6, 6, 6]
        test_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = 50
        actual = calculate_score_manager(test_result, test_card, "Yahtzee")
        self.assertEqual(expected, actual)

    def test_calculate_score_manager_chance(self):
        test_result = [2, 2, 4, 4, 1]
        test_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1,
                     '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                     'Chance': -1}
        expected = 13
        actual = calculate_score_manager(test_result, test_card, "Chance")
        self.assertEqual(expected, actual)
