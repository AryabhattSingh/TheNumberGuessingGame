import random
import os

EASY_LEVEL_LIVES = 10
MEDIUM_LEVEL_LIVES = 7
HARD_LEVEL_LIVES = 5


def first_game_instructions():
    print("\nComputer will select a number in the range of 1 to 100.")
    print("You will have to guess that number.")
    print("You get 10 lives in EASY and 5 lives in HARD mode.")
    print("For each wrong guess a life will be deducted.")
    print("\nIf you guess the number before your lives run out, you win!")


def print_game_instructions():
    print("\nDepending on the absolute difference between user guess and computer selected number, "
          "one of the following will be printed :")
    print("> 20           -> Too High or Too Low")
    print(">=10 and <=20  -> High or Low")
    print(">=5 and <10    -> Close")
    print(">=3 and <5     -> Very Close")
    print(">=1 and <3     -> Almost there")


def set_difficulty():
    level = ""
    while level != "easy" and level != "hard":
        level = input("\nChose a difficulty level. Type 'EASY' or 'MEDIUM' or 'HARD' :").lower()
        if level == "easy":
            return EASY_LEVEL_LIVES
        elif level == "medium":
            return MEDIUM_LEVEL_LIVES
        elif level == "hard":
            return HARD_LEVEL_LIVES
        else:
            print("\nKindly enter a valid value!")


def is_guess_valid(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def make_a_guess():
    guess_valid = False
    while not guess_valid:
        user_guess = input("\nMake a guess: ")
        if is_guess_valid(user_guess):
            user_guess = int(user_guess)
            if user_guess <= 0 or user_guess > 100:
                print("Kindly enter a whole number between 0 and 100 only!")
            else:
                return user_guess
        else:
            print("Kindly enter whole number only!")


def evaluate_guess(random_selected_number, user_guess, lives):
    difference = user_guess - random_selected_number
    abs_difference = abs(difference)
    if abs_difference != 0:
        lives -= 1

    if abs_difference > 20:
        if difference > 0:
            print("Too High.")
        else:
            print("Too Low.")
    elif abs_difference in range(10, 21):
        if difference > 0:
            print("High")
        else:
            print("Low")
    elif abs_difference in range(5, 10):
        print("Close")
    elif abs_difference in range(3, 5):
        print("Very Close")
    elif abs_difference in range(1, 3):
        print("Almost there")
    else:
        print(f"\n{'*' * 30}")
        print(f"You got it! The answer was {user_guess}")
        print(f"{'*' * 30}")

    return lives


def play_game():
    print(f"\nWelcome to The Number Guessing Game!")
    lives = set_difficulty()
    print(f"\nCOMPUTER SELECTED A NUMBER IN THE RANGE OF 1 AND 100")
    random_selected_number = random.randint(1, 100)

    user_guess = 0
    while user_guess != random_selected_number and lives > 0:
        print(f"\nYou have {lives} attempts remaining to guess the number.")
        user_guess = make_a_guess()
        lives = evaluate_guess(random_selected_number, user_guess, lives)
        if lives == 0:
            print(f"\n{'*' * 36}")
            print("You have run out of lives. Game over")
            print(f"{'*' * 36}")
        elif user_guess != random_selected_number:
            print("Guess again!")


def another_round():
    next_round = ""
    while next_round != "y" and next_round != "n":
        next_round = input("\n\n-Do you want to play another round?-----\n"
                           "Type 'y' to start a new game or 'n' to stop: ").lower()
        if next_round != "y" and next_round != "n":
            print(f"\n{'+' * 40}")
            print("Kindly enter 'y' or 'n' only!")
            print(f"{'+' * 40}")
    return next_round
