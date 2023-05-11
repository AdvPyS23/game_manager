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
    # Change working directory to the path of the script
    dir_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(dir_path)
    # Create the object library (the main collection)
    library = Collection("library")
    # If there is already a saved file for the library, load it
    if os.path.isfile("./library.gmcol"):
        library.load_file("library")

    # If not, create one (empty)
    else: library.save()

    input(WELCOME_SCREEN)

    command_input = input(command_screen(library))
    choose_action(command_input, library)
    while command_input != "exit":
        command_input = input(command_screen(library))
        library = choose_action(command_input, library)
    
    library.save()


def choose_action(command, lib):
    if command == "new":
        lib.new_game()
    elif command == "del":
        game = input("Please enter the id of the game to delete. ")
        lib.remove_game(game)
    elif command == "change":
        game = input("Please enter the id of the game to change. ")
# TEST VALID INPUT HERE!!!
        detail = input("Please enter the detail of the game to change. ")
# TEST VALID INPUT HERE!!!
        game.ask_detail(detail, input("What value?"))
    elif command in lib.get_game_ids():
        game = command
        print("Here should come the info about the game")
    elif command != "exit":
        print("This was not a valid command.")
        input("Press Enter to continue...")
    return lib

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

def command_screen(col):
    '''
    Defines and returns the command screen depending on the loaded collection
    '''

    command_screen = f'''
Your collection contains the following games:
{col.get_string()}
Choose your options by typing one of the following commands into the console:

- Add a new game:               "new"
- Remove a game:                "del"
- See details of a game:        "game_id"
- Change a detail of a game:    "change"
'''
    return command_screen

main()






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
