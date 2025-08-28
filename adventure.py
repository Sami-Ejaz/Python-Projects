print("Welcome to the Adventure Game : ")
name=input("Enter Your Name :")
print("Welcome ",name," to the Adventure World ..")
user_input=input("Press Y if you want to play this Game ").lower()
if user_input==('y'):
    ans=input("You were on a dirt road  and it has come to end.You can now go to left or right." \
    " which way you awnt to go? ").lower()
    if ans=="left":
        ans2=("There is river Ahead . do you want to swim or want to have a boat ").lower()
        if ans2=="boat":
            print("Here is Your Boat and have safe Joourney")
        elif ans2=="swim":
            print("Here is your Jacket go and swim")
        else:
            print("You Have choose wrong choice")
    elif ans=="right":
        ans3=input("You are on the Right side. You want to have car or go back. ").lower()
        if ans3=="car":
            print("Rock and Roll Car is cheat code for car. ")
        elif ans3=="back":
            print("So you dont want to go ahead .. have Safe Journey .You can Walk back yo your home")
    else:
        print("You Have Choose Wrong choice ..")
else:
    print(" So You dont want to play this game .Okay Bye ..")
