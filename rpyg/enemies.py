"""Defines the enemies in the game"""
__author__ = 'Emma Grasmeder'

from character import Character

class Enemy(Character):
    '''
        The defining characteristic of an enemy is that it is, by default,
        antagonistic towards the protagonist's party. 

        I don't yet know how we'll navigate this framework when our heroes 
        either shapeshift, confuse, or charm an Enemy object...
    '''
    def __init__(self, name, base_hp, base_damage):
        self.is_antagonistic = True
        super().__init__(name=name,
                        base_hp=base_hp,
                        base_damage=base_damage)


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", base_hp=10, base_damage=20)

class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", base_hp=30, base_damage=27)

class Bandit(Enemy):
    def __init__(self):
        super().__init__(name="Bandit", base_hp=8, base_damage=14)

class Dire_Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Dire_Wolf", base_hp=10, base_damage=75)

class Giant(Enemy):
    def __init__(self):
        super().__init__(name="Giant", base_hp=50, base_damage=90)