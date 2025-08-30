import random
print("Rock Paper Seessior Game : ")

user_wins=0
computer_wins=0
options=["rock", "paper", "scissor"]
while True:
    user_input=input("Type Rock/Paper/Scissor or Q to quit ").lower()
    if user_input=='q':
        break
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    # 0 For Rock 1 1 for Paper 2 for Scissor
    computer_pick=options[random_number]
    print("Computer Picked :",computer_pick)
    if user_input=='rock' and computer_pick=='scissor':
        print("You Won ")
        user_wins+=1
    elif user_input=='paper' and computer_pick=='rock':
        print("You Won ")
        user_wins+=1
    elif user_input=='scissor' and computer_pick=='paper':
        print("You Won ")
        user_wins+=1
    else:
        print("You Lost")
        computer_wins+=1
print("You Won ",user_wins," Times")
print("The Computer wons",computer_wins," times")
print("\n\n Good Bye ..")    