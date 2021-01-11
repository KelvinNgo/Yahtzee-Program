from unittest import TestCase
from yahtzee import sum_ones_to_sixes


class TestSumOnesToSixes(TestCase):

    def test_sum_ones_to_sixes_ones(self):
        test_result = [1, 1, 1, 1, 1]
        expected = 5
        actual = sum_ones_to_sixes(test_result, "Ones")
        self.assertEqual(expected, actual)

    def test_sum_ones_to_sixes_twos(self):
        test_result = [2, 2, 2, 2, 2]
        expected = 10
        actual = sum_ones_to_sixes(test_result, "Twos")
        self.assertEqual(expected, actual)

    def test_sum_ones_to_sixes_threes(self):
        test_result = [3, 3, 3, 3, 3]
        expected = 15
        actual = sum_ones_to_sixes(test_result, "Threes")
        self.assertEqual(expected, actual)

    def test_sum_ones_to_sixes_fours(self):
        test_result = [4, 4, 4, 4, 4]
        expected = 20
        actual = sum_ones_to_sixes(test_result, "Fours")
        self.assertEqual(expected, actual)

    def test_sum_ones_to_sixes_fives(self):
        test_result = [5, 5, 5, 5, 5]
        expected = 25
        actual = sum_ones_to_sixes(test_result, "Fives")
        self.assertEqual(expected, actual)

    def test_sum_ones_to_sixes_sixes(self):
        test_result = [6, 6, 6, 6, 6]
        expected = 30
        actual = sum_ones_to_sixes(test_result, "Sixes")
        self.assertEqual(expected, actual)

    def test_sum_ones_to_sixes_two_twos_scattered(self):
        test_result = [2, 3, 1, 2, 5]
        expected = 4
        actual = sum_ones_to_sixes(test_result, "Twos")
        self.assertEqual(expected, actual)

    def test_sum_ones_to_sixes_threes_no_threes(self):
        test_result = [1, 2, 4, 5, 6]
        expected = 0
        actual = sum_ones_to_sixes(test_result, "Threes")
        self.assertEqual(expected, actual)
