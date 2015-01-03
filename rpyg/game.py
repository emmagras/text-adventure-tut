"""
A simple text adventure designed as a learning experience for new programmers.
Based originally on the tutorial by Phillip Johnson.
"""
__author__ = 'Emma Grasmeder'
import world
from player import Player


def play():
    def real_game_mode(action_input,player):
        if action_input == action.hotkey:  #see room.available_actions()
            player.do_action(action, **action.kwargs)
    def nl_train_mode():
        print("Entering Natural Language processing mode!")
        player.do_action
        pass

    world.load_tiles()
    player = Player()
    while player.is_alive() and not (player.victory or player.nl_train):
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action: " +"\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input not in ["iddqd","idkfa","rosebud"]:
                    real_game_mode(action_input, player)
                    break
                else: #cheat enabled
                    nl_train_mode()
                    break




if __name__ == "__main__":
    play()