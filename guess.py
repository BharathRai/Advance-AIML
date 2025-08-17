import random

# 1. Set the range and generate the secret number
secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100. Can you guess it?")

# 2. Initialize variables
attempts = 0
guess = 0 # Initialize guess to a value that won't match the secret number

# 3. Start the game loop
# The loop continues as long as the guess is not correct
while guess != secret_number:
    try:
        # Get the player's guess
        guess_input = input("Enter your guess: ")
        guess = int(guess_input)
        
        # Increment the attempt counter
        attempts += 1

        # 4. Provide feedback
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")

    except ValueError:
        print("Oops! That's not a valid number. Please enter a number.")

# 5. Print the success message after the loop ends
print(f"🎉 You got it! The secret number was {secret_number}.")
print(f"It took you {attempts} attempts to guess correctly.")