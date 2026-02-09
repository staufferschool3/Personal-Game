# Game imports
from Alnir_Game import Enemy

# Instancing Enemy
Enemy_critter = Enemy()

# Equipment Manager
class EquipmentMan:
    def __init__(self):
        None

    def weapon(self, Damage=None, Effect=None):
        self.weapon.dmg = Damage
        self.weapon.effect = Effect

    def effect(self, Effect=None):
        self.effect = Effect

# Rusty Sword
def rusty_sword(Enemy_critter):
    Tetnis = Enemy_critter.agi(-10)
    Rusty_sword = EquipmentMan.weapon(40)
    Rusty_sword = EquipmentMan.effect(Tetnis)
