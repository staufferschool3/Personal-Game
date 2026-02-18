# Imports
from GameData import GameData
from Player import Player

# Iitialize
GameData = GameData()
Player = Player()

class Map():
    def __init__(self):
        self.map = GameData.map
        self.travel = GameData.map['World Travel']

    def spawn_location(self, Player):
        Alnari_spawns = self.map['Spawn_location']['Alnari']
        Monster_spawns = self.map['Spawn_location']['Monsters']
        if Player.race in Alnari_spawns:
            self.player_spawn = Alnari_spawns[f'{Player.race}']
        elif Player.race in Monster_spawns:
            self.player_spawn = Monster_spawns[f'{Player.race}']
        else:
            return False
        self.location = self.player_spawn

    def map_movement(self):
        Destination = input("Where would you like to go: ")
        if Destination in self.map['World Map']:
            if self.location in self.travel:
                if Destination in self.travel[f'{self.location}']:
                        self.location = Destination