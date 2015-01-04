'''
    agents.py is the main class to manage the agents
    in the rpyg ABM.

    The class will be instantiated and used between run.py
    and model.py
'''

__author__ = 'Emma Grasmeder'
import time

class Agent:
    def __init__(self, hp=100, dmg=10):
        """
            Creates a new enemy

            :param hp: character's hitpoints
            :param dmg: damage per unit of time
            :param lifespan: to keep track of agent life
        """
        self.hp = hp
        self.dmg = dmg
        self.lifespan = time.time()
        self.is_alive = True

    def die(self):
        self.is_alive = False
        self.lifespan = time.time()-self.lifespan
        print("agent died after %s seconds" % self.lifespan)


    def take_damage(self,amt):
        if self.is_alive and self.hp > amt:  #alive but about to die
            self.hp -= amt
        elif self.is_alive: #alive but hp <= amt, die
            self.hp -= amt
            self.die()
        else:
            pass # not alive, hp>=< dmg

    def attack(self,victim):
        victim.take_damage(self.dmg)

    def status_report(self):
        if self.is_alive:
            print("hp: ", self.hp)

