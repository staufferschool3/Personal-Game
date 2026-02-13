import json
import os

class GameData:
    def __init__(self):
        self.master_items = {}

        # Load all categories into one searchable dictionary
        for category in ["Weapons", "Armor", "Offhand", "Spells", "Enemies", "Graveyard", "Player_race"]:
            Base_path = os.path.dirname(__file__)
            Game_data = os.path.join(Base_path, f'data/{category}.json')
            with open(Game_data, "r") as f:
                self.master_items.update(json.load(f))

        self.player_Monster = self.master_items['Monster Race']
        self.player_Alnari = self.master_items['Alnari']