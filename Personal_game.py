#!/usr/bin/env python3
#  ^^ SHEBANG ^^


# Import library
import os
import time
import readchar
import random
import sys

# Player class system
class Player:
    def __init__(self, User_name, User_race):
        self.name = User_name
        self.race = User_race
        self.level = 1
        self.Exp = 0
        self.Max_exp = 15

        #Player stats
        self.Vit = random.randint(6, 12)
        self.Dex = random.randint(3,5)
        self.Agil = random.randint(3,5)
        self.Str = random.randint(3,5)
        self.Mp = random.randint(3,5)

# Variable for later use
User_name = ""
User_race = ""
User_input = ""
User_attack = 0
Weapon = 0
Confirmed = ""
Enemy = User_name

# Clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Clear screen and place name at top of screen
def user_name():
    clear()
    print(f"\n\nRace: {User_race}  Name: {User_name}  Level: {User_level}  Exp: {Exp}\n\n\n")

# User yes or no input
def user_answer(User_input):
    match User_input:
        case "yes" | "Yes" | "YES" | "y" | "Y":
            return "y"
        case "no" | "No" | "NO" | "n" | "N":
            return "n"
        case _:
            print(User_input, "is not a valid answer. Please use yes or no.\nPress button.")
            key = readchar.readchar()
            return ""

# User Dies
def user_died():
    print("You died.")
    key = readchar.readchar()

# User Command function
def user_commands(User_input):
    match User_input.lower():
        case "help" | "h":
            return help()
        case "status" | "s":
            return status()
        case "attack" | "a":
            return attack()
        case "submit":
            return submit(Enemy)
        case "passturn" | "p":
            return ""
        case _:
            return ""

# Help function
def help():
    print("\n\nhelp--Shows all user commands.")
    print("status--Shows stat values. 'Stats are randomized.'")
    print("attack--Attacks the enemy.")
    print("defend--Defends against enemy.")
    print("submit--You submit to your death.")
    print("passturn--Passes your turn.")

# Show stats function
def status():
    print(f"\n--- {User_name}'s Current Stats ---")
    print(f"Vitality:     {Vit}")
    print(f"Dexterity:    {Dex}")
    print(f"Agility:      {Agil}")
    print(f"Strength:     {Str}")
    print(f"Mana:         {Mp}")
    print("---------------------------------")
    return "" # Return empty so 'None' doesn't print

# Attack
def attack():
    global User_attack
    User_attack = Str + Weapon

# Submit
def submit(Enemy):
    global Vit
    if Enemy == User_name:
        Vit = 0
        print("You couldn't ake it any more and succumbed to some wolves.")
        user_died()
        key = readchar.readchar()
        sys.exit()
    else:
        Vit = 0
        print(f"{Enemy} took you for all you had.")
        key = readchar.readchar()
        user_died()
        sys.exit()

# Monster encounter List
#Monster_encounter = [Orc, Slime, Dulahan, Spider, Oger, Goblin, Werebeast, Dragon, Dryad, Rest]
#Rand_encounter = [8, 15, 5, 9, 5, 12, 3, 1, 2, 40]

# Enemy class
class ClassEnemy:
    def __init__(self, Enemy_name, Enemy_race, Enemy_attackName, Enemy_vit, Enemy_str):
        self.enemy_name = Enemy_name
        self.enemy_race = Enemy_race
        self.enemy_attackName = Enemy_attackName
        self.enemy_vit = Enemy_vit
        self.enemy_str = Enemy_str

    # Combat phase
    def combat(self):
        global Vit
        global Exp
        global User_attack
        global Enemy
        global User_name
        Enemy = self.enemy_name
        print(f"{self.enemy_name} {self.enemy_race} has approched.")
        while self.enemy_vit > 0 and Vit > 0:
            user_name()
            print(f"{self.enemy_name} {self.enemy_race}")
            User_input = input("What do you do: ")
            if User_input.lower() == "attack":
                user_commands(User_input)
                Vit -= self.enemy_str
                self.enemy_vit -= User_attack
                print(f"{self.enemy_name}{self.enemy_race} used {self.enemy_attackName}.")
                time.sleep(1)
                print(f"{self.enemy_attackName} did {self.enemy_str} damage.")
                time.sleep(1)
                print(f"You did {User_attack} in damage.")
                User_attack = 0
                key = readchar.readchar()
            elif User_input.lower() == "pass_turn":
                Vit -= self.enemy_str
                print(f"{self.enemy_name}{self.enemy_race} used {self.enemy_attackName}.\n{self.enemy_attackName} did {self.enemy_str} damage.")
                print(f"You did {User_attack} in damage.")
                key = readchar.readchar()
            else:
                user_commands(User_input)
                key = readchar.readchar()
                pass
        Enemy = User_name
        if Vit < 1:
            user_died()
        else:
            time.sleep(1)
            Exp = Exp + 3
            print(f"Congradulations you beat the {self.enemy_name} {self.enemy_race}.\n\nYou gained 3 Exp.")
            key = readchar.readchar()

# Monster Functions
def starter_slime():
    Slime = ClassEnemy("Starter", "Slime", "Slam", 10, random.randint(1, 3))
    Slime.combat()

# ---------------------Main code-------------------------
# Get username
user_name()
print("This is your story in the world of Alnir.\n\nIn this world you can fight, hunt, gather, build, create, and destroy the world as you please.")
key = readchar.readchar()
Confirmed = ""
while Confirmed != "y":
    User_name = ""
    user_name()
    print("You will not be able to change your name later.\n")
    User_name = input("What is your name: ")
    User_input = input(f"Is your name {User_name}? y/n: ")
    Confirmed = user_answer(User_input)
user_name()
print("Welcome to to the world.")
key = readchar.readchar()
Confirmed = ""
# Is user a Monster
while Confirmed not in ["y", "n"]:
    user_name()
    User_input = input("Are you a Monster_Creature? y/n: ")
    Confirmed = user_answer(User_input)
Looper = True
if Confirmed == "y":
    while Looper:
        user_name()
        # Monster Creater Race Selection
        print("Are you a Orc, Slime, Dulahan, Spider, Oger, Goblin, Dryad,\n"
            "Werebeast(Has sub-race'incomplete'), or Dragon(Not recomended for first play-through.)")
        User_input = input("What are you: ").strip().capitalize()
        match User_input:
            case "Orc" | "Slime" | "Dulahan" | "Spider" | "Oger" | "Goblin" | "Dryad" | "Werebeast" | "Dragon":
                User_race = User_input
                Looper = False
            case _:
                print(f"{User_race} is not a valid selection.")
                Looper = True

elif Confirmed == "n":
    while Looper:
        user_name()
        print("Sorry not implemented yet.\nContinuing with monsters.\n\n")
        # Race Selection -not implemented
        print("Are you a Orc, Slime, Dulahan, Spider, Oger, Goblin, Dryad,\n"
            "Werebeast(Has sub-race'incomplete'), or Dragon(Not recomended for first play-through.)")
        User_input = input("What are you: ").strip().capitalize()
        match User_input:
            case "Orc" | "Slime" | "Dulahan" | "Spider" | "Oger" | "Goblin" | "Dryad" | "Werebeast" | "Dragon":
                User_race = User_input
                Looper = False
            case _:
                print(f"{User_race} is not a valid selection.")
                Looper = True
# Try commands
user_name()
User_input = input("Great!! Now to look at see command list.\n\n Type 'help': ")
user_commands(User_input)
key = readchar.readchar()

while User_input.lower() != "done":
    user_name()
    User_input = input("Great!! Now test the commands to see what they do.\n"
        "Type 'Done' when finished: ")
    if User_input.lower() == "done":
        pass
    else:
        user_commands(User_input)
        key = readchar.readchar()

user_name()
print("Now let's try combat.")
key = readchar.readchar()

# First Combat
starter_slime()

Confirmed = "y"
user_name()
print("Thanks for playing the demo.")
while Confirmed == "y":
    User_input = input("Would you like to do first combat again with new stats? y/n: ")
    Confirmed = user_answer(User_input)
    
    # Restart combat
    if Confirmed == "y":
        Vit = random.randint(6, 12)
        Dex = random.randint(3,5)
        Agil = random.randint(3,5)
        Str = random.randint(3,5)
        Mp = random.randint(3,5)

        starter_slime()
    elif Confirmed == "n":
        break   

# End of totorial.
print("")
