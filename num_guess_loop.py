#!/usr/bin/env python3

# Author: Tony G

# Date: 2025-04-26

# This program generates a random number and asks the user to guess it
# until they guess correctly, using a loop and a break statement.

import random


def main():
    # Generate a random number between 1 and 10
    correct_number = random.randint(1, 10)

    print("Guess the number between 1 and 10!")

    while True:
        try:
            # Input
            user_guess = int(input("Enter your guess: "))

            # Process & Output
            if user_guess == correct_number:
                print("You guessed correctly!")
                break
            else:
                print("Incorrect guess. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
