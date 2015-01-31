"""Describes the actions a player can make in the game"""
__author__ = 'Phillip Johnson, Emma Grasmeder'

from character import Character


class Action():
    """The base class for all actions"""
    def __init__(self, method, name, hotkey, **kwargs):
        """Creates a new action

        :param method: the function object to execute
        :param name: the name of the action
        :param ends_turn: True if the player is expected to 
            move after this action else False
        :param hotkey: The keyboard key the player should 
            use to initiate this action
        """

        self.method = method
        self.name = name
        self.kwargs = kwargs
        self.hotkey = hotkey

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Character.move_north,
                            name='Move north',
                            hotkey='n')


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Character.move_south,
                            name='Move south', hotkey='s')


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Character.move_east,
                            name='Move east',
                            hotkey='e')


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Character.move_west,
                            name='Move west',
                            hotkey='w')


class ViewInventory(Action):
    """Prints the character's inventory"""
    def __init__(self):
        super().__init__(method=Character.print_inventory,
                            name='View inventory',
                            hotkey='i')


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Character.attack,
                            name="Attack",
                            hotkey='a',
                            enemy=enemy)

class Open(Action):
    def __init__(self, direct_object):
        super().__init__(method=Character.use,
                            name="Open",
                            hotkey='u',
                            direct_object=direct_object)


class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Character.flee,
                            name="Flee",
                            hotkey='f',
                            tile=tile)