name = input("Type your name: ")
print(f"Welcome {name} to this adventure")

answer = input("You are on a dirt road and it has come to an end and you can go left or right. Which way do you want to go? (left/right) ").lower()

if answer == "left":
    answer2 = input("You have now come to a river? Do you want to swim accross or walk around. (walk/swim) ").lower()
    if answer2 == "swim":
        print("You swam accross and were eaten by piranhas")
    elif answer2 == "walk":
        answer3 = input("You walked for many miles and found a village. What will you do skip the village or go in and ask for help? (skip/help) ").lower()
        if answer3 == "skip":
            print("You kept on walking, ran out of water and died of dehydration. You Lost!")
        elif answer3 == "help":
            print("You went to the village to seek for help. Some kind villagers guide you in and provide place to stay.")
        else:
            print("Not a valid option.")
    else:
        print("Not a valid option.")

elif answer == "right":
    answer4 = input("You came to a bridge, it looks old, are you courageous enough to cross it or do you want to head back? Type cross or back. ").lower()
    if answer4 == "cross":
        print("Congrats! you passed the game! You meet a stranger who helps you go back to your city.")
    elif answer4 == "back":
        print("You lost! This game is not for cowards")
    else:
        print("Not a valid option.")
else:
    print("Not a valid option.")