"""
A simple text adventure designed as a learning experience for new programmers.
Based originally on the tutorial by Phillip Johnson. Written for Python 3!
"""
__author__ = 'Emma Grasmeder'
import world
from character import Character


def play():
    world.load_tiles()
    my_character = Character()
    my_character.name = input("Initializing...\n\n\n\n\nAh! Hello\n" +\
        "What is your name, stranger?\n\nCall me ")
    while my_character.is_alive() and not (my_character.victory):
        room = world.tile_exists(my_character.location_x, my_character.location_y)
        room.modify_character(my_character)
        # Check again since the room could have changed the player's state
        if my_character.is_alive() and not my_character.victory:
            print("--------------\n--\n--------------\nChoose an action: " +"\n")
            available_actions = room.available_actions()
            print("room avail actions: %s"%room.name)
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:  #see world.tile_exists(x,y).room.available_actions()
                    my_character.do_action(action, **action.kwargs)
                    break

if __name__ == "__main__":
    play()