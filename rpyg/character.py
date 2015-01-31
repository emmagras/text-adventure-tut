import random
import items, world

__author__ = 'Emma Grasmeder'


class Character:
    def __init__(self, name="unnamed", base_hp=10, base_damage=1):
        self.name = name
        self.damage = base_damage #later will be replaced by use_item(weapon1) or w.e.
        self.inventory = [items.Gold(15), items.Rock()]

        self.location_x, self.location_y = (2, 4)
        self.victory = False
        self.stats = {"Dexterity":7, "Vitality":10, 
                    "Intelligence":6,"Wisdom":4, "Charisma":6}
        self.hp = self.stats["Vitality"]*base_hp

    def is_alive(self):
        return self.hp > 0

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def view_character_stats(self):
        for statk, statv in self.stats.items():
            print("%s: %s\n" % statk, statv)

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def use(self, direct_object, **kwargs):
        ''' 
            Need to build in a "sense nearby items" function 

            Also, need to see if I can re-use the "do_action" method 
            for usable items.
        '''
        if isinstance(direct_object, items.UsableItem):
            direct_object.do_action(kwargs)
    
    def flee(self, tile):
        """Moves the character randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

