import random

from combat import Combat

COLORS = ['yellow', 'red', 'blue']

NAMES = ['Francesco', 'Alessandro', 'Andrea',
         'Lorenzo', 'Mattia', 'Matteo',
         'Gabriele', 'Leonardo', 'Riccardo', 'Tommaso']

class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    strength = 5
    weapon_strength = 10
    armor = 5
    weapon = 'sword'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)
        self.name = random.choice(NAMES)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{} the {}, HP: {}'.format(self.name,
                                          self.__class__.__name__,
                                          self.hit_points,)


class Goblin(Monster):
    max_hit_points = 3
    max_experience = 2
    sound = 'squeak'

class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 2
    max_experience = 6

class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
    sound = 'raaaaaar'

class Rat_Bandit(Monster):
    min_hit_points = 50
    max_hit_points = 55
    min_experience = 5
    max_experience = 5
