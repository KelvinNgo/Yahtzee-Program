import random
import re
import doctest

"""
Kelvin Ngo
A01086182
COMP 1510 Set F
Assignment 3!!
"""


def EMPTY_SCORE() -> int:
    return -1


def MAXIMUM_DICE_ROLLS() -> int:
    return 5


def FULL_HOUSE_VALUE() -> int:
    return 25


def SMALL_STRAIGHT_VALUE() -> int:
    return 30


def LARGE_STRAIGHT_VALUE() -> int:
    return 40


def SCORE_OF_ZERO() -> int:
    return 0


def FIRST_YAHTZEE_VALUE() -> int:
    return 50


def SUBSEQUENT_YAHTZEE_VALUE() -> int:
    return 100


def BLUE_TEXT() -> str:
    return "\u001b[34m"


def RED_TEXT() -> str:
    return "\u001b[31m"


def GREEN_TEXT() -> str:
    return "\u001b[32m"


def YELLOW_TEXT() -> str:
    return "\u001b[33m"


def MAGENTA_TEXT() -> str:
    return "\u001b[35m"


def CYAN_TEXT() -> str:
    return "\u001b[36m"


def END_COLOUR() -> str:
    return "\u001b[0m"


def FIRST_YAHTZEE_CONGRATULATIONS() -> None:
    print(f"{YELLOW_TEXT()}CONGLATURATION{END_COLOUR()} !!!\n"
          f"YOU GOT YOUR FIRST {YELLOW_TEXT()}YAHTZEE{END_COLOUR()}\n")


def SUBSEQUENT_YAHTZEE_CONGRATULATIONS() -> None:
    print(f"Okay settle down now, that's too many {YELLOW_TEXT()}YAHTZEE{END_COLOUR()}s\n")


def create_scorecard() -> dict:
    """Create a dictionary representing a Yahtzee scorecard.

    :postcondition: Create a dictionary with keys representing points that the user can score in Yahtzee.
    :return: A dictionary representing a Yahtzee scorecard.

    >>> create_scorecard()
    {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1, '\
4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1}
    """
    score_card = {"Ones": EMPTY_SCORE(), "Twos": EMPTY_SCORE(), "Threes": EMPTY_SCORE(), "Fours": EMPTY_SCORE(),
                  "Fives": EMPTY_SCORE(), "Sixes": EMPTY_SCORE(), "3 of a kind": EMPTY_SCORE(),
                  "4 of a kind": EMPTY_SCORE(), "Full House": EMPTY_SCORE(), "Small Straight": EMPTY_SCORE(),
                  "Large Straight": EMPTY_SCORE(), "Yahtzee": EMPTY_SCORE(), "Chance": EMPTY_SCORE()}
    return score_card


def check_for_bonus(score_card: dict) -> dict:
    """Check upper section (Ones to Sixes) and give 35 point bonus if sum is equal or greater than 63.

    :param score_card: A dictionary representing a Yahtzee scorecard.
    :precondition: score_card is a dict with the upper keys "Ones" to "Sixes" filled in with values.
    :postcondition: Calculate if the sum of "Ones" to "Sixes" is 63 or greater. If it is, fill in the bonus with
    35 points. Otherwise, fill in the bonus with 0 points.
    :return: An updated dict representing a Yahtzee scorecard with the bonus filled in.

    >>> test_card = create_scorecard()
    >>> test_card["Ones"] = 3
    >>> test_card["Twos"] = 6
    >>> test_card["Threes"] = 9
    >>> test_card["Fours"] = 12
    >>> test_card["Fives"] = 15
    >>> test_card["Sixes"] = 18
    >>> test_card["3 of a kind"] = -1
    >>> test_card["4 of a kind"] = -1
    >>> test_card["Full House"] = -1
    >>> test_card["Small Straight"] = -1
    >>> test_card["Large Straight"] = -1
    >>> test_card["Yahtzee"] = -1
    >>> test_card["Chance"] = -1
    >>> check_for_bonus(test_card)
    {'Ones': 3, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 18, '3 of a kind': -1, '4 of a kind': -1, '\
Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1, 'Sum': 63, 'Bonus': 35}

    >>> test_card = create_scorecard()
    >>> test_card["Ones"] = 2
    >>> test_card["Twos"] = 6
    >>> test_card["Threes"] = 9
    >>> test_card["Fours"] = 12
    >>> test_card["Fives"] = 15
    >>> test_card["Sixes"] = 18
    >>> test_card["3 of a kind"] = -1
    >>> test_card["4 of a kind"] = -1
    >>> test_card["Full House"] = -1
    >>> test_card["Small Straight"] = -1
    >>> test_card["Large Straight"] = -1
    >>> test_card["Yahtzee"] = -1
    >>> test_card["Chance"] = -1
    >>> check_for_bonus(test_card)
    {'Ones': 2, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 18, '3 of a kind': -1, '4 of a kind': -1, '\
Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1, 'Sum': 62, 'Bonus': 0}
    """
    upper_list = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]
    upper_total = {key: score for key, score in score_card.items() if key in upper_list}

    if sum(upper_total.values()) >= 63:
        score_card["Sum"] = sum(upper_total.values())
        score_card["Bonus"] = 35

    else:
        score_card["Sum"] = sum(upper_total.values())
        score_card["Bonus"] = 0

    return score_card


def calculate_final_score(score_card: dict) -> int:
    """Calculate the user's final score.

    :param score_card: A dictionary representing a Yahtzee score card.
    :precondition: score_card is a dictionary with all the necessary values filled in.
    :postcondition: Sum all the ints within score_card and return the final result as an int
    :return: An int representing the final result of the score card summed up.

    >>> test_card = {'Ones': 2, 'Twos': 6, 'Threes': 9, 'Fours': 12, 'Fives': 15, 'Sixes': 18, 'Sum': 62,
    ... 'Bonus': 0, '3 of a kind': 20, '4 of a kind': 17, 'Full House': 25, 'Small Straight': 0,
    ... 'Large Straight': 40, 'Yahtzee': 0, 'Chance': 18}
    >>> calculate_final_score(test_card)
    244

    """
    return sum(score_card.values())


def print_scorecard(score_card: dict) -> None:
    """Display current state of scorecard to user.

    :postcondition: Print out the current state of the scorecard to the user.

    >>> test_card = create_scorecard()
    >>> print_scorecard(test_card)
    This is your current score card
    <BLANKLINE>
    \u001b[32mOnes\u001b[0m
    \u001b[32mTwos\u001b[0m
    \u001b[32mThrees\u001b[0m
    \u001b[32mFours\u001b[0m
    \u001b[32mFives\u001b[0m
    \u001b[32mSixes\u001b[0m
    \u001b[32m3 of a kind\u001b[0m
    \u001b[32m4 of a kind\u001b[0m
    \u001b[32mFull House\u001b[0m
    \u001b[32mSmall Straight\u001b[0m
    \u001b[32mLarge Straight\u001b[0m
    \u001b[32mYahtzee\u001b[0m
    \u001b[32mChance\u001b[0m
    """
    print("This is your current score card\n")
    for score_key, score_value in score_card.items():
        if score_value == -1:
            print(f"{GREEN_TEXT()}{score_key}{END_COLOUR()}")
        else:
            print(f"{GREEN_TEXT()}{score_key}{END_COLOUR()} {RED_TEXT()}{score_value}{END_COLOUR()}")


def display_dice(roll_func):
    """Display dice user has rolled.

    :param roll_func: A dice rolling function
    :precondition: roll_func is a function that randomly generates 5 numbers and returns it as a list.
    :postcondition: Will display the list in a neat format.
    :return: The return from roll_func, which will be a list representing 5 rolled dice.
    """
    def dice_wrapper(stack_of_dice: list) -> list:
        print(f"You {RED_TEXT()}VIOLENTLY{END_COLOUR()} shake your fist and release it!\n")

        roll = roll_func(stack_of_dice)
        for dice in range(0, len(roll)):
            print(f"+---+\n"
                  f"| {roll[dice]} |\n"
                  f"+---+")

        print(f"What a {RED_TEXT()}maneuver{END_COLOUR()}! Nice rolls.\n")
        return roll
    return dice_wrapper


@display_dice
def roll_die(amount_of_dice: int) -> list:
    """Roll a given amount of six-sided dice and return the randomly generated results as a list.

    :param amount_of_dice: An int representing the amount of dice to roll
    :precondition: amount_of_die is an int between 1-5 for the purposes of Yahtzee
    :postcondition: Randomly generate an amount of numbers equal to amount_of_die and place into a list.
    :return: A list containing 1-5 randomly generated numbers converted to strings.
    """
    dice = []

    for die in range(0, amount_of_dice):
        dice.append(random.randint(1, 6))

    return dice


def return_die_to_board(dice_in_hand: list) -> list:
    """Select the six-sided dice that the user wishes to keep and remove it/them from a list containing dice.

    :param dice_in_hand: A list containing six-sided dice that the user is keeping in their hand.
    :precondition: rolled_die is a list containing ints representing numbers that the user has rolled.
    :postcondition: The user input which six-sided dice they wish to keep from rolled_dice and they will be placed
    into a list.
    :return: A list of six-sided dice that the user kept.
    """
    choose_to_return = input("Please select the dice you wish to put back on the board from your hand. "
                             "Select the dice by value with spaces separating them.\n\n E.g. '1 2 5 if "
                             "you wish to select 3 dice with values of 1, 2, and 5. Enter anything else if you wish "
                             "to skip.\n\nYOU ONLY GET ONE SHOT AT THIS DON'T MESS UP!!!!!!!: ")

    try:
        dice_to_return = [int(dice_value) for dice_value in choose_to_return.split()]

        for dice in dice_to_return:
            dice_in_hand.remove(dice)

        return dice_in_hand

    except ValueError:
        return dice_in_hand


def keep_die(rolled_dice: list) -> list:
    """Select the six-sided dice that the user wishes to move and place it into a new list.

    :param rolled_dice: A list containing six-sided dice that the user has rolled.
    :precondition: rolled_die is a list containing ints representing numbers that the user has rolled.
    :postcondition: The user input which six-sided dice they wish to keep from rolled_dice and they will be placed
    into a list.
    :return: A list of six-sided dice that the user kept.
    """
    choose_to_keep = input(f"Please select the dice you wish put in your hand and keep. "
                           "Select the dice by value with spaces separating them.\n\n E.g. '1 2 5 if "
                           "you wish to select 3 dice with values of 1, 2, and 5. Enter anything else if you wish "
                           "to skip.\n\nYOU ONLY GET ONE SHOT AT THIS DON'T MESS UP!!!!!!!: ")
    try:
        dice_to_keep = [int(dice_value) for dice_value in choose_to_keep.split()]

        for dice in dice_to_keep:
            rolled_dice.remove(dice)

        return dice_to_keep

    except ValueError:
        return rolled_dice


def dice_turn(all_dice: list) -> list:
    """Simulate a single dice rolling turn of Yahtzee.

    :param all_dice: A list containing integers representing dice player currently has.
    :precondition: all_dice contains exactly 5 integers representing dice.
    :postcondition: Will take the user through a round of dice rolling. The user can choose to keep dice,
    remove dice that is being kept, and roll an amount of dice equal to the maximum(5) subtracted by the amount
    of dice being kept.
    :return: A list containing 5 randomly generated numbers representing rolled dice.
    """
    print(f"You can choose to {CYAN_TEXT()}KEEP{END_COLOUR()} dice in your hand and not re-roll them.\n")

    dice_in_hand = keep_die(all_dice)

    print(f"\nThis is what you have in your hand {dice_in_hand}. You can choose to "
          f"{CYAN_TEXT()}PUT IT BACK{END_COLOUR()} on the board to be re-rolled.\n")

    dice_in_hand = return_die_to_board(dice_in_hand)

    dice_on_board = roll_die(MAXIMUM_DICE_ROLLS() - len(dice_in_hand))
    dice_on_board += dice_in_hand

    print(f"This is what you currently have right now {dice_on_board}\n")

    return dice_on_board


def dice_manager() -> list:
    """Manage the six-sided dice rolls of the user during a round of Yahtzee.

    :postcondition: The function will simulate a round of six-sided dice rolls for a user. The user will be allowed to
    roll 3 times. Before the 2nd and 3rd rolls, the user can choose to keep dice or put them back to be rolled.
    :return: A list containing the final results of the dice rolled by user.
    """
    roll = roll_die(MAXIMUM_DICE_ROLLS())

    for rolls in range(2):
        stop_rolling_check = input("Input 'score' if you wish to stop rolling and update your score card. "
                                   "Enter anything else if you wish to keep rolling. Remember you can only roll "
                                   "3 times total!!!!: ")

        if stop_rolling_check != "score":
            roll = dice_turn(roll)

        else:
            return roll

    return roll


def choose_score(score_card: dict) -> str:
    """Retrieve input from the user to choose a score to update.

    :param score_card: A dictionary representing a Yahtzee scorecard.
    :precondition: score_card is a dictionary representing a Yahtzee scorecard.
    :postcondition: Generates a list of keys from score_card then checks if user input is in the list. If it is,
    the key will be returned as a string. Otherwise, the user will try again until successful.
    :return: A string corresponding to a key within the Yahtzee scorecard dictionary.
    """
    valid_scores = [score for score in score_card.keys()]

    for selection, score in enumerate(valid_scores, 1):
        print(f"{selection}: {score}")

    while True:
        try:
            select_score = int(input("Please choose the score you wish to update by the number associated "
                                     "with it in the menu: "))

            if select_score in range(1, len(valid_scores) + 1):
                return valid_scores[select_score - 1]

            else:
                print(f"\nNow listen to me {RED_TEXT()}VERY{END_COLOUR()} carefully, enter a number "
                      f"that is in the menu.")

        except ValueError:
            print(f"\nNow listen to me {RED_TEXT()}VERY{END_COLOUR()} carefully, enter a number "
                  f"that is in the menu.")


def sum_ones_to_sixes(dice_result: list, score_card_location: str) -> int:
    """Calculate the sum of chosen dice face.

    :param dice_result: A list representing 5 dice the user has rolled.
    :param score_card_location: A string representing the score user wishes to update.
    :precondition: dice_result must be a list containing 5 integers that represent dice created with randomly
    generated numbers. score_card_location must a string that exists within a Yahtzee scorecard dictionary.
    :postcondition: sum_ones_to_sixes will count how many dice match score_card_location and multiply that count
    by the face value of the dice.
    :return: An int representing the score the user has earned for a given score location.

    >>> test_result = [2, 2, 2, 4, 5]
    >>> sum_ones_to_sixes(test_result, "Twos")
    6

    >>> test_result = [1, 3, 4, 5, 6]
    >>> sum_ones_to_sixes(test_result, "Twos")
    0
    """
    one_to_sixes_tuple = ("Ones", "Twos", "Threes", "Fours", "Fives", "Sixes")
    ones_to_sixes_counter = one_to_sixes_tuple.index(score_card_location) + 1
    return dice_result.count(ones_to_sixes_counter) * ones_to_sixes_counter


def calculate_4_of_a_kind(dice_result: list) -> int:
    """Determine if dice counts as a 4 of a kind and return the score.

    :param dice_result: A list representing 5 dice the user has rolled.
    :precondition: dice_result must be a list containing 5 integers that represent dice created with randomly
    generated numbers.
    :postcondition: Use regex to determine if the dice result in a 3 of a kind. If so, return a score equal to the
    sum of the dice. Otherwise, return a score of 0.
    :return: An int representing the score earned by the dice.

    >>> test_result = [5, 5, 4, 5, 5]
    >>> calculate_4_of_a_kind(test_result)
    24

    >>> test_result = [1, 2, 3, 4 ,5]
    >>> calculate_4_of_a_kind(test_result)
    0
    """
    dice_regex = ""

    for dice in sorted(dice_result):
        dice_regex += str(dice)

    seek_four_of_a_kind = re.compile(r"([1-6])\1{3}")
    four_of_a_kind_result = seek_four_of_a_kind.search(dice_regex)

    if four_of_a_kind_result:
        return sum(dice_result)

    else:
        return SCORE_OF_ZERO()


def calculate_3_of_a_kind(dice_result: list) -> int:
    """Determine if dice counts as a 4 of a kind and return the score.

    :param dice_result: A list representing 5 dice the user has rolled.
    :precondition: dice_result must be a list containing 5 integers that represent dice created with randomly
    generated numbers.
    :postcondition: Use regex to determine if the dice result in a 3 of a kind. If so, return a score equal to the
    sum of the dice. Otherwise, return a score of 0.
    :return: An int representing the score earned by the dice.

    >>> test_result = [1, 1, 2, 2, 1]
    >>> calculate_3_of_a_kind(test_result)
    7

    >>> test_result = [1, 2, 3, 4 ,5]
    >>> calculate_3_of_a_kind(test_result)
    0
    """
    dice_regex = ""

    for dice in sorted(dice_result):
        dice_regex += str(dice)

    seek_three_of_a_kind = re.compile(r"([1-6])\1{2}")
    three_of_a_kind_result = seek_three_of_a_kind.search(dice_regex)

    if three_of_a_kind_result:
        return sum(dice_result)

    else:
        return SCORE_OF_ZERO()


def calculate_full_house(dice_result: list) -> int:
    """Determine if dice counts as a 4 of a kind and return the score.

    :param dice_result: A list representing 5 dice the user has rolled.
    :precondition: dice_result must be a list containing 5 integers that represent dice created with randomly
    generated numbers.
    :postcondition: Use regex to determine if the dice result in a 3 of a kind. If so, return a score equal to the
    sum of the dice. Otherwise, return a score of 0.
    :return: An int representing the score earned by the dice.

    >>> test_result = [1, 1, 2, 2, 1]
    >>> calculate_full_house(test_result)
    25

    >>> test_result = [1, 2, 3, 4 ,5]
    >>> calculate_full_house(test_result)
    0
    """
    dice_regex = ""

    for dice in sorted(dice_result):
        dice_regex += str(dice)

    seek_three_of_a_kind = re.compile(r"([1-6])\1{2}")
    seek_doubles = re.compile(r"([1-6])\1")

    three_of_a_kind_result = seek_three_of_a_kind.search(dice_regex)
    check_for_two_doubles = seek_doubles.findall(dice_regex)

    if three_of_a_kind_result and len(check_for_two_doubles) == 2:
        return FULL_HOUSE_VALUE()

    else:
        return SCORE_OF_ZERO()


def determine_small_straight(dice_result: list) -> int:
    """Determine if rolled dice results in a small straight.

    :param dice_result: A list representing 5 dice the user has rolled.
    :precondition: dice_result must be a list containing 5 integers that represent dice created with randomly
    generated numbers.
    :postcondition: Check if the dice results in a small straight. If so, return a score of 30. Otherwise, return
    a score of 0.
    :return: An int representing the score earned by the dice.

    >>> test_result = [1, 2, 3, 4, 5]
    >>> determine_small_straight(test_result)
    30

    >>> test_result = [3, 4, 1, 1, 1]
    >>> determine_small_straight(test_result)
    0
    """
    dice_regex = ""

    for dice in set(sorted(dice_result)):
        dice_regex += str(dice)

    seek_small_straight = re.compile(r"1234|2345|3456")

    small_straight_result = seek_small_straight.search(dice_regex)

    if small_straight_result:
        return SMALL_STRAIGHT_VALUE()

    else:
        return SCORE_OF_ZERO()


def determine_large_straight(dice_result: list) -> int:
    """Determine if rolled dice results in a large straight.

    :param dice_result: A list representing 5 dice the user has rolled.
    :precondition: dice_result must be a list containing 5 integers that represent dice created with randomly
    generated numbers.
    :postcondition: Check if the dice results in a large straight. If so, return a score of 40. Otherwise, return
    a score of 0.
    :return: An int representing the score earned by the dice.

    >>> test_result = [1, 2, 3, 4, 5]
    >>> determine_large_straight(test_result)
    40

    >>> test_result = [3, 4, 1, 1, 1]
    >>> determine_large_straight(test_result)
    0
    """
    dice_regex = ""

    for dice in set(sorted(dice_result)):
        dice_regex += str(dice)

    seek_large_straight = re.compile(r"12345|23456")

    large_straight_result = seek_large_straight.search(dice_regex)

    if large_straight_result:
        return LARGE_STRAIGHT_VALUE()

    else:
        return SCORE_OF_ZERO()


def calculate_yahtzee(dice_result: list, score_card: dict) -> int:
    """Determine if rolled dice results in Yahtzee and if Yahtzee was already scored

    :param dice_result: A list representing 5 dice the user has rolled.
    :param score_card: A dictionary representing a Yahtzee score card.
    :precondition: dice_result must be a list containing 5 integers that represent dice created with randomly
    generated numbers. score_card must be a dictionary containing keys that represent a Yahtzee score card.
    :postcondition: Calculates if the dice resulted in a Yahtzee. If so, then checks if Yahtzee was already scored.
    If the user already got Yahtzee, return a score of 100. If the user has not earned Yahtzee yet, return a score of
    50. If the user did not get Yahtzee, return a score of 0
    :return: An int representing the score earned from rolling Yahtzee

    >>> test_result = [1, 1, 1, 1, 1]
    >>> test_card = create_scorecard()
    >>> calculate_yahtzee(test_result, test_card)
    \u001b[33mCONGLATURATION\u001b[0m !!!
    YOU GOT YOUR FIRST \u001b[33mYAHTZEE\u001b[0m
    <BLANKLINE>
    50

    >>> test_result = [2, 2, 2, 2, 2]
    >>> test_card = create_scorecard()
    >>> test_card["Yahtzee"] = 100
    >>> calculate_yahtzee(test_result, test_card)
    Okay settle down now, that's too many \u001b[33mYAHTZEE\u001b[0ms
    <BLANKLINE>
    100

    >>> test_result = [1, 2, 3, 4, 5]
    >>> test_card = create_scorecard()
    >>> calculate_yahtzee(test_result, test_card)
    0
    """
    if len(set(dice_result)) == 1 and score_card["Yahtzee"] == EMPTY_SCORE():
        FIRST_YAHTZEE_CONGRATULATIONS()
        return FIRST_YAHTZEE_VALUE()

    elif len(set(dice_result)) == 1 and score_card["Yahtzee"] >= 50:
        SUBSEQUENT_YAHTZEE_CONGRATULATIONS()
        return SUBSEQUENT_YAHTZEE_VALUE()

    else:
        return SCORE_OF_ZERO()


def calculate_score_manager(dice_result: list, score_card: dict, score_card_location: str) -> int:
    """Update a score within the Yahtzee score card.

    :param dice_result: A list representing 5 dice the user has rolled.
    :param score_card: A dictionary representing a Yahtzee score card.
    :param score_card_location: A string representing the key in score card to be updated with a new value.
    :precondition: dice_result must be a list containing 5 integers that represent dice created with randomly
    generated numbers. score_card must be a dictionary containing keys that represent a Yahtzee score card.
    score_card_location must be a string pointing an existing key within score_card.
    :postcondition: calculate_score_manager will determine which score is being updated and calls the correct function
    to return an integer representing the score that will be inserted
    :return: A dict representing a Yahtzee scorecard with a key updated.

    >>> test_result = [2, 3, 1, 1, 1]
    >>> test_card = create_scorecard()
    >>> calculate_score_manager(test_result, test_card, "Ones")
    3

    >>> test_result = [5, 5, 3, 4, 6]
    >>> test_card = create_scorecard()
    >>> calculate_score_manager(test_result, test_card, "Chance")
    23
    """
    if score_card_location in ("Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"):
        return sum_ones_to_sixes(dice_result, score_card_location)

    elif score_card_location == "4 of a kind":
        return calculate_4_of_a_kind(dice_result)

    elif score_card_location == "3 of a kind":
        return calculate_3_of_a_kind(dice_result)

    elif score_card_location == "Full House":
        return calculate_full_house(dice_result)

    elif score_card_location == "Large Straight":
        return determine_large_straight(dice_result)

    elif score_card_location == "Small Straight":
        return determine_small_straight(dice_result)

    elif score_card_location == "Yahtzee":
        return calculate_yahtzee(dice_result, score_card)

    elif score_card_location == "Chance":
        return sum(dice_result)


def insert_result(rolled_dice: list, score_card: dict) -> None:
    """Calculate result value that will be placed into a score card key.

    :param rolled_dice: A list containing six-sided dice that the user has rolled.
    :param score_card: A dictionary representing a Yahtzee score card.
    :precondition: dice_result must be a list containing 5 integers that represent dice created with randomly
    generated numbers. score_card must be a dictionary containing keys that represent a Yahtzee score card.
    :postcondition: User inputs a score key to be updated with a new value. Then the score earned by inserting the
    dice result into chosen key will be calculated. The chosen key will be updated with the value from calculating
    the score earned.
    """
    i_am_sentinel = True
    while i_am_sentinel:
        score_to_update = choose_score(score_card)

        if score_card[score_to_update] == -1:
            calculated_score = calculate_score_manager(rolled_dice, score_card, score_to_update)
            score_card[score_to_update] = calculated_score
            i_am_sentinel = False

        elif score_card[score_to_update] != 0 and score_to_update == "Yahtzee":
            calculated_score = calculate_score_manager(rolled_dice, score_card, score_to_update)
            score_card[score_to_update] = calculated_score
            i_am_sentinel = False

        else:
            print(f"{RED_TEXT()}HEY{END_COLOUR()}, you already entered a score there, don't try to pull "
                  f"a fast one on me.")


def check_if_card_full(score_card: dict) -> str:
    """Check if a player has completely filled out their score card.

    :param score_card: A dictionary representing a Yahtzee score card.
    :precondition: score_card must be a dictionary containing keys that represent a Yahtzee score card.
    :postcondition: Checks the score card for -1 which represents an empty spot in the score card. If no empty spots
    are in the score card, return 'Complete'. Otherwise, returns 'Continue'
    :return: A string that represents whether a player is finished the game or not.

    >>> check_if_card_full(create_scorecard())
    'Continue'
    """
    if EMPTY_SCORE() in score_card.values():
        return "Continue"
    else:
        return "Complete"


def a_turn(score_card: dict) -> dict:
    """Simulate a turn of Yahtzee

    Can't be easily doc tested or unit tested because multiple functions requiring input and random will be called.
    As well as a while loop to prevent user from making invalid inputs.

    :param score_card: A dictionary with keys representing points that the user can score in Yahtzee.
    :precondition: score_card is a dictionary representing a Yahtzee score card.
    :postcondition: Calls multiple functions to simulate a single round of Yahtzee
    :return: An updated dictionary representing a new score card after a single round of Yahtzee
    """
    print_scorecard(score_card)

    dice_result = dice_manager()
    insert_result(dice_result, score_card)

    print_scorecard(score_card)
    return score_card


def taking_turns() -> None:
    """Manage the alternation of player turns then return the final results of both players.

    Can't be easily doc tested or unit tested because of while loops and multiple functions calls with input
    and random.

    :postcondition: Alternates through both player's turns with a while loop. Each loop will check if a player
    has completed their score card. If so, the result will be summed up and placed into a dictionary that will
    contain the final scores for both players. If the player has not finished their score card, their turn
    function will be called and they will keep playing. When both players finish and the final_scores dictionary
    is filled in, determine_winner will be called.
    """
    player_one = create_scorecard()
    player_two = create_scorecard()

    final_scores = {"Player One Total": EMPTY_SCORE(), "Player Two Total": EMPTY_SCORE()}
    i_am_sentinel = True
    while i_am_sentinel:
        if check_if_card_full(player_one) == "Complete":
            final_scores["Player One Total"] = calculate_final_score(check_for_bonus(player_one))
            continue

        else:
            print(f"{CYAN_TEXT()}Player One{END_COLOUR()}'s turn\n")
            a_turn(player_one)

        if check_if_card_full(player_two) == "Complete":
            final_scores["Player Two Total"] = calculate_final_score(check_for_bonus(player_two))
            continue

        else:
            print(f"{MAGENTA_TEXT()}Player Two{END_COLOUR()}'s turn\n")
            a_turn(player_two)

        if check_if_card_full(player_one) == "Complete" and check_if_card_full(player_two) == "Complete":
            i_am_sentinel = False

    determine_winner(final_scores)


def determine_winner(final_scores: dict) -> None:
    """Determine winner of Yahtzee game and print witty victory messages or a message stating there is a draw.

    :param final_scores: A dictionary containing the final score of two Yahtzee players.
    :precondition: final_scores must be a dictionary containing two keys that represent two different players.
    The values of the dictionary should also be the final score of the player after finishing Yahtzee.
    :postcondition: Checks which key contains the higher value and prints a victory message for the associated player.
    If both players draw then a draw message is printed instead.

    >>> test_final_score = {"Player One Total": 555, "Player Two Total": 444}
    >>> determine_winner(test_final_score)
    Here are the \u001b[33mFINAL\u001b[0m results!
    <BLANKLINE>
    Player One Total: \u001b[33m555\u001b[0m
    Player Two Total: \u001b[33m444\u001b[0m
    \u001b[31mAS GOD AS MY WITNESS, PLAYER TWO IS BROKEN IN HALF!!!!\u001b[0m
    <BLANKLINE>
    Player One Wins!

    >>> test_final_score = {"Player One Total": 220, "Player Two Total": 220}
    >>> determine_winner(test_final_score)
    Here are the \u001b[33mFINAL\u001b[0m results!
    <BLANKLINE>
    Player One Total: \u001b[33m220\u001b[0m
    Player Two Total: \u001b[33m220\u001b[0m
    \u001b[33mIMPOSSIBLE, IT'S A DRAW!!!!\u001b[0m
    """
    print(f"Here are the {YELLOW_TEXT()}FINAL{END_COLOUR()} results!\n")

    for key, value in final_scores.items():
        print(f"{key}: {YELLOW_TEXT()}{value}{END_COLOUR()}")

    if final_scores["Player One Total"] > final_scores["Player Two Total"]:
        print(f"{RED_TEXT()}AS GOD AS MY WITNESS, PLAYER TWO IS BROKEN IN HALF!!!!{END_COLOUR()}\n")
        print("Player One Wins!")

    elif final_scores["Player Two Total"] > final_scores["Player One Total"]:
        print(f"{RED_TEXT()}AS GOD AS MY WITNESS, PLAYER ONE IS BROKEN IN HALF!!!!{END_COLOUR()}\n")
        print("Player Two Wins!")

    elif final_scores["Player One Total"] == final_scores["Player Two Total"]:
        print(f"{YELLOW_TEXT()}IMPOSSIBLE, IT'S A DRAW!!!!{END_COLOUR()}")


def main():
    """Execute program."""
    # doctest.testmod(verbose=True)
    taking_turns()


if __name__ == '__main__':
    main()
