
# Imports
from Player import Player
import os
import readchar

# Player Initialization
Player = Player()
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
while Player.input not in ["Alnari", "Monster_Creature"]:
    Player.hud()
    Player.input = input("Are you a 'Alnari' or a 'Monster_Creature': ").strip().title()
# Monster Race Selection
Looper = True
if Player.input == "Monster_Creature":
    while Looper:
        Player.hud()
        print("Are you a Orc, Slime, Dulahan, Spider, Oger, Goblin, Dryad,\n"
            "Werebeast(Has sub-race'incomplete'), Demon(Not recomended for first play-through, or Dragon(Not recomended for first play-through.)")
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
    while Looper:
        Player.hud()
        print("Are you a Human, Wood Elf, Dwarf, High Elf,\n"
            "Beastman(Has sub-race'incomplete'), or Angel(Not recomended for first play-through.)")
        Player.input = input("What are you: ").strip().title()
        match Player.input:
            case "Human" | "Wood Elf" | "Dwarf" | "High Elf" | "Beastman" | "Halfling" | "Angel":
                Race = Player.input
                Looper = False
            case _:
                print(f"{Player.race} is not a valid selection.")
                readchar.readchar()
                Looper = True
Player.race = Race
Player.hud()