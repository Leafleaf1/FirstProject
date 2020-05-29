# Leaf Bennett
# Created May 29, 2020

import random
import library
# Initial variables
health = 100

userName = input("Enter Your Name")
userName = userName.title()
print(library.text.intro)
print("Welcome to Hidden Valley! Let's begin")
userInput = input("Do you choose the fast route (1) or the scenic route (2) \n")

if userInput == "1":
    print(f"{userName}, you have started your journey on the fast route!")
    userInput = input("You found a horse, would you like to ride it? yes (1) | no (2) \n")
    if userInput == "1":
        print("You've started the speedy way to go get !")

if userInput == "2":
    print(f"{userName}, you have started your journey on the scenic route!")
