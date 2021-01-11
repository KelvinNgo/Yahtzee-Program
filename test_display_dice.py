from unittest import TestCase
from unittest.mock import patch
import io
from yahtzee import RED_TEXT
from yahtzee import END_COLOUR
import random


def display_dice(roll_func):
    def dice_wrapper(stack_of_dice):
        print(f"You {RED_TEXT()}VIOLENTLY{END_COLOUR()} shake your fist and release it!\n")

        roll = roll_func(stack_of_dice)
        for dice in range(0, len(roll)):
            print(f"+---+\n"
                  f"| {roll[dice]} |\n"
                  f"+---+")

        print(f"What a {RED_TEXT()}maneuver{END_COLOUR()}! Nice rolls.\n")
        return roll
    return dice_wrapper


class TestDisplayDice(TestCase):

    @patch("random.randint", side_effect=[5, 4, 3, 5, 1])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_dice_with_roll_die(self, mock_stdout, mock_randint):

        @display_dice
        def roll_die(amount_of_dice: int) -> list:
            dice = []

            for die in range(0, amount_of_dice):
                dice.append(random.randint(1, 6))

            return dice
        expected = roll_die(5)
        actual_return = [5, 4, 3, 5, 1]
        actual_print = f"You {RED_TEXT()}VIOLENTLY{END_COLOUR()} shake your fist and release it!\n\n" \
                       "+---+\n" \
                       "| 5 |\n" \
                       "+---+\n" \
                       "+---+\n" \
                       "| 4 |\n" \
                       "+---+\n" \
                       "+---+\n" \
                       "| 3 |\n" \
                       "+---+\n" \
                       "+---+\n" \
                       "| 5 |\n" \
                       "+---+\n" \
                       "+---+\n" \
                       "| 1 |\n" \
                       "+---+\n" \
                       f"What a {RED_TEXT()}maneuver{END_COLOUR()}! Nice rolls.\n\n"
        self.assertEqual(mock_stdout.getvalue(), actual_print)
        self.assertEqual(expected, actual_return)
