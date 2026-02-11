import json

class GameData:
    def __init__(self):
        self.master_items = {}
        # Load all categories into one searchable dictionary
        for category in ["Weapons", "Armor", "Offhand", "Spells", "Enemies"]:
            with open(f"data{category}.json", "r") as f:
                self.master_items.update(json.load(f))
