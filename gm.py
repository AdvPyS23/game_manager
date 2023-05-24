"""
This is the file to run the game manager.
It requires the modules game, library, collection and history to run.
"""

import os
from datetime import datetime
import numpy as np
import pandas as pd
import csv
from game import Game, GAME_DETAILS
from library import Library
from collection import Collection
from history import History
    

# Change working directory to the path of the script
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(DIR_PATH)
LIBRARY_PATH = "./library.gm"

def main():
    
    # Initiate object library (empty)
    library = Library()
    # If there is already a saved file for the library, load it
    if os.path.isfile(LIBRARY_PATH): library.load(LIBRARY_PATH)

    # Start the user interaction
    input(WELCOME_SCREEN)
    library = user_interaction(library)

    # Save the library into the file
    if input("Do you want to save the library before you quit? Enter 'y' if so: ") == "y": library.save(LIBRARY_PATH)


WELCOME_SCREEN = '''
                            Hi, welcome to 

###############################################################################
                            
    __ _  __ _ _ __ ___   ___    _ __ ___   __ _ _ __   __ _  __ _  ___ _ __ 
   / _` |/ _` | '_ ` _ \ / _ \  / '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__|
  | (_| | (_| | | | | | |  __/  | | | | | | (_| | | | | (_| | (_| |  __/ |   
   \__, |\__,_|_| |_| |_|\___|  |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|   
    __/ |                                                     __/ |          
   |___/                                                     |___/           

###############################################################################

                        Press enter to continue ... 

'''

def command_screen(lib): return f'''

################################## GAME MANAGER ##################################

Your library contains the following games:

{str(lib)}

Choose your option by typing one of the following commands into the console:

- Add a new game:               "new"
- See details of a game:        "see"
- Modify a detail of a game:    "mod"
- Rename a game:                "name"
- Delete a game from library:   "del"

- Save the library:             "save"
- Quit:                         "exit"

################################################################################

'''

def choose_action(command, lib):
    if command == "new":
        lib.add()
    elif command == "del":
        lib.delete()
    elif command == "mod":
        lib.modify()
    elif command == "see":
        lib.show()
        input("\nPress enter to continue...")
    elif command == "save":
        lib.save(LIBRARY_PATH)
    elif command == "name":
        lib.rename()
    elif command != "exit":
        print("This was not a valid command.")
        input("Press Enter to continue...")
    return lib

def user_interaction(lib):
    command_input = input(command_screen(lib))
    choose_action(command_input, lib)
    while command_input != "exit":
        command_input = input(command_screen(lib))
        lib = choose_action(command_input, lib)
    return lib

main()




###################################
### TESTS
###################################

# tichu = Game("Tichu")
# print(tichu)
# # Game: Tichu (ID: game_*
# tichu.set_detail("min_num_players", 3)
# print(tichu.get_detail("min_num_players"))
# # 3
# tichu.set_detail("min_num_players", 0)
# # Error
# print(tichu.get_detail("min_num_players"))
# # 3
# #### !!!!!!!!!!!!!   WRONG RESULT   !!!!!!!!!!!!! #############
# tichu.set_detail("max_num_players", 24)
# print(tichu.get_detail("max_num_players"))
# # 24
# tichu.set_detail("complexity", 7)
# print(tichu.get_detail("complexity"))
# # 7
# tichu.set_detail("complexity", 24)
# # Error
# print(tichu.get_detail("complexity"))
# # 7
# #### !!!!!!!!!!!!!   WRONG RESULT   !!!!!!!!!!!!! #############
# tichu.set_detail("social_type", "13")
# print(tichu.get_detail("social_type"))
# # 13
# print(tichu.get_detail_str("social_type"))
# # The social type (cooperative, one_vs_all, teams, all_vs_all, other) of Tichu is: one_vs_all, all_vs_all


# details_in = {"min_num_players": "2",
#               "max_num_players": "6",
#               "min_duration": "60",
#               "max_duration": "120",
#               "min_age": "12",
#               "complexity": "5",
#               "difficulty": "9",
#               "topic": "1",
#               "skills": "23",
#               "physical_form": "9319",
#               "social_type": "21"}
# tichu.set_multi_details(details_in)
# print(tichu.get_all_details())
# # {'min_num_players': '2', 'max_num_players': '6', 'min_duration': '60', 'max_duration': '120',
# # 'min_age': '12', 'complexity': '5', 'difficulty': '9', 'topic': '1', 'skills': '23',
# # 'physical_form': '139', 'social_type': '12'}
# print(tichu.get_detail("physical_form"))
# # 139
# print(tichu.get_detail_str("physical_form"))
# # The physical form (board, cards, dice, supplementals, other) of Tichu is: cards, supplementals, other

# tichu.ask_detail("min_duration")
# # --> enter 4
# print(tichu.get_detail("min_duration"))
# # 4

# tichu.ask_detail("social_type")
# print(tichu.get_detail("min_duration"))

# tichu.ask_all_details()
# print(tichu.get_all_details())



