#Simple Password Generator 1.0 by Houman Hafez (SpecialSpicy)
#Imports (Random to use choice and shuffle) (string to use all the letters, digits and etc. in a simple line of code without doing too much)
import string
import random

#Defining a list with letters, digits and other characters
characters = list(string.ascii_letters + string.digits + " !@#$%^&*()")

#A function to generate a password (Exception Handling: ValueError Included)

def generate_password():
    try:
        #Input of a number defines the length of the password. 
        password_length = int(input("How long would you like your password to be? "))


        #Shuffling the characters list
        random.shuffle(characters)
        
        #An empty list
        password = [] 
         
        #A for loop to add random letters in length of the input of the user into our list
        for x in range(password_length):
            password.append(random.choice(characters))
        
        #Shuffling it again to make sure it's as random as possible
        random.shuffle(password)
        
        #This line turns our list to a variable and then it gets printed
        password = "" .join(password)
        print(password)

        #As said before ValueError is taken care of.
    except ValueError:
        print("Please Type Only A Number!")

#With a while loop the user gets asked if he/she wants a password
#Since it's a loop the user doesn't have to start the application again
while True:

    option = input("Do you want to generate a password? (Y/N): ").lower()

    #With a If Statement the user's input gets taken care of
    if option == "y":
        generate_password()
    elif option == "n":
        print("Program Terminated!")
        quit()
    else:
        print("Invalid input, please input Y or N")
        