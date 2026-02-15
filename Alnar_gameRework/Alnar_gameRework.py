#!/usr/bin/env python3

# Imports
from Player import Player
import os
import readchar
from GameData import GameData
import time

# Initializations
Player = Player()
GameData = GameData()

# Start of Story
os.system("cls" if os.name == "nt" else "clear")
print("\n\n\n")
print(f"          Alnar\n     World of wonder\n\n     Enter to start", end='', flush=True)
readchar.readkey()

# Get Player Name
Confirmed = None
while Confirmed != "y":
    Player.hud()
    print("You will not be able to change your name later.\n")
    Name = input("What is your name: ").capitalize().strip()
    Player.input = input(f"Is your name {Name}? y/n: ")
    Confirmed = Player.choice()
Player.name = Name

# Get Player Race
Player.hud()
while Player.input not in ["Alnari", "Monster"]:
    Player.hud()
    Player.input = input("Are you a 'Alnari' or a 'Monster': ").strip().title()
    if Player.input in ["Monster", "Alnari"]:
        Player.faction = Player.input

# Monster Race Selection
Looper = True
if Player.input == "Monster":
    while True:
        Player.hud()
        print(f"{list(GameData.player_Monster.keys())}")
        Player.input = input("What are you: ").strip().title()
        if Player.input in GameData.player_Monster:
            Race = Player.input
            break
        else:
            print(f"{Player.race} is not a valid selection.", end="", flush=True)
            readchar.readchar()

# Alnari Race Selection
elif Player.input == "Alnari":
    while True:
        Player.hud()
        print(f"{list(GameData.player_Alnari.keys())}")
        Player.input = input("What are you: ").strip().title()
        if Player.input in GameData.player_Alnari:
            Race = Player.input
            break
        else:
            print(f"{Player.race} is not a valid selection.", end="", flush=True)
            readchar.readchar()
Player.race = Race
Player.stat_mod()

# Skill Point Dist
Player.hud()
print("Time to use your skill points.", end="", flush=True)
readchar.readkey()
Player.skill_points += 50
Player.skill_dist()
Player.hud()
print("Welcome to the world of Alnar.", end="", flush=True)
readchar.readkey()
