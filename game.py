
V
import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

print("Guess a number between 1 and 100:")

# Number of attempts the user has made
attempts = 0

while True:
    # Increment the attempts counter
    attempts += 1

    # Get user's guess
    guess = int(input("Enter your guess: "))

    # Check the user's guess
    if guess < number_to_guess:
        print("Higher!")
    elif guess > number_to_guess:
        print("Lower!")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break
