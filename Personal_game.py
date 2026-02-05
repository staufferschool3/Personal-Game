#!/usr/bin/env python3
#  ^^ SHEBANG ^^


# Import library
import os
import time
import readchar

# username for later use
Usr_name = ""

# Clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# user yes or no input
def usr_answer(Answer):
    match Answer:
        case "yes" | "Yes" | "YES" | "y" | "Y":
            return "y"
        case "no" | "No" | "NO" | "n" | "N":
            return "n"
        case _:
            print(Answer, "is not a valid answer. Please use yes or no.")
            time.sleep(2)
            return "n"
        
# Clear screen and place name at top of screen
def usr_name():
    clear()
    print(f"\n\n{Usr_name}\n\n\n")

# Monster Creature Race function

# Main code
usr_name()
print("This is your story in the world of Alnir.\n\nIn this world you can fight, hunt, gather, build, create, and destroy the world as you please.")
key = readchar.readchar()
Confirmed = ""
while Confirmed != "y":
    usr_name()
    print("You will not be able to change your name later.\n")
    Usr_name = input("What is your name: ")
    Answer = input(f"Is your name {Usr_name}? y/n: ")
    Confirmed = usr_answer(Answer)
usr_name()
print("Welcome to to the world.")
key = readchar.readchar()
Confirmed = ""
while Confirmed not in ["y", "n"]:
    usr_name()
    Answer = input("Are you a Monster_Creature? y/n: ")
    Confirmed = usr_answer(Answer)
print(Answer)
