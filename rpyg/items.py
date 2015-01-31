"""Describes the items in the game."""
__author__ = 'Emma Grasmeder'


class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name,
                                                    self.description,
                                                    self.value)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name,
                                                            self.description,
                                                            self.value,
                                                            self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for\
                          bludgeoning.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with\
                            some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)


class Gold(Item):
    def __init__(self, amt):
        #self.amt = amt
        self.amt = 100
        super().__init__(name="Gold",description="A round coin with {} \
            stamped on the front.".format(str(self.amt)),value=self.amt)


class UsableItem():
    """The base class for all usable items"""
    def __init__(self,
                name,
                description,
                status,
                is_binary,
                value=None,
                **kwargs):
        self.name = name
        self.description = description
        self.value = value
        self.status = status
        self.is_binary = is_binary

        if not is_binary:
            self.not_binary(kwargs)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n"\
            .format(self.name,
                    self.description,
                    self.value)

class Door(UsableItem):
    def __init__(self, is_locked):
        self.is_locked = False
        self.status = "open"
        self.is_binary = True
        super().__init__(name="Door",description="A heavy wooden door with\
            rusty hinges sits {} in front of you."\
                .format(str(self.status)),status=self.status)

    def do_action(self, **kwargs):
        ''' This function will handle actions on items
            which have more than one way to be interacted with '''
        pass