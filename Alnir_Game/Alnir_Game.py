#!/usr/bin/env python3
#  ^^ SHEBANG ^^


# Import library
import os
import time
import readchar
import random
import sys
from Alnir_assets.Equipment import EquipmentMan

# Instancing EquipmentMan
Equipment = EquipmentMan()

# Player class system
class Player:
    # Player info
    def __init__(self, Equipment, Name=None, Race=None):
        self.name = Name
        self.race = Race
        self.level = 1
        self.exp = 0
        self.max_exp = 15
        self.skill_points = 0
        self.atk_power = 0
        self.equiped = Equipment.weapon

        # Player stats
        self.vit = 100
        self.dex = 5
        self.agi = 5
        self.str = 5
        self.man = 5

    # User Dies
    def died(self):
        print("\nYou died.")
        Key = readchar.readchar()

    # Player takes damage
    def damage(self, Current_enemy):
        self.vit -= Current_enemy.str
        if self.vit <= 0:
            self.vit = 0
            self.died()

    # Player leveling
    def check_level(self):
        if self.exp >= self.max_exp:
            self.level += 1
            self.exp -= self.max_exp
            self.max_exp = int(self.max_exp * 1.5)
            self.skill_points += 3
            print(f"Level Up! You are now {self.level}")

    # User yes or no input
    def answer(self):
        match self.input.strip():
            case "yes" | "Yes" | "YES" | "y" | "Y":
                return "y"
            case "no" | "No" | "NO" | "n" | "N":
                return "n"
            case _:
                print(f"{self.input} is not a valid answer. Please use yes or no.\nPress button.")
                Key = readchar.readchar()

    # User Command function
    def commands(self, Current_enemy=None):
        match self.input.lower().strip():
            case "help" | "h":
                return self.help()
            case "status" | "s":
                return self.status()
            case "attack" | "a":
                return self.attack(Current_enemy)
            case "submit":
                return self.submit(Current_enemy)
            case "pass" | "p":
                self.passturn(Current_enemy)
                return "pass"
            case _:
                return None

    # Help function
    def help(self):
        print("\n\nhelp--Shows all user commands.")
        print("status--Shows stat values. 'Starting stats are randomized.'")
        print("attack--Attacks the enemy.")
        #print("defend--Defends against enemy.")
        print("submit--You submit to your death.")
        print("pass--Passes your turn.")
        Key = readchar.readchar()

    # Show stats function
    def status(self):
        print(f"\n--- {self.name}'s Current Stats ---")
        print(f"Vitality:     {self.vit}")
        print(f"Dexterity:    {self.dex}")
        print(f"Agility:      {self.agi}")
        print(f"Strength:     {self.str}")
        print(f"Mana:         {self.man}")
        print("---------------------------------")
        Key = readchar.readchar()

    # Attack
    def attack(self, Current_enemy):
        self.atk_power = self.str #+ self.equiped
        if Current_enemy == None:
            if self.equiped == None:
                print(f"\nYou swing your hands at the air like a moron.")
                Key = readchar.readchar()
            else:
                print(f"\nYou swing your {self.equiped} like a moron at the air.")

    # Submit
    def submit(self, Current_enemy):
        self.vit
        if Current_enemy == None:
            self.vit = 0
            print("\nYou couldn't take it any more and succumbed to some wolves.")
            time.sleep(1)
            self.died()
            sys.exit()
        else:
            self.vit = 0
            print(f"\n{Current_enemy.name} {Current_enemy.race} took you for all you had.")
            time.sleep(1)
            self.died()
            sys.exit()

    # Pass
    def passturn(self, Current_enemy):
        if Current_enemy == None:
            print("\nYou wait for a cloud to pass you by.")
            Key = readchar.readchar()
        return "pass"

    # Clear screen and place name at top of screen
    def hud(self):
        # Clear screen
        os.system("cls" if os.name == "nt" else "clear")
        #
        print(f"\n\nRace: {self.race}  Name: {self.name}  Level: {self.level}  Exp: {self.exp}\n\n\n")

# Enemy class
class Enemy:
    def __init__(self, Enemy_name, Enemy_race, Enemy_attackName, Enemy_vit, Enemy_str):
        self.name = Enemy_name
        self.race = Enemy_race
        self.attackName = Enemy_attackName
        self.vit = Enemy_vit
        self.str = Enemy_str

    # Combat phase
    def combat(self, Player):
        Enemy = self.name
        print(f"{self.name} {self.race} has approched.")
        Key = readchar.readchar()
        while self.vit > 0 and Player.vit > 0:
            Player.hud()
            print(f"{self.name} {self.race}")
            Player.input = input("What do you do: ")
            Result = Player.commands(self)
            if Player.input.lower() == "attack":
                Player.vit -= self.str
                self.vit -= Player.atk_power
                print(f"\n{self.name}{self.race} used {self.attackName}.")
                time.sleep(1)
                print(f"{self.attackName} did {self.str} damage.")
                time.sleep(1)
                print(f"You did {Player.atk_power} damage.")
                Player.atk_power = 0
                Key = readchar.readchar()
            elif Result == "pass":
                Player.vit -= self.str
                print(f"\n{self.name}{self.race} used {self.attackName}.")
                time.sleep(1)
                print(f"{self.attackName} did {self.str} damage.")
                time.sleep(1)
                print(f"You did {Player.atk_power} damage.")
                Key = readchar.readchar()
            else:
                pass
        if Player.vit < 1:
            Player.died()
        else:
            time.sleep(1)
            Player.exp += 3
            print(f"Congradulations you beat the {self.name} {self.race}.\n\nYou gained 3 Exp.")
            Key = readchar.readchar()

# Monster encounter List
#Monster_encounter = [Orc, Slime, Dulahan, Spider, Oger, Goblin, Werebeast, Dragon, Dryad, Rest]
#Encounter_rand = [8, 15, 5, 9, 5, 12, 3, 1, 2, 40]

# Monster Functions
def starter_slime(User):
    Slime = Enemy("Starter", "Slime", "Slam", 10, random.randint(1, 3))
    Slime.combat(User)

# ---------------------Main code-------------------------
# Player instance
User = Player(Equipment)

# Get username
User.hud()
print("This is your story in the world of Alnir.\n\nIn this world you can fight, hunt, gather, build, create, and destroy the world as you please.")
Key = readchar.readchar()
Confirmed = None
while Confirmed != "y":
    User.hud()
    print("You will not be able to change your name later.\n")
    Name = input("What is your name: ")
    User.name = Name.capitalize().strip()
    User.input = input(f"Is your name {User.name}? y/n: ")
    Confirmed = User.answer()
User.hud()
print("Welcome to to the world.")
Key = readchar.readchar()
Confirmed = None
# Is user a Monster
while Confirmed not in ["y", "n"]:
    User.hud()
    User.input = input("Are you a Monster_Creature? y/n: ")
    Confirmed = User.answer()
Looper = True
if Confirmed == "y":
    while Looper:
        User.hud()
        # Monster Creater Race Selection
        print("Are you a Orc, Slime, Dulahan, Spider, Oger, Goblin, Dryad,\n"
            "Werebeast(Has sub-race'incomplete'), or Dragon(Not recomended for first play-through.)")
        User.input = input("What are you: ").strip().capitalize()
        match User.input:
            case "Orc" | "Slime" | "Dulahan" | "Spider" | "Oger" | "Goblin" | "Dryad" | "Werebeast" | "Dragon":
                User.race = User.input
                Looper = False
            case _:
                print(f"{User.input} is not a valid selection.")
                Looper = True

elif Confirmed == "n":
    while Looper:
        User.hud()
        print("Sorry not implemented yet.\nContinuing with monsters.\n\n")
        # Race Selection -not implemented
        print("Are you a Orc, Slime, Dulahan, Spider, Oger, Goblin, Dryad,\n"
            "Werebeast(Has sub-race'incomplete'), or Dragon(Not recomended for first play-through.)")
        User.input = input("What are you: ").strip().capitalize()
        match User.input:
            case "Orc" | "Slime" | "Dulahan" | "Spider" | "Oger" | "Goblin" | "Dryad" | "Werebeast" | "Dragon":
                User.race = User.input
                Looper = False
            case _:
                print(f"{User.race} is not a valid selection.")
                Looper = True
# Try commands
User.hud()
User.input = input("Great!! Now to look at see command list.\n\n Type 'help': ")
User.commands()

while User.input.lower() != "done":
    User.hud()
    User.input = input("Great!! Now test the commands to see what they do.\n"
        "Type 'Done' when finished: ")
    if User.input.lower() == "done":
        pass
    else:
        User.commands()

User.hud()
print("Now let's try combat.")
Key = readchar.readchar()

# First Combat
starter_slime(User)

Confirmed = "y"
User.hud()
print("Thanks for playing the demo.")
while Confirmed == "y":
    User.input = input("Would you like to do first combat again with new stats? y/n: ")
    Confirmed = User.answer()
    
    # Restart combat
    if Confirmed == "y":
        User.vit = random.randint(6, 12)
        User.dex = random.randint(3,5)
        User.agi = random.randint(3,5)
        User.str = random.randint(3,5)
        User.man = random.randint(3,5)

        starter_slime(User)
    elif Confirmed == "n":
        break   

# End of totorial.