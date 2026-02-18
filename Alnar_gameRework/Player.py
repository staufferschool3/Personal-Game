
# Imports
import os
import random
import readchar
import json
import sys
from GameData import GameData
import time

# Initializations
GameData = GameData()

# Player class
class Player:
	def __init__(self, Name=None, Race=None, Faction=None):
		pass

		# Player Things
		self.name = Name
		self.race = Race
		self.faction = Faction
		self.status = {
			"Vit": 1,
			"Str": 1,
			"Agi": 1,
			"Dex": 1,
			"Int": 0
		}

		self.level = 1
		self.exp = 0
		self.max_exp = 15
		self.skill_points = 0

		# Basic Starting val
		self.health_multi = 1
		self.atk_multi = 1
		self.speed_multi = 1
		self.evasion_multi = 1
		self.handling_multi = 1
		self.mana_multi = 1

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

		# Inventory
		self.inventory = {}
		self.equiped = {
			"Weapon": None,
			"Armor": None,
			"Offhand": None
		}

		# Spells
		self.knownspells = []

	# Stat modifires
	def stat_mod(self):
		if self.faction == "Monster":
			GameData.player_health = GameData.player_Monster[f'{self.race}']
			GameData.player_atk = GameData.player_Monster[f'{self.race}']
			GameData.player_speed = GameData.player_Monster[f'{self.race}']
			GameData.player_evasion = GameData.player_Monster[f'{self.race}']
			GameData.player_handling = GameData.player_Monster[f'{self.race}']
			GameData.player_mana = GameData.player_Monster[f'{self.race}']

			self.health_multi = GameData.player_health['Health_multi']
			self.atk_multi = GameData.player_atk['Atk_multi']
			self.speed_multi = GameData.player_speed['Speed_multi']
			self.evasion_multi = GameData.player_evasion['Evasion_multi']
			self.handling_multi = GameData.player_handling['Handling_multi']
			self.mana_multi = GameData.player_mana['Mana_multi']

		elif self.faction == "Alnari":
			GameData.player_health = GameData.player_Alnari[f'{self.race}']
			GameData.player_atk = GameData.player_Alnari[f'{self.race}']
			GameData.player_speed = GameData.player_Alnari[f'{self.race}']
			GameData.player_evasion = GameData.player_Alnari[f'{self.race}']
			GameData.player_handling = GameData.player_Alnari[f'{self.race}']
			GameData.player_mana = GameData.player_Alnari[f'{self.race}']

			self.health_multi = GameData.player_health['Health_multi']
			self.atk_multi = GameData.player_atk['Atk_multi']
			self.speed_multi = GameData.player_speed['Speed_multi']
			self.evasion_multi = GameData.player_evasion['Evasion_multi']
			self.handling_multi = GameData.player_handling['Handling_multi']
			self.mana_multi = GameData.player_mana['Mana_multi']

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
		print("Vit:", self.status['Vit'])
		print("Str:", self.status['Str'])
		print("Agi:", self.status['Agi'])
		print("Dex:", self.status['Dex'])
		print("Int:", self.status['Int'])

	# Skill Point Application
	def skill_dist(self):
		while self.skill_points > 0:
				self.hud()
				print(f"Skill Points: {self.skill_points}")
				self.see_status()
				print("\n\n0) Exit\n1) Vit\n2) Str\n3) Agi\n4) Dex\n5) Int\n")
				Skill_select = input("Select Stat: ").strip().capitalize()
				if Skill_select in ["0", "Exit"]:
					break
				Num = input("How many skill points to add: ")
				if int(Num) > self.skill_points:
					print("Not enough skill points.", end="", flush=True)
					readchar.readkey()
					pass
				elif int(Num) < 0:
					print("Not a valid input.", end="", flush=True)
					readchar.readkey()
					pass
				else:
					match Skill_select.strip().capitalize():
						case 'Vit' | '1':
							self.status['Vit'] += int(Num)
							self.skill_points -= int(Num)
							self.refresh_stats()
						case 'Str' | '2':
							self.status['Str'] += int(Num)
							self.skill_points -= int(Num)
							self.refresh_stats()
						case 'Agi' | '3':
							self.status['Agi'] += int(Num)
							self.skill_points -= int(Num)
							self.refresh_stats()
						case 'Dex' | '4':
							self.status['Dex'] += int(Num)
							self.skill_points -= int(Num)
							self.refresh_stats()
						case 'Int' | '5':
							self.status['Int'] += int(Num)
							self.skill_points -= int(Num)
							self.refresh_stats()
						case _:
							print("Not an expected input.", end="", flush=True)
							readchar.readkey()
							pass
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
		time.sleep(.01)
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
