import sys
import os
import getpass

print("Login")

def search(username, password, users): #Söker efter användare
   for user in users:
       user = user.split(',')

       if password: #om användare och lösen stämmer, return true. Annars false.
           if user[0] == username and user[1] == password:
               return True
       else:
           if user[0] == username:
               return True
   return False


def get_balance(username, password, users): #Få fram användarens balance
   for user in users:
       user = user.split(',')

       if user[0] == username and user[1] == password:
           return user[2]

#skickar pengar från en användare till en annan
def transfer(username, amount, balance, account, users):
   for i, user in enumerate(users): #enumerate så i vet vart den skall börja
       user = user.split(',')
       if user[0] == username:
           users[i] = ','.join([username,user[1], str(float(balance) - float(amount))]) + '\n'

       if user[0] == account:
           new_balance = float(user[2]) + float(amount)
           print("New BitJespercoin balance is: ", new_balance)
           users[i] = ','.join([account, user[1], str(new_balance)]) + '\n'

   with open('USER_INFORMATION.txt', 'w') as my_file:
       for user in users:
           my_file.write(user)


with open('USER_INFORMATION.txt', 'a') as my_file:
   Greet_customer = input("Welcome to JC BANK. Are you a member of us? \n type:Yes/No  ")
   if Greet_customer == 'Yes':
       print("Perfect.")
   else:
       make_membership = input("Would you like to become a member? type: \n Yes/No  ")
       print("We give all members 3 BitJespercoin as a welcome gift. ")
       if make_membership == 'Yes':
           create_user = input("Please type your new-username:  " "\n")
           create_pass = input("Please type a password:  " "\n")
           my_file.write('\n')
           my_file.write(','.join([create_user, create_pass, '3']))
           print("Your username has now been created. You will now gonna redirect you to login. ")
       else:
           print("Ok thank you for visiting.  ")
           quit()

#öppnar, läser filen, kollar ifall login är korrekt.
with open('USER_INFORMATION.txt', 'r+') as my_file:

   users = my_file.readlines()
   while True:
       username = input("Type in your Username:  " "\n")
       password = input("Type in your Password:  " "\n")
       if username == "":
           continue


       if search(username, password, users):
           choice = input("Do you want to transfer BitJespercoin from your account to another. \n (Yes/No) ")
           if choice == "Yes":
               balance = get_balance(username, password, users)

               while True:
                   account = input("Please enter the account you want to transfer to \n")
                   if not search(account, None, users): #om användare ej har password, break
                       print("No user exists with account " + account)
                   else:
                       break
               while True:
                   amount = input("Enter the amout of BitJespercoins you want to transfer \n Amount: ")
                   #om amount är större än användares balance, break.
                   if float(amount) > float(balance):
                       print("Amount you entered is more than your balance ")
                   else:
                       break
               #annars, kör transfer
               transfer(username, amount, balance, account, users) #överför pengarna
               print("Transfer completed!")

           break
       else:
           print('\n'"Username or password was incorrect.", "'", username.capitalize(),"'.")
           print("Try again please. ")
       continue

   print("good job ")









