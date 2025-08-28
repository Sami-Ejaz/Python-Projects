import random
print("Roll a Dice Game: ")
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll

while True:
 player=input("Enter Player Between 2-4 ")
 if player.isdigit():
    player=int(player)
    if 2<=player<=4:
       break
    else:
       print("Player must be between 2-4 :")
 else:
    print("Invalid. Try Again")

max_score=50
player_score=[0 for i in range(player)]
# this is list comprehension . it will make all zero scores as 0
while max(player_score)< max_score:
   for player_idx in range(player): 
     print("\nPlayer Number",player_idx +1 ," Turn Has Started")
     print("Your Total Score is :",player_score[player_idx],"\n")
     current_score=0

     while True:
      should_roll=input("Would You Like To Roll (y):? ")
      if should_roll.lower()!="y":
       break


      value=roll()

      if value==1:
       print("You Rolled a 1 And Your Turn is Over ..")
       break
     
      else:
       current_score+=value
       print("You Rolled a :",value)

     print("Your Current Score is : ",current_score)

   player_score[player_idx]+=current_score
   print("Your Total Socre is :",player_score[player_idx])
max_score=max(player_score)
wining_idx=player_score.index(max_score)
print("Player Number ",wining_idx+1," is the winner the the score ",max_score)





        
                
    

        

        
