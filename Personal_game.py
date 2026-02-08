#!/usr/bin/env python3
#  ^^ SHEBANG ^^


# Import library
import os
import time
import readchar
import random
import sys

# Variable for later use
Weapon = 0
Confirmed = ""
Enemy = Player.name

# Player class system
class Player:
    # Player info
    def __init__(self, Name, Race):
        self.name = Name
        self.race = Race
        self.level = 1
        self.exp = 0
        self.max_exp = 15
        self.skill_points = 0
        self.input = ""

        # Player stats
        self.vit = random.randint(6, 12)
        self.dex = random.randint(3,5)
        self.agi = random.randint(3,5)
        self.str = random.randint(3,5)
        self.man = random.randint(3,5)

    # User Dies
    def died(self):
        print("You died.")
        key = readchar.readchar()

    # Player takes damage
    def damage(self):
        self.vit -= Enemy_str
        if self.vit <= 0:
            self.vit = 0
            self.died()

    # Player leveling
    def check_level(self):
        if self.exp >= self.max_exp:
            self.level += 1
            self.exp -= self.max_exp
            self.max_exp *= 1.5
            self.skill_points += 3
            print(f"Level Up! You are now {self.level}")

    # User yes or no input
    def answer(self.input):
        match self.input:
            case "yes" | "Yes" | "YES" | "y" | "Y":
                return "y"
            case "no" | "No" | "NO" | "n" | "N":
                return "n"
            case _:
                print(f"{self.input} is not a valid answer. Please use yes or no.\nPress button.")
                key = readchar.readchar()
                return ""

    # User Command function
    def commands(self.input):
        match self.input.lower():
            case "help" | "h":
                return self.help()
            case "status" | "s":
                return self.status()
            case "attack" | "a":
                return self.attack()
            case "submit":
                return self.submit(Enemy)
            case "passturn" | "p":
                return ""
            case _:
                return ""

    # Help function
    def help(self):
        print("\n\nhelp--Shows all user commands.")
        print("status--Shows stat values. 'Stats are randomized.'")
        print("attack--Attacks the enemy.")
        print("defend--Defends against enemy.")
        print("submit--You submit to your death.")
        print("passturn--Passes your turn.")

    # Show stats function
    def status(self):
        print(f"\n--- {self.name}'s Current Stats ---")
        print(f"Vitality:     {self.vit}")
        print(f"Dexterity:    {self.dex}")
        print(f"Agility:      {self.agi}")
        print(f"Strength:     {self.str}")
        print(f"Mana:         {self.man}")
        print("---------------------------------")
        return ""

    # Attack
    def attack(self.str):
        self.attack
        self.attack = self.str + Weapon

    # Submit
    def submit(ClassEnemy):
        self.vit
        if Enemy == self.name:
            self.vit = 0
            print("You couldn't ake it any more and succumbed to some wolves.")
            self.died()
            key = readchar.readchar()
            sys.exit()
        else:
            Vit = 0
            print(f"{Enemy} took you for all you had.")
            key = readchar.readchar()
            self.died()
            sys.exit()

    # Clear screen and place name at top of screen
    def hud(self):
        # Clear screen
        def clear():
            os.system("cls" if os.name == "nt" else "clear")
        clear()
        print(f"\n\nRace: {self.race}  Name: {self.name}  Level: {self.level}  Exp: {self.exp}\n\n\n")

# Enemy class
class ClassEnemy:
    def __init__(self, Enemy_name, Enemy_race, Enemy_attackName, Enemy_vit, Enemy_str):
        self.enemy_name = Enemy_name
        self.enemy_race = Enemy_race
        self.enemy_attackName = Enemy_attackName
        self.enemy_vit = Enemy_vit
        self.enemy_str = Enemy_str

    # Combat phase
    def combat(self, Player):
        Enemy = self.enemy_name
        print(f"{self.enemy_name} {self.enemy_race} has approched.")
        while self.enemy_vit > 0 and Vit > 0:
            user_name()
            print(f"{self.enemy_name} {self.enemy_race}")
            Player.input = input("What do you do: ")
            if Player.input.lower() == "attack":
                Player.commands(Player.input)
                Player.vit -= self.enemy_str
                self.enemy_vit -= Player.attack
                print(f"{self.enemy_name}{self.enemy_race} used {self.enemy_attackName}.")
                time.sleep(1)
                print(f"{self.enemy_attackName} did {self.enemy_str} damage.")
                time.sleep(1)
                print(f"You did {Player.attack} in damage.")
                Player.attack = 0
                key = readchar.readchar()
            elif Player.input.lower() == "pass_turn":
                Player.vit -= self.enemy_str
                print(f"{self.enemy_name}{self.enemy_race} used {self.enemy_attackName}.\n{self.enemy_attackName} did {self.enemy_str} damage.")
                print(f"You did {Player.attack} in damage.")
                key = readchar.readchar()
            else:
                Player.commands(Player.input)
                key = readchar.readchar()
                pass
        Enemy = Player.name
        if Player.vit < 1:
            Player.died()
        else:
            time.sleep(1)
            Exp = Exp + 3
            print(f"Congradulations you beat the {self.enemy_name} {self.enemy_race}.\n\nYou gained 3 Exp.")
            key = readchar.readchar()

# Monster encounter List
#Monster_encounter = [Orc, Slime, Dulahan, Spider, Oger, Goblin, Werebeast, Dragon, Dryad, Rest]
#Rand_encounter = [8, 15, 5, 9, 5, 12, 3, 1, 2, 40]

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
