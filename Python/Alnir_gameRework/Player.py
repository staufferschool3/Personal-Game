
# Imports
import os
import random
import readchar
import json
import sys

# Player class
class Player:
	def __init__(self, Name=None, Race=None):
		# Weapon/Armor/Offhand/Spells.json Files Import
		Base_path = os.path.dirname(__file__)
		Weapon_path = os.path.join(Base_path, 'data/Weapons.json')
		Armor_path = os.path.join(Base_path, 'data/Armor.json')
		Offhand_path = os.path.join(Base_path, 'data/Offhand.json')
		Spells_path = os.path.join(Base_path, 'data/Spells.json')
		with open(Weapon_path, 'r') as Weapon_file:
			self.Weapon_data = json.load(Weapon_file)
		with open(Armor_path, 'r') as Armor_file:
			self.Armor_data = json.load(Armor_file)
		with open(Offhand_path, 'r') as Offhand_file:
			self.Offhand_data = json.load(Offhand_file)
		with open(Spells_path, 'r') as Spells_file:
			self.Spells_data = json.load(Spells_file)

		# Player Things
		self.name = Name
		self.race = Race
		self.status = {
			"Vit": 1,
			"Str": 1,
			"Agi": 1,
			"Dex": 1,
			"Int": 0
		}

		self.health_multi = 67
		self.atk_multi = 8
		self.speed_multi = 5
		self.evasion_multi = 4
		self.handling_multi = 5
		self.mana_multi = 9

		self.stats = {
			"Health": round((self.status['Vit'] * 1.5) * self.health_multi),
			"Atk": round((self.status['Str'] * 1.5) * self.atk_multi), 
			"Speed": round((self.status['Agi'] * 1.5) * self.speed_multi),
			"Evasion": round((self.status['Agi'] * 1.5) * self.evasion_multi),
			"Handling": round((self.status['Dex'] * 1.5) * self.handling_multi),
			"Mana": round((self.status['Int'] * 1.5) * self.mana_multi)
		}

		self.hidden_stats = {
			"Charisma": random.randint(0, 100),
			"Global_distain": 0
		}

		self.status_ailments = {
			"Poison": 0,
			"Bleed": 0,
			"Tetanus": 0,
			"Paralysis": 0
		}

		self.level = 1
		self.exp = 0
		self.max_exp = 15
		self.skill_points = 0

		# Inventory
		self.inventory = {}
		self.equiped = {
			"Weapon": None,
			"Armor": None,
			"Offhand": None
		}

		# Spells
		self.knownspells = []

	# Refresh Stats
	def refresh_stats(self):
		# Level Handling
		if self.exp >= self.max_exp:
			self.exp -= self.max_exp
			self.level += 1
			self.max_exp = round(self.max_exp * 1.5)
		# Base stats from attributes
		self.stats["Health"] = round((self.status['Vit'] * 1.5) * self.health_multi)
		self.stats["Atk"] = round((self.status['Str'] * 1.5) * self.atk_multi)
		self.stats["Speed"] = round((self.status['Agi'] * 1.5) * self.speed_multi)
		self.stats["Evasion"] = round((self.status['Agi'] * 1.5) * self.evasion_multi)
		self.stats["Handling"] = round((self.status['Dex'] * 1.5) * self.handling_multi)
		self.stats["Mana"] = round((self.status['Int'] * 1.5) * self.mana_multi)
		# Test for death
		self.player_death()

		# Add bonuses from equipped items
		#if self.equiped["Weapon"]:
		    #item_data = WEAPONS.get(self.equiped["Weapon"])
		    #self.stats["Atk"] += item_data.get("atk_bonus", 0)

	# See Status
	def see_status(self):
		print(self.status['Vit'])
		print(self.status['Str'])
		print(self.status['Agi'])
		print(self.status['Dex'])
		print(self.status['Int'])

	# Skill Point Application
	def skill_dist(self):
		while self.skill_points > 0:
				self.hud()
				self.see_status()
				print("0) Exit\n1) Vit\n2) Str\n3) Agi\n4) Dex\n5) Int\n")
				Skill_select = input("Select Stat: ").strip().capitalize()
				match Skill_select.strip().capitalize():
					case 'Exit' | 0:
						break
					case 'Vit' | 1:
						self.status['Vit'] += 1
						self.skill_points - 1
						self.refresh_stats()
					case 'Str' | 2:
						self.status['Str'] += 1
						self.skill_points - 1
						self.refresh_stats()
					case 'Agi' | 3:
						self.status['Agi'] += 1
						self.skill_points - 1
						self.refresh_stats()
					case 'Dex' | 4:
						self.status['Dex'] += 1
						self.skill_points - 1
						self.refresh_stats()
						break
					case 'Int' | 5:
						self.status['Int'] += 1
						self.skill_points - 1
						self.refresh_stats()
						break
					case _:
						print("Not an expected input.")
						break
		else:
			print("No skill points avaliable", end="", flush=True)
			readchar.readkey()

	# Player Death
	def player_death(self):
		if self.stats['Health'] <= 0:
			self.hud()
			print("You Died.", end="", flush=True)
			readchar.readkey()
			sys.exit()

	# Player Hud
	def hud(self):
		self.refresh_stats()
		# Clear Screen
		os.system("cls" if os.name == "nt" else "clear")
		Hud = f"\n   --- Race: {self.race} | Name: {self.name} | HP: {self.stats['Health']} | Level: {self.level} | Exp: {self.exp}/{self.max_exp} ---\n"
		Hud_len = len(Hud)
		print("-"*Hud_len)
		print(Hud)
		print("-"*Hud_len)
		print("\n\n")

	# Spell Slots
	def spells_slots(self):
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

	# Weapons Draw
	def weapon_draw(self, Weapon):
		Result = self.Weapon_data.get(Weapon)
		print(f"\n'{Weapon}':", Result)
