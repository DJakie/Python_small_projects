# RANDOM NUMBER GUESSING GAME

import random

# Defining a function to take the initial guess of the user
def get_valid_guess():
    while True:
        guess = input("Type a number: ")

        if guess.isdigit():
            guess = int(guess)
            if guess >= 0:
                return guess
            else:
                print("Please enter a non-negative number.")
        else:
            print("Invalid input! Please type a number next time.")

print("Can you guess a number between 0 and 10?")


## random number between 0 to 10
# random.randrange(0,101) 
# or
random_number = random.randint(0,10)

# Assigning the guess to a variable
guess = get_valid_guess()

# Assistance for the user to get the correct guess
count = 1 # counter for the number of attempts
while guess != random_number:
    count += 1
    if guess > random_number:
        try_again = input("Sorry you have guessed a number higher than the actual number. Would u like to try again? (yes/no) ").lower()
    else:
        try_again = input("Sorry you have guessed a number lower than the actual number. Would you like to try again? (yes/no) ").lower()
    
    if try_again == "yes":
        guess = get_valid_guess()
    else:
        print("Game Over!")
        quit()

print(f"Congragulations! You have guessed the number correctly in {count} attempts !!")