from unittest import TestCase
from unittest.mock import patch
import io
from yahtzee import determine_winner
from yahtzee import RED_TEXT
from yahtzee import YELLOW_TEXT
from yahtzee import END_COLOUR


class TestDetermineWinner(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_determine_winner_player_one_wins(self, mock_stdout):
        final_scores = {"Player One Total": 9001, "Player Two Total": 9000}
        determine_winner(final_scores)
        expected = f"Here are the {YELLOW_TEXT()}FINAL{END_COLOUR()} results!\n\n" \
                   f"Player One Total: {YELLOW_TEXT()}9001{END_COLOUR()}\n" \
                   f"Player Two Total: {YELLOW_TEXT()}9000{END_COLOUR()}\n" \
                   f"{RED_TEXT()}AS GOD AS MY WITNESS, PLAYER TWO IS BROKEN IN HALF!!!!{END_COLOUR()}\n\n" \
                   "Player One Wins!\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_determine_winner_player_two_wins(self, mock_stdout):
        final_scores = {"Player One Total": 1, "Player Two Total": 1000000}
        determine_winner(final_scores)
        expected = f"Here are the {YELLOW_TEXT()}FINAL{END_COLOUR()} results!\n\n" \
                   f"Player One Total: {YELLOW_TEXT()}1{END_COLOUR()}\n" \
                   f"Player Two Total: {YELLOW_TEXT()}1000000{END_COLOUR()}\n" \
                   f"{RED_TEXT()}AS GOD AS MY WITNESS, PLAYER ONE IS BROKEN IN HALF!!!!{END_COLOUR()}\n\n" \
                   "Player Two Wins!\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_determine_winner_draw(self, mock_stdout):
        final_scores = {"Player One Total": 123, "Player Two Total": 123}
        determine_winner(final_scores)
        expected = f"Here are the {YELLOW_TEXT()}FINAL{END_COLOUR()} results!\n\n" \
                   f"Player One Total: {YELLOW_TEXT()}123{END_COLOUR()}\n" \
                   f"Player Two Total: {YELLOW_TEXT()}123{END_COLOUR()}\n" \
                   f"{YELLOW_TEXT()}IMPOSSIBLE, IT'S A DRAW!!!!{END_COLOUR()}\n"
        self.assertEqual(expected, mock_stdout.getvalue())
