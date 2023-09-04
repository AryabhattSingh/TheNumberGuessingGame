from game_functions import *
from ascii_art import *

want_to_play = ""

while want_to_play != "y" and want_to_play != "n":
    want_to_play = input("\nDo you wan to play the game?\n"
                         "Type 'y' to enter in game or 'n' to quit : ").lower()
    if want_to_play != "y" and want_to_play != "n":
        print(f"\n{'+' * 30}")
        print("Kindly enter a valid entry")
        print(f"{'+' * 30}")


if want_to_play == "y":
    print(logo)
    first_game_instructions()
    next_game = ""
    while next_game != "n":
        print_game_instructions()
        play_game()
        next_game = another_round()
        if next_game == "y":
            clear_screen()
    else:
        goodbye()

elif want_to_play == "n":
    goodbye()
