
# Imports
from Player import Player
import os
import readchar
from GameData import GameData

# Initializations
Player = Player()
GameData = GameData()

# Start of Story
os.system("cls" if os.name == "nt" else "clear")
print("\n\n\n")
print(f"Welcome. to the world of Alnar.", end='', flush=True)
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
while Player.input not in ["Alnari", "Monster Race"]:
    Player.hud()
    Player.input = input("Are you a 'Alnari' or a 'Monster Race': ").strip().title()

# Monster Race Selection
Looper = True
if Player.input == "Monster Race":
    while Looper:
        Player.hud()
        print(f"{list(GameData.player_races['Monster Race'].keys())}")
        #print("Are you a Orc, Slime, Dulahan, Spider, Oger, Goblin, Dryad,\n"
        #    "Werebeast(Has sub-race'incomplete'), Demon(Not recomended for first play-through, or Dragon(Not recomended for first play-through.)")
        Player.input = input("What are you: ").strip().title()
        match Player.input:
            case "Orc" | "Slime" | "Dulahan" | "Spider" | "Oger" | "Goblin" | "Dryad" | "Werebeast" | "Dragon" | "Demon":
                Race = Player.input
                Looper = False
            case _:
                print(f"{Player.input} is not a valid selection.")
                Looper = True

# Alnari Race Selection
elif Player.input == "Alnari":
    while True:
        Player.hud()
        print(f"{list(GameData.player_races['Alnari'].keys())}")
        Player.input = input("What are you: ").strip().title()
        if Player.input in GameData.player_races['Alnari']:
            Race = Player.input
            break
        else:
            print(f"{Player.race} is not a valid selection.", end="", flush=True)
            readchar.readchar()
Player.race = Race

# Skill Point Dist
Player.hud()
print("Time to use your skill points.", end="", flush=True)
readchar.readkey()
Player.skill_points += 100
Player.skill_dist()