"""Describes the items in the game."""
__author__ = 'Emma Grasmeder'


class Item():
    '''
        Items are game objects that are in some way interact-with-able.
        
        This class was originally designed for items that players could
        hold in their inventory, but why should we differentiate between
        a lock in a wooden door (not an object just anyone can have in
        their inventory) and a padlock in an inventory. So, doors and
        traps and any other non-environment, non-character objects will
        be *items,* and depending on skills will be interact-with-able in
        different capacities. #maybe only giants can put doors in their
        #inventory, and only certain crafty people can install doors.
    '''
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return "{}:\n=====\n{}\nWeighs: {}\n".format(self.name,
                                                    self.description,
                                                    self.weight)


class Weapon(Item):
    def __init__(self, 
                    name,
                    description,
                    weight,
                    damage,
                    speed):

        self.damage = damage # 50 -> kill a human in 2 hits (without mods)
        self.speed = speed # 10 -> 6 uses per minute (without mods)
        super().__init__(name, description, weight)

    def __str__(self):
        return "{} \n =====\n{}\nDamage: {}\nWeighs: {}".format(self.name,
                                                            self.description,
                                                            self.damage,
                                                            self.weight)


class Rock(Weapon):
    def __init__(self):
        super().__init__(\
                    name="Rock",
                    description="A fist-sized rock, suitable for bludgeoning.",
                    weight=2.5,
                    damage=5,
                    speed=7)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(\
                    name="Dagger",
                    description="A small dagger with some rust.\n"+
                        "Somewhat more dangerous than a rock.",
                    weight=2.5,
                    damage=10,
                    speed=10)


class Gold(Item):
    def __init__(self, amt):
        #self.amt = amt
        self.amt = 100
        super().__init__(\
            name="Gold",
            description="A round coin with {} stamped on the front.".\
                format(str(self.amt)),
            weight=.03)