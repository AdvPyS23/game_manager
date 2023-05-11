"""
This is the file to run the game manager.
It requires the modules game_collection and history to run.
"""

import os
import numpy as np
import pandas as pd
from game_collection import Game, Collection
from history import History

def main():
    # Create the object library (the main collection)
    library = Collection("library")
    # If there is already a saved file for the library, load it
    if os.path.isfile("./library.gmcol"): library.load_file("library")
    # If not, create one (empty)
    else: library.save()

    input(WELCOME_SCREEN)

    command_screen =f'''
    Your collection contains the following games:
    {library.get_string()}
    Choose your options by typing one of the following commands into the console:

    - Add a new game:               "new"
    - See details of a game:        "game_id"
    - Change a detail of a game:    "change"
    - Remove a game:                "del"
    '''

    command_input = input(command_screen)
    choose_action(command_input, library)
    while command_input != "exit":
        command_input = input(command_input)
        library = choose_action(command_input, library)


def choose_action(command, lib):
    if command == "new":
        lib.new_game()
    elif command == "change":
        game = input("Please enter the id of the game to change. ")
# TEST VALID INPUT HERE!!!
        detail = input("Please enter the detail of the game to change. ")
# TEST VALID INPUT HERE!!!
        game.set_single_detail(detail, input("What value?"))
# OPTIMISE INPUT! (THERE IS NO METHOD ASK_SINGLE_DETAIL YET...)
    elif command == "del":
        game = input("Please enter the id of the game to delete. ")
        lib.remove_game(game)
    else:
        if command in lib.get_game_ids():
            game = command
            print("Here should come the info about the game")
        elif command != "exit":
            print("This was not a valid command.")
            # input("Press Enter to continue...")
    return lib

# tichu = Game("Tichu")
# tichu.ask_details()
# tichu.set_single_detail("topic", "SCIENCE fiction")

# uno = Game("Uno")
# uno.ask_details()
# uno.set_single_detail("topic", "fantasy")

# print(tichu.game_id)
# tichu.print_details()
# print(tichu.get_single_detail("topic"))
# tichu.print_single_detail("topic")

# Sabrina = Collection("Sabrina")
# Sabrina.add_game(tichu.game_id, tichu.details)
# Sabrina.add_game(uno.game_id, uno.details)
# Sabrina.remove_game(tichu.game_id)
# Sabrina.print_collection()
# Sabrina.save_collection()
# Sabrina.load_collection()

WELCOME_SCREEN = '''
                            Hi, welcome to 

##############################################################################
                            
  __ _  __ _ _ __ ___   ___ _ __ ___   __ _ _ __   __ _  __ _  ___ _ __ 
 / _` |/ _` | '_ ` _ \ / _ \ '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__|
| (_| | (_| | | | | | |  __/ | | | | | (_| | | | | (_| | (_| |  __/ |   
 \__, |\__,_|_| |_| |_|\___|_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|   
  __/ |                                                  __/ |          
 |___/                                                  |___/           

##############################################################################

                        Press enter to continue 

'''

main()