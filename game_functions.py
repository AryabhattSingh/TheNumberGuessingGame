import random
import os


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
    pass


def make_a_guess():
    pass


def evaluate_guess(random_selected_number, user_guess, lives):
    pass


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
