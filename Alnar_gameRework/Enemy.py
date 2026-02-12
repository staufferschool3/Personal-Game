
# Imports
import json
import os

# Enemy Class
class Enemy:
    def __init__(self):
        Base_path = os.path.dirname(__file__)
        File_path = os.path.join(Base_path, 'data/Enemies.json')
        with open(File_path, 'r') as file:
            self.data = json.load(file)

    def draw(self, Monster):
        Result = self.data.get(Monster)
        print(f"\n'{Monster}':", Result)

Enemy_loader = Enemy()

os.system("cls" if os.name == "nt" else "clear")
Enemy_loader.draw(input("What monster to summon? : ").capitalize().strip())