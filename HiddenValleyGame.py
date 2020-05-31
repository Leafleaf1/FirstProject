# Leaf Bennett
# Created May 29, 2020

from termcolor import colored
import library
from library import storyText, loseHP, storyText, situationText


# Initial variables
health = 100

userName = situationText("Enter Your Name: ")
userName = userName.title()

storyText(library.text.intro)

storyText("Welcome to Hidden Valley! Let's begin \n")

userInput = situationText("Do you choose the fast route (1) or the scenic route (2) \n")

#First Story - Leaf
if userInput == "1":
    storyText(f"{userName}, you have started your journey on the fast route! \n")
    userInput = situationText(situationText("You found a horse, would you like to ride it? Yes (1) | No (2) \n"))
    if userInput == "1":
        storyText("You've started the speedy but loud way to go get to the stream!\n")
        userInput = situationText("After a few minutes of riding the horse you spotted a bear getting closer, \n do you"
                          "want to hop off and try to scare the bear off 60% (1) or turn the horse around and run"
                          "away 80% (2)? \n")
        if userInput == "1":
            x = library.rng_percentage()
            if x >= 60:
                storyText("You scared off the bear, but you noticed you've lost the trail! \n You see the town in the"
                      "distance")

                pass
            if x < 60:
                health -= 20
                loseHP("You now have " + str(health) + "HP")
                storyText("The bare cut your back, but you managed to escape!")
                storyText("You got lost trying to run away from the bear but you can see the town in the distance")
                pass

# Second Story - Finn
    if userInput== "2":
        storyText("you've began the long walk ahead of you")

if userInput == "2":
    storyText(f"{userName}, you have started your journey through the scenic route!"
          f"Let's begin the safe, prettier, but longer walk! \n")
    userInput = situationText("""Shall you grab a bag full of nuts and berries for the walk? there are always better snacks on the road to pick up
 Yes (1) | No (2) \n""")


    if userInput == "1":
        storyText("This can be helpful bringing your health up, just by a couple of points")
    if userInput == "2":
        storyText("You missed out on this delicious snack! You can always pick some up in the forest!")