#!/usr/bin/env python3
#  ^^ SHEBANG ^^


# Import library
import os
import time
import readchar
import random
import sys

# Variable for later use
Usr_level = 1
Usr_name = ""
Usr_race = ""
Usr_input = ""
Usr_attack = 0
Weapon = 0
Confirmed = ""
Max_exp = 15
Enemy = Usr_name

# User stat variables
Vit = random.randint(6, 12)
Dex = random.randint(3,5)
Agil = random.randint(3,5)
Str = random.randint(3,5)
Mp = random.randint(3,5)
Exp = 0

# Monster Stats
#   Slime
Slime_vit = 10

# Clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# User yes or no input
def usr_answer(Usr_input):
    match Usr_input:
        case "yes" | "Yes" | "YES" | "y" | "Y":
            return "y"
        case "no" | "No" | "NO" | "n" | "N":
            return "n"
        case _:
            print(Usr_input, "is not a valid answer. Please use yes or no.\nPress button.")
            key = readchar.readchar()
            return ""
        
# Clear screen and place name at top of screen
def usr_name():
    clear()
    print(f"\n\nRace: {Usr_race}  Name: {Usr_name}  Level: {Usr_level}  Exp: {Exp}\n\n\n")

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
    print("\n\nhelp--Shows all user commands.")
    print("status--Shows stat values. 'Stats are randomized.'")
    print("attack--Attacks the enemy.")
    print("pass_turn--Passes your turn.")
    print("submit--You submit to your death.")

# Attack
def attack():
    global Usr_attack
    Usr_attack = Str + Weapon

# Submit
def submit(Enemy):
    global Vit
    if Enemy == Usr_name:
        Vit = 0
        print("You couldn't ake it any more and succumbed to some wolves.")
        usr_died()
        key + readchar.readchar()
        sys.exit()
    else:
        Vit = 0
        print(f"{Enemy} took you for all you had.")
        key = readchar.readchar()
        usr_died()
        sys.exit()



# User Command function
def usr_commands(Usr_input):
    match Usr_input.lower():
        case "status" | "s":
            return show_stats()
        case "help" | "h":
            return show_commands()
        case "attack" | "a":
            return attack()
        case "submit":
            return submit(Enemy)
        case "pass_turn" | "p":
            return ""
        case _:
            return ""

# Monster Functions
def slime():
    global Enemy
    global Vit
    global Exp
    global Slime_vit
    global Usr_attack
    Enemy = "Slime"
    while Slime_vit > 0 and Vit > 0:
        Slam = random.randint(1, 3)
        usr_name()
        print("You encounterd a Slime.\n")
        Usr_input = input("What do you do: ")
        if Usr_input.lower() == "attack":
            usr_commands(Usr_input)
            Vit -= Slam
            Slime_vit -= Usr_attack
            print(f"Slime used slam.\nSlam did {Slam} damage.")
            time.sleep(1)
            print(f"You did {Usr_attack} in damage.")
            Usr_attack = 0
            key = readchar.readchar()
        elif Usr_input.lower() == "pass_turn":
            Vit -= Slam
            print(f"Slime used slam.\nSlam did {Slam} damage.")
            print(f"You did {Usr_attack} in damage.")
            key = readchar.readchar()
        else:
            usr_commands(Usr_input)
            key = readchar.readchar()
            pass
    Enemy = Usr_name
    if Vit < 1:
        usr_died()
        Slime_vit = 10
    else:
        Exp = Exp + 3
        Slime_vit = 10
        print(f"Congradulations you beat the slime.\n\nYou gained 3 Exp.")
        key = readchar.readchar()

# User Dies
def usr_died():
    print("You died.")
    key = readchar.readchar()

# Monster encounter List
#Monster_encounter = [Orc, Slime, Dulahan, Spider, Oger, Goblin, Werebeast, Dragon, Dryad, Rest]
#Rand_encounter = [8, 15, 5, 9, 5, 12, 3, 1, 2, 40]

# Main code
#Get username
usr_name()
print("This is your story in the world of Alnir.\n\nIn this world you can fight, hunt, gather, build, create, and destroy the world as you please.")
key = readchar.readchar()
Confirmed = ""
while Confirmed != "y":
    Usr_name = ""
    usr_name()
    print("You will not be able to change your name later.\n")
    Usr_name = input("What is your name: ")
    Usr_input = input(f"Is your name {Usr_name}? y/n: ")
    Confirmed = usr_answer(Usr_input)
usr_name()
print("Welcome to to the world.")
key = readchar.readchar()
Confirmed = ""
#Is user a Monster
while Confirmed not in ["y", "n"]:
    usr_name()
    Usr_input = input("Are you a Monster_Creature? y/n: ")
    Confirmed = usr_answer(Usr_input)
Looper = True
if Confirmed == "y":
    while Looper:
        usr_name()
        # Monster Creater Race Selection
        print("Are you a Orc, Slime, Dulahan, Spider, Oger, Goblin, Dryad,\n"
            "Werebeast(Has sub-race'incomplete'), or Dragon(Not recomended for first play-through.)")
        Usr_input = input("What are you: ").strip().capitalize()
        match Usr_input:
            case "Orc" | "Slime" | "Dulahan" | "Spider" | "Oger" | "Goblin" | "Dryad" | "Werebeast" | "Dragon":
                Usr_race = Usr_input
                Looper = False
            case _:
                print(f"{Usr_race} is not a valid selection.")
                Looper = True

elif Confirmed == "n":
    while Looper:
        usr_name()
        print("Sorry not implemented yet.\nContinuing with monsters.\n\n")
        #Race Selection -not implemented
        print("Are you a Orc, Slime, Dulahan, Spider, Oger, Goblin, Dryad,\n"
            "Werebeast(Has sub-race'incomplete'), or Dragon(Not recomended for first play-through.)")
        Usr_input = input("What are you: ").strip().capitalize()
        match Usr_input:
            case "Orc" | "slime" | "Dulahan" | "Spider" | "Oger" | "Goblin" | "Dryad" | "Werebeast" | "Dragon":
                Usr_race = Usr_input
                Looper = False
            case _:
                print(f"{Usr_race} is not a valid selection.")
                Looper = True
#Try commands
usr_name()
Usr_input = input("Great!! Now to look at see command list.\n\n Type 'help': ")
usr_commands(Usr_input)
key = readchar.readchar()

while Usr_input.lower() != "done":
    usr_name()
    Usr_input = input("Great!! Now test the commands to see what they do.\n"
        "Type 'Done' when finished: ")
    if Usr_input.lower() == "done":
        pass
    else:
        usr_commands(Usr_input)
        key = readchar.readchar()

usr_name()
print("Now let's try combat.")
key = readchar.readchar()

#First Combat
slime()

Confirmed = "y"
usr_name()
print("Thanks for playing the demo.")
while Confirmed == "y":
    Usr_input = input("Would you like to do first combat again with new stats? y/n: ")
    Confirmed = usr_answer(Usr_input)
    
    #Restart combat
    if Confirmed == "y":
        Vit = random.randint(6, 12)
        Dex = random.randint(3,5)
        Agil = random.randint(3,5)
        Str = random.randint(3,5)
        Mp = random.randint(3,5)

        slime()
    elif Confirmed == "n":
        break   

#End of totorial.
print("")
