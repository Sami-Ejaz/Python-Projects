import random
import time

operators=["+","-","*"]
min_value=3
max_value=15
total_queation=10
def quetion_generator():
    left=random.randint(min_value,max_value)
    right=random.randint(min_value,max_value)
    operator=random.choice(operators)
    exp=str(left)+" "+operator+" "+str(right)
    ans=eval(exp)
    return exp,ans

# exp,ans=quetion_generator()
# print(exp,ans)
wrong=0
input("Press Enter To Start :")
print(" -----------------------------------")
start_time=time.time()
for i in range(total_queation):
    exp,ans=quetion_generator()
    while True:
        guess=input("Question "+str(i+1)+")  "+exp+"= ")
        if guess==str(ans):
            break
        wrong+=1
end_time=time.time()
total_time=round(start_time-end_time,2)
print("You Finished in ",total_time," seconds")
print("----------------------------------------")
print("Nice Work ...........")