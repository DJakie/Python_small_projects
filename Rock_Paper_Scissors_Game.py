import random

user_wins = 0                                                               #variable to store no of times the user won
computer_wins = 0                                                           #variable to store no of times the computer won

options = ["rock", "paper", "scissors"]                                     #assigning the options in a list

while True:
    user_input = input("Type Rock/Paper/ Scissors or Q to quit. ").lower()  #taking the input form the user and converting to lower
    if user_input == "q":
        break                                                               #to break the while loop when the user wants to quit

    if user_input not in options:                                           #go back to start of while loop again to allow user to input his options again
        print("Please enter correct options.")
        continue

    random_number = random.randint(0,2)                                     #generating random number as rock: 0, paper: 1, scissors: 2 for input of computer                 
                                                                            
    computer_pick = options[random_number]                                  #assigning the numbers to rock paper and scissor using list created before
    print(f"Computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick =="scissors":                 #using if elif and else for all the outcomes of the game
        print("You won!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick =="rock":
        print("You won!")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick =="paper":
        print("You won!")
        user_wins += 1
    
    elif user_input == computer_pick:
        print("Its a Draw!")    
    
    else: 
        print("You lost!")
        computer_wins += 1
    
print(f"You won {user_wins} times.")                                          #final result of the game
print(f"The computer won {computer_wins} times.")
print("Goodbye!") 
