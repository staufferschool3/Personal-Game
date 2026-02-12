# Equipment Manager
class EquipmentMan:
    def __init__(self):
        self.weapon = {"Name": "Fists", "Dmg": 0, "Effect": None}

    def equiped_weapon(self,Player, Weapon_name, Damage, Effect=None):
        # Updates the Player Gear
        self.weapon = {"Name": Weapon_name, "Dmg": Damage, "Effect": Effect}
        Player.equiped_weapon = self.weapon
        print(f"\n[SYSTEM]: {Weapon_name} equiped (Damage: {Damage})")