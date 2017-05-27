"""CS 61A Presents The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS>0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return the
    number of 1's rolled (capped at 11 - NUM_ROLLS).
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    total = 0
    one_count = 0
    num_rolls_copy = num_rolls

    #just rolling the dice here
    while num_rolls > 0:
        point = dice()
        num_rolls-=1
        if point != 1:
            total += point
        else:
            one_count += 1

    #now implementing case of Pig Out
    if one_count > 0:
        return min(11-num_rolls_copy, one_count)
    else:
        return total

    # END PROBLEM 1


def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2

    # copying opponent's score into another variable so as not to modify the original.
    opponent_score_copy = opponent_score
    #generating the digits of opponent's score
    tens =  opponent_score_copy//10
    ones = opponent_score_copy%10

    return 1+max(tens,ones)

    # END PROBLEM 2


# Write your prime functions here!
def is_prime(curr_score_1):

    if curr_score_1==1:
        return False

    n = curr_score_1//2

    while n>1:
        rem = curr_score_1%n
        n-=1
        #some code here
        if rem == 0:
            return False
    return True

def next_prime(curr_score_2):
    n=curr_score_2 + 1
    while n>curr_score_2:
        if is_prime(n):
            return n
        else:
            n += 1


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player. Also
    implements the Hogtimus Prime rule.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2

    curr_score = 0
    #implementing free bacon as first step based on num_rolls
    if num_rolls == 0:
        curr_score = free_bacon(opponent_score)
    else:
        curr_score = roll_dice(num_rolls, dice)

    #now changing the score according to hogtimus prime
    if is_prime(curr_score):
        curr_score = next_prime(curr_score)

    return curr_score
    # END PROBLEM 2


def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog Wild).
    """
    # BEGIN PROBLEM 3
    "*** REPLACE THIS LINE ***"
    sum=score+opponent_score
    if sum%7==0:
        return four_sided
    else:
        return six_sided
    # END PROBLEM 3

def is_swap(score0, score1):
    """Returns whether one of the scores is double the other.
    """
    # BEGIN PROBLEM 4
    if (score0==2*score1) or (score1==2*score0):
        return True
    else:
        return False

    "*** REPLACE THIS LINE ***"
    # END PROBLEM 4

def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5

    while score0<goal and score1<goal:
        #variable to keep track only for the current ONE turn.
        turn_score = 0

        #using variables to allow abstraction for generality in functions.
        if player == 0 :
            own_score, opp_score = score0, score1
        else:
            own_score, opp_score = score1, score0

        #Hog Wild to change the nature of dice
        curr_dice = select_dice(own_score,opp_score)

        #for player 0 or 1
        if player == 0:
            num_rolls = strategy0(own_score,opp_score)
        else:
            num_rolls = strategy1(own_score,opp_score)

        #to record the own_score, already includes Free Bacon, Pig Out, Hogtimus Prime.
        turn_score = take_turn(num_rolls, opp_score, dice=curr_dice)

        #updating current player's score
        own_score += turn_score

        #implementing Swine Swap
        if player == 0:
            if is_swap(own_score,opp_score):
                score0, score1 = opp_score, own_score
            else:
                score0, score1 = own_score, opp_score
        else:
            if is_swap(own_score,opp_score):
                score1, score0 = opp_score, own_score
            else:
                score0, score1 = opp_score, own_score

        #changing the player
        player = other(player)

    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid
    strategy output. All strategy outputs must be integers from -1 to 10.

    >>> check_strategy_roll(10, 20, num_rolls=100)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(10, 20) returned 100 (invalid number of rolls)

    >>> check_strategy_roll(20, 10, num_rolls=0.1)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(20, 10) returned 0.1 (not an integer)

    >>> check_strategy_roll(0, 0, num_rolls=None)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(0, 0) returned None (not an integer)
    """
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert 0 <= num_rolls <= 10, msg + ' (invalid number of rolls)'


def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the
    strategy returns a valid input. Use `check_strategy_roll` to raise
    an error with a helpful message if the strategy returns an invalid
    output.

    >>> def fail_15_20(score, opponent_score):
    ...     if score != 15 or opponent_score != 20:
    ...         return 5
    ...
    >>> check_strategy(fail_15_20)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(15, 20) returned None (not an integer)
    >>> def fail_102_115(score, opponent_score):
    ...     if score == 102 and opponent_score == 115:
    ...         return 100
    ...     return 5
    ...
    >>> check_strategy(fail_102_115)
    >>> fail_102_115 == check_strategy(fail_102_115, 120)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(102, 115) returned 100 (invalid number of rolls)
    """
    # BEGIN PROBLEM 6
    "*** REPLACE THIS LINE ***"
    moi = 0

    while moi<goal:
        toi = 0
        while toi<goal:
            num_rolls = strategy(moi,toi)
            res = check_strategy_roll(moi,toi,num_rolls)
            if res == None:
                toi+=1
        moi+=1
    return None

    # END PROBLEM 6


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    """
    # BEGIN PROBLEM 7


    def temp(*args):
        num_samples_copy = num_samples
        arbit=0
        while num_samples_copy>0:
            arbit = arbit + fn(*args)
            num_samples_copy-=1
        return arbit/num_samples
    return temp

    # END PROBLEM 7


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN PROBLEM 8
    make_averaged_var = make_averaged(roll_dice,num_samples)
    iterator,dice_init = 0,0
    while iterator<10:
         iterator+=1
         dice_new = make_averaged_var(iterator,dice)

         if dice_init < dice_new:
            dice_init = dice_new
            lower = iterator
    return lower

    # END PROBLEM 8


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(4)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False: # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False: #False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 9

    trial1 = free_bacon(opponent_score)
    if is_prime(trial1):
        trial1 = next_prime(trial1)

    if trial1==margin or trial1>margin:
        return 0
    else:
        return num_rolls

    # END PROBLEM 9
check_strategy(bacon_strategy)


def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points and would not cause a swap.
    Otherwise, it rolls
    NUM_ROLLS.
    """
    # BEGIN PROBLEM 10

    if is_swap(score, opponent_score) and opponent_score>score:
        return 0
    else:
        a = bacon_strategy(score, opponent_score, margin, num_rolls)
        return a

    # END PROBLEM 10
check_strategy(swap_strategy)


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    Common pointers from previous 61a websites:
    Don't swap scores when you're winning.
    Find a way to leave your opponent with four-sided dice more often.
    If you are in the lead, you might take fewer risks. If you are losing, you might take bigger risks to catch up.
    Trigger a beneficial swine swap by trying to score only one point.
    """
    # BEGIN PROBLEM 11
    "*** REPLACE THIS LINE ***"
    trial3 = max((opponent_score//10),(opponent_score%10)) + 1

    #Trigger a beneficial swine swap as long as new addition to my score doesnt give disadvantage.
    if (score+1)*2 == opponent_score:
        return swap_strategy(score,opponent_score,14,10) #14,10

    #opponent gets left with a four-sided die iff new score and opponent_score are divisble by 7
    elif (score + trial3 + opponent_score) % 7 == 0 and trial3 >= 7:
        return 0

    elif (score + opponent_score) % 7 == 0 and score<opponent_score:
        return swap_strategy(score, opponent_score, 3, 7)   #3,7

    elif score < opponent_score:
        return swap_strategy(score, opponent_score, 11, 7)   #11, 7

    else:
        return bacon_strategy(score, opponent_score,8, 4)

    # END PROBLEM 11
check_strategy(final_strategy)


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
