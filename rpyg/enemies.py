"""Defines the enemies in the game"""
__author__ = 'Emma Grasmeder'

from character import Character

class GiantSpider(Character):
    def __init__(self):
        super().__init__(name="Giant Spider", base_hp=10, base_damage=20)

class Ogre(Character):
    def __init__(self):
        super().__init__(name="Ogre", base_hp=30, base_damage=27)

class Bandit(Character):
    def __init__(self):
        super().__init__(name="Bandit", base_hp=8, base_damage=14)

class Dire_Wolf(Character):
    def __init__(self):
        super().__init__(name="Dire_Wolf", base_hp=10, base_damage=75)

class Giant(Character):
    def __init__(self):
        super().__init__(name="Giant", base_hp=50, base_damage=90)

