from unittest import TestCase
from yahtzee import calculate_3_of_a_kind


class TestCalculate3OfAKind(TestCase):

    def test_calculate_3_of_a_kind_all_in_front(self):
        test_result = [3, 3, 3, 4, 5]
        expected = 18
        actual = calculate_3_of_a_kind(test_result)
        self.assertEqual(expected, actual)

    def test_calculate_4_of_a_kind_all_in_back(self):
        test_result = [4, 5, 3, 3, 3]
        expected = 18
        actual = calculate_3_of_a_kind(test_result)
        self.assertEqual(expected, actual)

    def test_calculate_4_of_a_kind_spread_out(self):
        test_result = [3, 4, 3, 5, 3]
        expected = 18
        actual = calculate_3_of_a_kind(test_result)
        self.assertEqual(expected, actual)

    def test_calculate_4_of_a_kind_with_yahtzee(self):
        test_result = [3, 3, 3, 3, 3]
        expected = 15
        actual = calculate_3_of_a_kind(test_result)
        self.assertEqual(expected, actual)

    def test_calculate_4_of_a_kind_not_4_of_a_kind(self):
        test_result = [3, 3, 2, 2, 1]
        expected = 0
        actual = calculate_3_of_a_kind(test_result)
        self.assertEqual(expected, actual)
