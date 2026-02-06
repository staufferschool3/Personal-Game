#!/usr/bin/env python3
#  ^^ SHEBANG ^^


# Import library
import os
import time
import readchar
import random

# Variable for later use
Usr_name = ""
Usr_race = ""
Usr_input = ""

# User stat variables
Vit = 0
Dex = 0
Agil = 0
Str = 0
Mp = 0

# Monster Stats
#   Slime
Slime_Vit = 10

# Clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# User yes or no input
def usr_answer(Answer):
    match Answer:
        case "yes" | "Yes" | "YES" | "y" | "Y":
            return "y"
        case "no" | "No" | "NO" | "n" | "N":
            return "n"
        case _:
            print(Answer, "is not a valid answer. Please use yes or no.\nPress button.")
            key = readchar.readchar()
            return "n"
        
# Clear screen and place name at top of screen
def usr_name():
    clear()
    print(f"\n\nRace: {Usr_race}  Name: {Usr_name}\n\n\n")

# Show stats function
def show_stats():
    print(f"\n--- {Usr_name}'s Current Stats ---")
    print(f"Vitality:     {Vit}")
    print(f"Dexterity:    {Dex}")
    print(f"Agility:      {Agil}")
    print(f"Strength:     {Str}")
    print(f"Mana:         {Mp}")
    print("---------------------------------")
    return "" # Return empty so 'None' doesn't print

# Help function
def show_commands():
    print("show_commands--Shows all user commands.")
    print("show_stats--Shows stat values.")

# User Command function
def usr_commands(Usr_input):
    match Usr_input.lower():
        case "show_stats":
            return show_stats()
        case "show_commands":
            return show_commands()
        case _:
            return ""

# Monster Functions
def Slime():
    global Vit
    while Slime_Vit > 0:
        Slam = Vit - 2

# Monster List
#Monster = [Orc, Slime, Dulahan, Spider, Oger, Goblin, Werebeast, Dragon, Dryad]

# Main code
usr_name()
print("This is your story in the world of Alnir.\n\nIn this world you can fight, hunt, gather, build, create, and destroy the world as you please.")
key = readchar.readchar()
Confirmed = ""
while Confirmed != "y":
    Usr_name = ""
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
Looper = True
if Confirmed == "y":
    while Looper:
        Usr_race = ""
        usr_name()
        # Monster Creater Race Selection
        print("Are you a Orc, Slime, Dulahan, Spider, Oger, Goblin, Dryad,\n"
            "Werebeast(Has sub-race'incomplete'), or Dragon(Not recomended for first play-through.)")
        Usr_race = input("What are you: ")
        match Usr_race:
            case "Orc" | "orc":
                Usr_race = "Orc"
                Looper = False
            case "Slime" | "slime":
                Usr_race = "Slime"
                Looper = False
            case "Dulahan" |"dulahan":
                Usr_race = "Dulahan"
                Looper = False
            case "Spider" | "spider":
                Usr_race = "Spider"
                Looper = False
            case "Oger" | "oger":
                Usr_race = "Oger"
                Looper = False
            case "Werebeast" | "werebeast":
                Usr_race = "Werebeast"
                Looper = False
            case "Goblin" | "goblin":
                Usr_race = "Goblin"
                Looper = False
            case "Dragon" | "dragon":
                Usr_race = "Dragon"
                Looper = False
            case _:
                print(f"{Usr_race} is not a valid selection.")
                Looper = True

usr_name()
Usr_input = input("Great!! Now to look at see command list.\n\n Type 'show_commands': ")
usr_commands(Usr_input)
key = readchar.readchar()

while Usr_input != "Done":
    usr_name()
    Usr_input = input("Great!! Now test the commands to see what they do.\n"
        "Type 'Done' when finished: ")
    if Usr_input == "Done":
        pass
    else:
        usr_commands(Usr_input)
        key = readchar.readchar()

usr_name()
print("Now let's try combat.")
key = readchar.readchar()

usr_name()
key = readchar.readchar()
