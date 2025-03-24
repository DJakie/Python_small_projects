print("QUIZZZ TIME!!")

playing = input("Do you want to play a quiz on Reserve Bank of India? ")

if playing.lower() != "yes":
    quit()

print("okay lets play!")
count = 0

answer = input("When was Reserve Bank of India established? ")
if answer.lower() == "1935":
    print("CORRECT ANSWER!")
    count += 1
else: 
    print("wrong answer :(")

answer = input("What was the act which lead to establishment of RBI? ")
if answer.lower() == "reserve bank of india act":
    print("CORRECT ANSWER!")
    count += 1
else: 
    print("wrong answer :(")

answer = input("When did the RBI Act take place? ")
if answer.lower() == "1934":
    print("CORRECT ANSWER!")
    count += 1
else: 
    print("wrong answer :(")

answer = input("Who was the first governor of RBI? ")
if answer.lower() == "osborne smith":
    print("CORRECT ANSWER!")
    count += 1
else: 
    print("wrong answer :(")

answer = input("Who was the first Indian governor of RBI? ")
if answer.lower() == "c d deshmukh":
    print("CORRECT ANSWER!")
    count += 1
else: 
    print("wrong answer :(")


print(f"you scored {count}/5 which is {count*20} %")