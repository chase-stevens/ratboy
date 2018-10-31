from character import Character
from monster import Rat_Bandit
from weapon import Steel_Blade

import sys

class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Rat_Bandit(),
            Rat_Bandit(),
            Rat_Bandit(),
            Rat_Bandit(),
            Rat_Bandit(),
            Rat_Bandit(),
            Rat_Bandit(),
            Rat_Bandit(),
            Rat_Bandit(),
            Rat_Bandit()
        ]
        self.monster = self.get_next_monster()
        self.player.equip_weapon(self.player.player_weapon)

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        if self.player.bushwhack_timer > 0:
            self.player.bushwhack_timer -= 1
        else:
            pass

        if self.player.doublestrike_timer > 0:
            self.player.doublestrike_timer -= 1
        else:
            pass

        if self.player.yojimbo_strike_timer > 0:
            self.player.yojimbo_strike_timer -= 1
        else:
            pass

        if self.monster.attack():
            print("{} attacks!".format(self.monster))

            if self.player.dodge():
                    print("You dodged! Yes!")
            else:
                    print("Oh no! The monster's attack lands!")
                    self.player.hit_points -= 1
                    print ("You have {} Hit Points.".format(self.player.hit_points))

        else:
            print ("{} missed!".format(self.monster))


    def player_turn(self):

        player_decision = input("[A]ttack, [R]est, Abilit[y], "
                                "Check [W]eapon, or [Q]uit? ")

        if player_decision == 'a':
            print("You're attacking the {}!".format(self.monster))
            if self.player.attack():
                if self.monster.dodge():
                    print("The monster dodged!")
                else:
                    damage = self.player.attack_calc(self.monster.armor)
                    if self.player.crit():
                        print("Critical hit!")
                        damage += damage
                    self.monster.hit_points -= damage
                    print("Hit! You did {} points of damage.".format(damage))
            else:
                print("You whiffed!")

        elif player_decision == 'b':
            if "[B]ushwhack" not in self.player.ABILITY_LIST:
                print("You don't know how to bushwhack anymore!")
                self.player_turn()

            elif self.player.bushwhack_timer > 0:
                print ("Bushwhack is still on cooldown!")
                self.player_turn()

            else:
                print("You're bushwhacking {}!".format(self.monster))
                self.player.bushwhack_timer += 3
                if self.player.attack():
                    if self.monster.dodge():
                        print("The monster dodged!")
                    else:
                        damage = self.player.bushwhack_formula(self.monster.armor)
                        if self.player.crit():
                            print("Critical hit!")
                            damage += damage
                        self.monster.hit_points -= damage
                        print("Thwump! Your bushwhack did {} points of damage.".format(damage))
                else:
                    print("You whiffed!")

        elif player_decision == 'j':
            if "Yo[j]imbo Strike" not in self.player.ABILITY_LIST:
                print("You don't know how to do that!")
                self.player_turn()

            elif self.player.yojimbo_strike_timer > 0:
                print ("Yojimbo Strike is still on cooldown!")
                self.player_turn()

            else:
                print("You're yojimbo striking {}!".format(self.monster))
                self.player.yojimbo_strike_timer += 3
                if self.player.attack():
                    if self.monster.dodge():
                        print("The monster dodged!")
                    else:
                        damage = self.player.yojimbo_strike_formula(self.monster.armor)
                        if self.player.crit():
                            print("Critical hit!")
                            damage += damage
                        self.monster.hit_points -= damage
                        print("Thwump! Your bushwhack did {} points of damage.".format(damage))
                else:
                    print("You whiffed!")

        elif player_decision == 'd':
            if "[D]oublestrike" not in self.player.ABILITY_LIST:
                print("You don't know how to doublestrike yet!")
                self.player_turn()

            elif self.player.doublestrike_timer > 0:
                print ("Doublestrike is still on cooldown!")
                self.player_turn()

            else:
                print("You're doublestriking {}!".format(self.monster))
                self.player.doublestrike_timer += 3

                for i in range(2):
                    if self.player.attack():
                        if self.monster.dodge():
                            print("The monster dodged!")
                        else:
                            damage = self.player.attack_calc(self.monster.armor)
                            if self.player.crit():
                                print("Critical hit!")
                                damage += damage
                            self.monster.hit_points -= damage
                            print("Hit! You did {} points of damage.".format(damage))
                    else:
                        print("You whiffed!")

        elif player_decision == 'r':
            self.player.rest()

        elif player_decision == 'y':
            print(self.player.ABILITY_LIST)
            self.player_turn()

        elif player_decision == 'w':
            print(self.player.player_weapon)
            self.player_turn()

        elif player_decision == 'q':
            sys.exit()

        else:
            self.player_turn()

    def cleanup(self):
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            print("{} has died!".format(self.monster))

            if self.player.leveled_up():
                self.player.level_up()

                if self.player.level == 2:
                    print("You have refined your ability! Your Bushwhack is now Doublestrike!")
                    self.player.ABILITY_LIST.remove("[B]ushwhack")
                    self.player.ABILITY_LIST.append("[D]oublestrike")

                if self.player.level == 5:
                    print("You have learned a new ability! You can now Yojimbo Strike!")
                    self.player.ABILITY_LIST.append("Yo[j]imbo Strike")

            self.monster = self.get_next_monster()

    def __init__(self):
        self.setup()

        while self.player.hit_points and (self.monster or self.monsters):
            print("\n" + "=" * 20)
            print(self.player)
            self.monster_turn()
            print("-" * 20)
            self.player_turn()
            self.cleanup()
            print("\n" + "=" * 20)

        if self.player.hit_points:
            print("You win!")
        elif self.monsters or self.monster:
            print("You lose!")
        sys.exit()

Game()
