# The Number Guessing Game

Welcome to the Number Guessing Game! This project offers an engaging guessing game where players can test their luck and intuition. In this game, users are presented with various options and challenges to make their gaming experience enjoyable.

## Getting Started

To begin playing the Number Guessing Game, follow these steps:

### I. Starting the Game

1. When the game starts, you will be prompted with a question: `Do you want to play the game? (y/n)`

2. If you enter `"y"`, the game will commence, and you will embark on an exciting journey. Here's what you can expect:

    1. An ASCII art display will set the mood for your gaming adventure.

    2. You will receive the following instructions and information:
	```bash
        a. The computer will choose a random number from the range of 1 to 100.

        b. Your primary objective is to guess this secret number.

        c. In EASY mode, you will have a generous 10 lives, in MEDIUM mode 7 lives while HARD mode provides a challenging 5 lives.

        d. Every incorrect guess will result in the deduction of one life.

        e. Your ultimate goal is to guess the number correctly before your lives run out. Victory awaits those who succeed!

        f. Depending on the absolute difference between your guess and the computers selected number, one of the following messages will be displayed:
           - 100 <= Difference > 20 : "Too High" (if your guess is too high) or "Too Low" (if your guess is too low).
           -  10 <= Difference <= 20: "High" or "Low."
           -   5 <= Difference < 10 : "Close."
           -   3 <= Difference < 5  : "Very Close."
           -   1 <= Difference < 3  : "Almost there."
	```

    3. You will be asked to choose your preferred difficulty level (`EASY`, `MEDIUM`, or `HARD`).

    4. The computer will randomly select a number between 1 and 100, both inclusive.

    5. The number of lives available to you will be displayed, ensuring you always know your status.

    6. You will be prompted to make your first guess. Input checking is implemented here to prevent crashes and to ensure that only whole numbers within the range [1, 100] are accepted.

    7. Your guess will be evaluated according to the game rules. Relevant information will be printed on the console, and if your guess is incorrect, one life will be deducted.

    8. If you successfully guessed the number before running out of lives, congratulations, you win! You will be greeted with a celebratory message.

    9. After the game concludes, you will be asked if you want to play another round. Input validation is in place to ensure that you only enter "y" for yes or "n" for no.
        - If you choose `"y"`, the console will be cleared, and a new game will start.
        - If you choose `"n"`, the game will bid you farewell.

### II. Ending the Game

1. If you enter `"n"` when asked if you want to play, the game will conclude gracefully, leaving you with a `"Goodbye"` message.

Enjoy the Number Guessing Game and have a fantastic time testing your guessing skills!

## License

This project is licensed under the MIT License. For more details, please refer to the [LICENSE](LICENSE) file.
