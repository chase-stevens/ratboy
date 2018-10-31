class Armor():
    armor_value = 1


class Ragged_Chest(Armor):
    armor_value = 5

    def __str__(self):
        return "Ragged Chest: {}".format(self.armor_value)


class Leather_Armor(Armor):
    armor_value = 10
    agility_up = 2


    def __str__(self):
        return "Leather Armor: {}".format(self.armor_value)


class Wrappings_of_the_Hero(Armor):
    armor_value = 20
    strength_up = 5
    agility_up = 10

    def __str__(self):
        return "Wrappings of the Hero: {}".format(self.armor_value)
