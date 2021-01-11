from unittest import TestCase
from yahtzee import determine_small_straight


class TestDetermineSmallStraight(TestCase):

    def test_determine_small_straight_1_to_4(self):
        test_result = [1, 2, 3, 4, 1]
        expected = 30
        actual = determine_small_straight(test_result)
        self.assertEqual(expected, actual)

    def test_determine_small_straight_2_to_5(self):
        test_result = [2, 3, 4, 5, 2]
        expected = 30
        actual = determine_small_straight(test_result)
        self.assertEqual(expected, actual)

    def test_determine_small_straight_3_to_6(self):
        test_result = [3, 4, 5, 6, 3]
        expected = 30
        actual = determine_small_straight(test_result)
        self.assertEqual(expected, actual)

    def test_determine_small_straight_with_large_straight(self):
        test_result = [1, 2, 3, 4, 5]
        expected = 30
        actual = determine_small_straight(test_result)
        self.assertEqual(expected, actual)

    def test_determine_small_straight_unordered(self):
        test_result = [1, 4, 3, 6, 2]
        expected = 30
        actual = determine_small_straight(test_result)
        self.assertEqual(expected, actual)

    def test_determine_small_straight_not_small_straight(self):
        test_result = [1, 2, 2, 4, 5]
        expected = 0
        actual = determine_small_straight(test_result)
        self.assertEqual(expected, actual)
