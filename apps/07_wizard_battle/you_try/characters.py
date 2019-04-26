import random


class Character:

    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl

    def roll(self):
        return random.randint(1, 12) * self.lvl


class Hero(Character):

    def attack(self, target):

        hero_roll = self.roll()
        target_roll = target.roll()

        if hero_roll >= target_roll:
            return [True, hero_roll, target_roll]
        else:
            return [False, hero_roll, target_roll]


class BadGuy(Character):

    def __init__(self, name, lvl, ):
        super().__init__(name, lvl)

