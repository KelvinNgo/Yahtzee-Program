from unittest import TestCase
from yahtzee import determine_large_straight


class TestDetermineLargeStraight(TestCase):

    def test_determine_small_straight_1_to_5(self):
        test_result = [1, 2, 3, 4, 5]
        expected = 40
        actual = determine_large_straight(test_result)
        self.assertEqual(expected, actual)

    def test_determine_large_straight_2_to_6(self):
        test_result = [2, 3, 4, 5, 6]
        expected = 40
        actual = determine_large_straight(test_result)
        self.assertEqual(expected, actual)

    def test_determine_large_straight_unordered(self):
        test_result = [3, 4, 5, 2, 1]
        expected = 40
        actual = determine_large_straight(test_result)
        self.assertEqual(expected, actual)

    def test_determine_small_straight_not_small_straight(self):
        test_result = [1, 2, 2, 4, 5]
        expected = 0
        actual = determine_large_straight(test_result)
        self.assertEqual(expected, actual)
