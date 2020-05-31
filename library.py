# Leaf Bennett
# Created May 29, 2020
import random
import sys
import time
from termcolor import colored

class Hidden_Vally:
    hidden_Vally_Intro = "Welcome To Hidden Valley!"
    pubs = {"The Snailbox", "Hole In The Wall", "The Sky And The Ground", "Leafy's Pub"}
    shops = {"Weapon Shop", "Clothing Shop", "Farmers Market"}

class text:
    intro = ("""To begin the story of Hidden Valley we need to dive into whats wrong with this dangerous place. 
There have been people terrorizing the animals around the main village in the center of the valley.
The animals have begun to retaliate to protect their young. They have bashed the closest water supply so you 
need to make it to the closest stream which is 3 miles away. There are many different choices and routs to play,
good luck!
""")

    madeIntoTown = (f"{Hidden_Vally.hidden_Vally_Intro}")


def rng_percentage():
    x = random.randint(1, 100)
    return x

def slowWriteText(text):
    y = text
    speed_Of_Typing = 0.01
    for char in text:
        sys.stdout.write(char)
        time.sleep(speed_Of_Typing)

def loseHP(text):
    print(colored(text, "red", "on_white", attrs=['bold']))

def storyText(text):
    x = colored(text, "blue")
    slowWriteText(x)
def situationText(text):
    x = colored(text, "red")
    slowWriteText(x)
    y = input()
    return y




