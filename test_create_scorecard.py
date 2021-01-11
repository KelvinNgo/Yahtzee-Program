from unittest import TestCase
from yahtzee import create_scorecard


class TestCreateScorecard(TestCase):

    def test_create_scorecard(self):
        expected = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1,
                    '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1,
                    'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1}
        actual = create_scorecard()
        self.assertEquals(expected, actual)
