__author__ = 'Phillip Johnson, Emma Grasmeder'

_world = {}


def tile_exists(x, y):
        """Returns the tile at the given coordinates or None if there is no tile.

        :param x: the x-coordinate in the worldspace
        :param y: the y-coordinate in the worldspace
        :return: the tile at the given coordinates or None if there is no tile
        """
        return _world.get((x, y))


def load_tiles(tile_map='resources/map.txt',train_tile=False):
    """Parses a file that describes the world space into the _world object"""
    with open(tile_map, 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            if not train_tile:
                tile_name = cols[x].replace('\n', '')
                input("tile name is: "+ tile_name)
            else: train_tile = 'LanguageTrainingRoom'
            _world[(x, y)] = \
                None if tile_name == \
                '' else getattr(__import__('tiles'), tile_name)(x, y)