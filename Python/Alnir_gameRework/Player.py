
# Imports
import os
import random
import readchar

# Player class
class Player:
	def __init__(self, Name=None, Race=None):
		self.name = Name
		self.race = Race
		self.status = {
			"Vit": 1,
			"Str": 1,
			"Agi": 1,
			"Dex": 1,
			"Int": 0
		}

		self.stats = {
			"Health": self.status['Vit'] * 100,
			"Atk": self.status['Str'] * 10, 
			"Speed": self.status['Agi'] * 5,
			"Evasion": self.status['Agi'] * 5,
			"Handling": self.status['Dex'] * 5,
			"Mana": self.status['Int'] * 10
		}

		self.hidden_stats = {
			"Charisma": random.randint(0, 100),
			"Distain": 0
		}

		self.status_ailments = {
			"Poison": 0,
			"Bleed": 0,
			"Tetnus": 0,
			"Paralysis": 0
		}

		self.level = 1
		self.exp = 0
		self.max_exp = 15
		self.skill_points = 0

	# Refresh Stats
	def refresh_stats(self):
		# Base stats from attributes
		self.stats["Health"] = self.status['Vit'] * 100
		self.stats["Atk"] = self.status['Str'] * 10

		# Add bonuses from equipped items
		#if self.equiped["Weapon"]:
		    #item_data = WEAPONS.get(self.equiped["Weapon"])
		    #self.stats["Atk"] += item_data.get("atk_bonus", 0)

		# Inventory
		self.inventory = []
		self.equiped = {
			"Weapon": None,
			"Armor": None,
			"Offhand": None
		}

		# Spells
		self.knownspells = []

	# Player Hud
	def hud(self):
		# Clear Screen
		os.system("cls" if os.name == "nt" else "clear")
		Hud = f"\n   --- Race: {self.race} | Name: {self.name} | HP: {self.stats['Health']} | Level: {self.level} | Exp: {self.exp}/{self.max_exp} ---\n"
		Hud_len = len(Hud)
		print("-"*Hud_len)
		print(Hud)
		print("-"*Hud_len)
		print("\n\n")

	# Spell Slots
	def spells(self):
		Key = readchar.readkey()
		match Key:
			case "1":
				self.knownspells
			case "2":
				self.knownspells
			case "3":
				self.knownspells
			case "4":
				self.knownspells
			case "5":
				self.knownspells
			case "6":
				self.knownspells
			case "7":
				self.knownspells
			case "8":
				self.knownspells
			case "9":
				self.knownspells
			case _:
				pass
	
	# Yes or No input
	def choice(self):
		match self.input.strip().title():
			case "Yes" | "Y":
				return "y"
			case "No" | "N":
				return "n"
			case _:
				print(f"{self.input} is not a valid answer. Please use yes or no.\nPress button.")
				readchar.readchar()

