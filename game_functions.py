
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


