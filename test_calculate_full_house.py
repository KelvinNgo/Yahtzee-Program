from unittest import TestCase
from yahtzee import calculate_full_house


class TestCalculateFullHouse(TestCase):

    def test_calculate_full_house_3_in_front_2_in_back(self):
        test_result = [5, 5, 5, 4, 4]
        expected = 25
        actual = calculate_full_house(test_result)
        self.assertEqual(expected, actual)

    def test_calculate_full_house_2_in_front_3_in_back(self):
        test_result = [4, 4, 5, 5, 5]
        expected = 25
        actual = calculate_full_house(test_result)
        self.assertEqual(expected, actual)

    def test_calculate_full_house_spread_out(self):
        test_result = [5, 4, 5, 4, 5]
        expected = 25
        actual = calculate_full_house(test_result)
        self.assertEqual(expected, actual)

    def test_calculate_full_house_not_full_house_two_doubles(self):
        test_result = [3, 3, 2, 2, 1]
        expected = 0
        actual = calculate_full_house(test_result)
        self.assertEqual(expected, actual)

    def test_calculate_full_house_not_full_house_at_all(self):
        test_result = [1, 2, 3, 4, 5]
        expected = 0
        actual = calculate_full_house(test_result)
        self.assertEqual(expected, actual)
