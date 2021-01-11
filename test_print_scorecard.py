from unittest import TestCase
from unittest.mock import patch
import io
from yahtzee import print_scorecard
from yahtzee import GREEN_TEXT
from yahtzee import RED_TEXT
from yahtzee import END_COLOUR


class TestPrintScorecard(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_scorecard_empty(self, mock_stdout):
        test_score_card = {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1,
                           '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1,
                           'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1}
        print_scorecard(test_score_card)
        expected = f"This is your current score card\n\n"\
                   f"{GREEN_TEXT()}Ones{END_COLOUR()}\n"\
                   f"{GREEN_TEXT()}Twos{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Threes{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Fours{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Fives{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Sixes{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}3 of a kind{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}4 of a kind{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Full House{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Small Straight{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Large Straight{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Yahtzee{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Chance{END_COLOUR()}\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_scorecard_filled_values(self, mock_stdout):
        test_score_card = {'Ones': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 6,
                           '3 of a kind': 16, '4 of a kind': 22, 'Full House': 25, 'Small Straight': 30,
                           'Large Straight': 40, 'Yahtzee': 50, 'Chance': 17}
        print_scorecard(test_score_card)
        expected = f"This is your current score card\n\n"\
                   f"{GREEN_TEXT()}Ones{END_COLOUR()} {RED_TEXT()}1{END_COLOUR()}\n"\
                   f"{GREEN_TEXT()}Twos{END_COLOUR()} {RED_TEXT()}2{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Threes{END_COLOUR()} {RED_TEXT()}3{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Fours{END_COLOUR()} {RED_TEXT()}4{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Fives{END_COLOUR()} {RED_TEXT()}5{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Sixes{END_COLOUR()} {RED_TEXT()}6{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}3 of a kind{END_COLOUR()} {RED_TEXT()}16{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}4 of a kind{END_COLOUR()} {RED_TEXT()}22{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Full House{END_COLOUR()} {RED_TEXT()}25{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Small Straight{END_COLOUR()} {RED_TEXT()}30{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Large Straight{END_COLOUR()} {RED_TEXT()}40{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Yahtzee{END_COLOUR()} {RED_TEXT()}50{END_COLOUR()}\n" \
                   f"{GREEN_TEXT()}Chance{END_COLOUR()} {RED_TEXT()}17{END_COLOUR()}\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
