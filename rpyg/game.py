"""
A simple text adventure designed as a learning experience for new programmers.
"""
__author__ = 'Phillip Johnson, Emma Grasmeder'
import world
from player import Player


def play():
    def real_game_mode(action_input,player):
        if action_input == action.hotkey:
            player.do_action(action, **action.kwargs)
    def nl_train_mode():
        print("God mode enabled!")
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