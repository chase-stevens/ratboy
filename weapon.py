class Weapon():
    weapon_damage = 1


class Iron_Sword(Weapon):
    weapon_damage = 5

    def __str__(self):
        return "Iron Sword - Damage: {}".format(self.weapon_damage)


class Steel_Blade(Weapon):
    weapon_damage = 10
    agility_up = 2

    def __str__(self):
        return "Steel Blade - Damage: {}".format(self.weapon_damage)


class Cosmic_Edge(Weapon):
    weapon_damage = 100
    strength_up = 10
    agility_up = 20

    def __str__(self):
        return "Cosmic Edge - Damage: {}".format(self.weapon_damage)
