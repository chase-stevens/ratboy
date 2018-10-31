import random
import math


from weapon import Steel_Blade
from combat import Combat


class Character(Combat):
    attack_limit = 10
    strength = 5
    agility = 5
    weapon_strength = 1
    defense = 5
    base_hit_points = 75
    level = 1
    experience = 0
    bushwhack_timer = 0
    doublestrike_timer = 0
    yojimbo_strike_timer = 0
    player_weapon = Steel_Blade()

    ABILITY_LIST = ['[B]ushwhack']




    def crit(self):
        roll = random.randint(1, 10)
        return roll == 10

    def __init__(self, **kwargs):
        self.name = input("Name: ")
        self.hit_points = self.base_hit_points

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "{}, Level: {} HP: {}/{}, XP: {}".format(self.name, self.level,
                                                        self.hit_points, self.base_hit_points,
                                                        self.experience)

    def rest(self):
        if self.hit_points < self.base_hit_points:
            self.hit_points += 1

    def leveled_up(self):
        return self.experience >= 10

    def level_up(self):
        self.experience = 0
        self.level += 1
        self.base_hit_points += 10
        self.hit_points = self.base_hit_points
        self.strength += 2
        self.defense += 2
        print("\nCongratulations! You have leveled up"
              "\nYou are now level {}."
              "\nYour strength has increased by 2"
              "\nYour armor has increased by 2".format(self.level))

    def attack_calc(self, target_def):
        calc = (((self.level * 2) / 5) + 1) * self.weapon_strength * (self.strength/target_def)
        return math.floor(calc)

    def bushwhack_formula(self, target_def):
        return math.floor((self.attack_calc(target_def) * 3) / 2)

    ## blade master abilities

    def doublestrike(self, target_def):
        self.attack_calc(target_def)
        self.attack_calc(target_def)

    def exposing_blow(self, target_def):
        self.attack_calc(target_def)

    def yojimbo_strike_formula(self, target_def):
        return self.attack_calc(target_def) * 6

    def equip_weapon(self, wep):
        self.weapon_strength = wep.weapon_damage
