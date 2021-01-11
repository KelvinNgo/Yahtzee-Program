from unittest import TestCase
from yahtzee import calculate_4_of_a_kind


class TestCalculate4OfAKind(TestCase):

    def test_calculate_4_of_a_kind_all_in_front(self):
        test_result = [6, 6, 6, 6, 5]
        expected = 29
        actual = calculate_4_of_a_kind(test_result)
        self.assertEqual(expected, actual)

    def test_calculate_4_of_a_kind_all_in_back(self):
        test_result = [5, 6, 6, 6, 6]
        expected = 29
        actual = calculate_4_of_a_kind(test_result)
        self.assertEqual(expected, actual)

    def test_calculate_4_of_a_kind_spread_out(self):
        test_result = [6, 5, 6, 6, 6]
        expected = 29
        actual = calculate_4_of_a_kind(test_result)
        self.assertEqual(expected, actual)

    def test_calculate_4_of_a_kind_with_yahtzee(self):
        test_result = [6, 6, 6, 6, 6]
        expected = 30
        actual = calculate_4_of_a_kind(test_result)
        self.assertEqual(expected, actual)

    def test_calculate_4_of_a_kind_not_4_of_a_kind(self):
        test_result = [5, 5, 6, 6, 6]
        expected = 0
        actual = calculate_4_of_a_kind(test_result)
        self.assertEqual(expected, actual)
