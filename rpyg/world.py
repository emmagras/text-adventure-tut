__author__ = 'Phillip Johnson, Emma Grasmeder'

_world = {}


def tile_exists(x, y):
        """Returns the tile at the given coordinates or None if there is no tile.
        :param x: the x-coordinate in the worldspace
        :param y: the y-coordinate in the worldspace
        :return: the tile at the given coordinates or None if there is no tile
        """
        return(_world.get((x, y)))


def load_tiles(tiles_map='resources/map.txt', noisy=False):
    """Parses a file that describes the world space into the _world object"""
    rows = open(tiles_map, 'r').readlines()
    for y, row in enumerate(rows):
        rooms_in_row = [room.replace('\n',"") for room in row.split('\t')]
        for x, tile_name in enumerate(rooms_in_row):
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)
            if noisy: return(_world)
