"""
Describes the tiles in the world space. Designed by Phillip Johnson
to describe a tile as a room. The new goal is to make rooms variable size,
and thus a tile represents a single meter of distance
"""
__author__ = 'Emma Grasmeder'

import items, enemies, actions, world, usable_items


class MapTile:
    """The base class for a tile within the world space"""
    def __init__(self, x, y, name=None, contents = [], **kwargs):
        """Creates a new tile.

        :param x: the x-coordinate of the tile
        :param y: the y-coordinate of the tile
        """
        self.x = x
        self.y = y
        self.character_modifier = None
        self.contents = contents
        self.name=name

    def modify_character(self, character):
        raise NotImplementedError()

    def event_text(self):
        '''
            Information to be displayed when the character moves into 
            this tile.

            In theory, certain tiles should have events, like a trap or
            your character going becoming invisible to average people. 
            This function will be the plae for those sentences to be 
            displayed.
        '''
        raise NotImplementedError() 

    def adjacent_moves(self):
        '''
            Returns all move actions for adjacent tiles.
        '''
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        '''
            Returns all of the available actions in this room, given a
            player's inventory
        '''
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        #print("MORE DEBUG: Name = %s"%self.name)
        moves.append(actions.CheckSurroundings(self))

        return moves


class StartingRoom(MapTile):
    def __init__(self,x,y):
        super().__init__(x,y,name="Starting Room",
            description="You find yourself if a cave with a" +\
                "flickering torch on the wall.\n You can make out four paths,"\
                +" each equally as dark and foreboding.",
            contents=None)

    def modify_character(self, character):
        pass

class EmptyCavePath(MapTile):
    def __init__(self, x, y):
        self.description = "Another unremarkable part of the cave."+\
                " You must forge onwards."
        super().__init__(x,y,name="Empty Cave Path",
            description=self.description,
            contents=None)

    def modify_character(self, character):
        pass

class House(MapTile):
    '''
        A generic base class for dwellings with 4 walls and a roof, by default.
    '''
    def __init__(self, x, y):
        super().__init__(x,y,name="A Generic House",
            description="A simple dwelling place,"+\
                " with 4 walls and a roof (for now)",
            contents=None)
    
    def intro_text(self):
        return ''' 
        '''
    def modify_character(self, character):
        pass

class LootRoom(MapTile):
    '''
        A room that contains a treasure chest 
    '''
    def __init__(self, x, y):
        self.contents = \
            [usable_items.TreasureChest(chest_contents=items.Gold())]
        self.name = "Treasure Chest Room"
        self.description = "A very dark room, but it looks like there"+\
                " might be something in the shadows..."
        super().__init__(x, y,
                contents=self.contents,
                name=self.name,
                description=self.description)
    
    def available_actions(self):
        return [item.actions for item in self.contents]

    def modify_character(self, character):
        pass

class FindDaggerRoom(MapTile):
    def __init__(self, x, y):
        self.contents = [items.Dagger()]
        self.name = "Find Dagger Room",
        self.description = "It's dark, but there seems to be something "+\
                    "glimmering on the floor."
        super().__init__(x, y,
                contents=self.contents,
                name=self.name,
                description=self.description)

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It's a dagger! You pick it up.
        """
    def modify_character(self, character):
        pass


class Find5GoldRoom(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def intro_text(self):
        return """
        Someone dropped a 5 gold piece. You pick it up.
        """
    def modify_character(self, character):
        pass


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_character(self, the_character):
        if self.enemy.is_alive():
            the_character.hp = the_character.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining."\
                .format(self.enemy.damage, the_character.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """
    def modify_character(self, character):
        pass


class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            An ogre is blocking your path!
            """
        else:
            return """
            A dead ogre reminds you of your triumph.
            """
    def modify_character(self, character):
        pass


class SnakePitRoom(MapTile):
    def intro_text(self):
        return """
        You have fallen into a pit of deadly snakes!

        You have died!
        """

    def modify_character(self, the_character):
        the_character.hp = 0


class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!


        Victory is yours!
        """

    def modify_character(self, character):
        character.victory = True

