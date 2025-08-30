# BANK MANAGEMENT SYSTEM:

# BANK ACCOUNT
# DEPOSIT MONEY
# WITHDRAW MONEY
# DETAILS
# UPDATE DETAILS
# DELETE ACCOUNT
import json
import random
import string
from pathlib import Path
class Bank:
    database='data.json'
    data=[]
    try:
       if Path(database).exists():
        with open(database) as fs:
            data=json.loads(fs.read())
       else:
        print("No Such File Exists .. ")
    except Exception as err:
       print(f"An Exception occured at {err}")
    @classmethod
    def __update(cls):
       with open(cls.database,'w')as fs:
             fs.write(json.dumps(Bank.data,indent=4))
    @classmethod
   # This will generate random account number
    def __account_generator(cls):
       alpha=random.choices(string.ascii_letters,k=3)
       num=random.choices(string.digits,k=3)
       specchar=random.choices("!@#$&*",k=1)
       id=alpha+num+specchar
       random.shuffle(id)
      #  ya shuffle hony ka badd humain list mily gi par usko string main convert karna pary ga.
       return "".join(id)
       
      # 1)  Create Account:
    def create_account(self):
       info={
       "Name":input("Enter Your Name :"),
       "Age":int(input("Enter Your Age :")),
       "Email":input("Enter Your Email :"),
       "Pin":input("Enter Your 4 No Pin"),
       "Account Number":Bank.__account_generator(),
       "Balance":0
       }
       if info['Age'] < 18 or len(str(info['Pin']))!=4: 
          #caanot find len of int .thatswyh we convert this into str
          print("Sorry ... You cannot create your bank account.Age must be greater than 18 and pin must be 4 digits")
       else:
          print("Congratulations !!! Your account has been created ")
          for i in info:
             print(f"{i} : {info[i]}")
          print("Note down your Account Number")

          Bank.data.append(info)
          Bank.__update()

         # 2) Deposit  MONEY
    def depositmoney(self):
        accnum=input("Enter Your Account Number :")
        pin=input("Enter Your Pin :")
        userdata=[i for i in Bank.data if i['Account Number']==accnum and i['Pin']==pin]

        if userdata==False:
           print("Sorry Data Not Found ...")
        else:
           amount=int(input("how much you want to deposit"))
           if amount>10000 or amount<0:
              print("Sorry Amount is too much .you can deposit below 100000 or below zero")
           else:
              userdata[0]['Balance']+=amount
            #   dictionary ka ander list ha phly first index ko access karna ho ga
              Bank.__update()
              print("Money Deposited Successfully")
          
         #  3) Withdraw Money:
    def withdrawmoney(self):
        accnum=input("Enter Your Account Number :")
        pin=input("Enter Your Pin :")
        userdata=[i for i in Bank.data if i['Account Number']==accnum and i['Pin']==pin]

        if userdata==False:
           print("Sorry Data Not Found ...")
        else:
           amount=int(input("how much you want to withdraw"))
           if userdata[0]['Balance']< amount:
              print("Sorry You dont have that much money")
           else:
              userdata[0]['Balance']-=amount
            #   dictionary ka ander list ha phly first index ko access karna ho ga
              Bank.__update()
              print("Money Withdrew Successfully")    


      #   4)       SHOW DETAILS: 

    def showdetails(self):
        accnum=input("Enter Your Account Number :")
        pin=input("Enter Your Pin :")
        userdata=[i for i in Bank.data if i['Account Number']==accnum and i['Pin']==pin]
      #   print(userdata) # is sa humain list ka ander aik dictionary print hogi

        print("Your Information : \n\n")
        for i in userdata[0]:
            print(f"{i}:{userdata[0][i]}")

# 5) UPDATE DETAILS:
    def updatedetails(self):
        accnum=input("Enter Your Account Number :")
        pin=input("Enter Your Pin :")
        userdata=[i for i in Bank.data if i['Account Number']==accnum and i['Pin']==pin]
        if userdata==False:
          print("No Such User Found")
        else:
           print("You Cannnot change the age,balance and account Number")
           print("Fill the details for change or leave it empty for no change")
           newdata={
              "Name":input("Enter Your Name :"),
              "Email":input("Enter Your New Email :"),
              "Pin":input("Enter Your New Pin")
           }
         #   if newdata['Name']==userdata[0]['Name']:
         #   username[0] is liye likha ha k userdata list main list ka ander [0] indeex par dictioary ha.
         # aur dictionary ka ander [name] ko access kar rahay han/
        if newdata['Name']=="":
           newdata["Name"]=userdata[0]["Name"]
         #   age empty ha to samny wala change nahi karna cha raha aur purana wala hi aa jye ga
        if newdata['Email']=="":
           newdata["Email"]=userdata[0]["Email"]
        if newdata['Pin']=="":
           newdata["Pin"]=userdata[0]["Pin"]

        newdata['Age']=userdata[0]['Age']
        newdata['Account Number']=userdata[0]['Account Number']
        newdata['Balance']=userdata[0]['Balance']

        if type(newdata['Pin'])==str:
           newdata['Pin']=int(newdata['Pin'])
         #   age Pin string hui to wo Int main convert ho jye gi.

         # abi jo hum na ya dummy data banaya ha isko orignal data main put akr dain gyn..
        for i in newdata:
           if newdata[i]==userdata[0][i]:
              continue         
         #   agr dono same hain to continue karo change karny ki zarorat nahi.
           else:
              userdata[0][i]=newdata[i]

        Bank.__update()
        print("Details Updated Successfully")

      # 6)  Delete details:           
    def deletedetails(self):
       accnum=input("Enter Your Account Number :")
       pin=input("Enter Your Pin :")
       userdata=[i for i in Bank.data if i['Account Number']==accnum and i['Pin']==pin]
       if userdata==False:
          print("No Such Data Found ..")
       else:
          check=input("Enter Y If You want to delete Your Account. or press N")

          if check=="N"or check=="n":
             print("byPassed.Nothng Chaanged")
          else:
             index=Bank.data.index(userdata[0])
             Bank.data.pop(index)
             print("Account Deleted Successfully ..")
             Bank.__update()




user=Bank()
print("Press 1 to create an account")
print("Press 2 to deposit money in bank")
print("Press 3 to withdraw money from bank")
print("Press 4 to show details")
print("Press 5 to update the bank details")
print("Press 6 to delete the account")
check=int (input("Tell Your Responce :"))
if check==1:
   user.create_account()
if check==2:
   user.depositmoney()
if check==3:
   user.withdrawmoney()
if check==4:
   user.showdetails()
if check==5:
   user.updatedetails()
if check==6:
   user.deletedetails()