"""
This is the file to run the game manager.
It requires the modules game, collection and history to run.
"""

import os
from datetime import datetime
import numpy as np
import pandas as pd
import csv
from game import Game, GAME_DETAILS
from collection import Collection
from history import History

def main():
    # Change working directory to the path of the script
    dir_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(dir_path)
    library_path = "./library.gm"
    
    library = {}
    # If there is already a saved file for the library, load it
    if os.path.isfile(library_path):
        # Go through all games and create instances for them inside the library dict
        with open(library_path, "r") as library_file:
            reader = csv.reader(library_file)
            for game in reader:
                id, name, detail_string = game
                details = detail_string.split(",")
                detail_dict = dict(zip(GAME_DETAILS, details))
                library[name] = Game(id, name, detail_dict)

    # Start the user interaction
    input(WELCOME_SCREEN)
    library = user_interaction(library)

    # Save all the games into the library file
    with open(library_path, 'w', encoding='UTF8', newline='') as library_file:
        writer = csv.writer(library_file)
        for name, game in library.items():
            id = game.get_id()
            name = game.get_name()
### MAYBE CHECK THAT NO GAME OBJECT HAS DIFFERENT NAME THAN ETNRY IN LIBRARY...
            details = ",".join(game.get_all_details().values())
            writer.writerow([id, name, details])


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

def command_screen(lib):
    '''
    Defines and returns the command screen depending on the loaded collection
    '''
    games_string = "    * " + "\n    * ".join(lib.keys())

    c_s = f'''
################################################################################
    
Your library contains the following games:

{games_string}

Choose your option by typing one of the following commands into the console:

- Add a new game:               "new"
- See details of a game:        "see"
- Modify a detail of a game:    "mod"
- Delete a game from library:   "del"

- Save and quit:                "exit"

################################################################################

'''
    return c_s

def choose_action(command, lib):
    if command == "new":
        id = f"game_{datetime.now():%Y%m%d%H%M%S%f}"
        name = input("Please enter the name of the new game: ")
        while name in lib.keys():
            name = input("There is already a game with this name in the library. Please enter another name: ")
        lib[name] = Game(id, name)
        lib[name].ask_all_details()
    elif command == "del":
        name = input("Please enter the name of the game to delete. ")
        while name not in lib.keys():
            name = input("There is no game with this name in the library. Please enter a valid name: ")
        if input(f"Are you sure to delete this game: {name}? Enter 'y' if so: ") == "y":
            lib.pop(name)
    elif command == "mod":
        name = input("Please enter the name of the game to change. ")
        while name not in lib.keys():
            name = input("There is no game with this name in the library. Please enter a valid name: ")
        detail = input("Please enter the detail of the game to change. ")
        while detail not in GAME_DETAILS:
            detail = input("There is no such detail. Please enter a valid detail: ")
        lib[name].ask_detail(detail)
    elif command == "see":
        name = input("Please enter the name of the game to see. ")
        while name not in lib.keys():
            name = input("There is no game with this name in the library. Please enter a valid name: ")
        print("\n" + lib[name].get_all_details_str())
        input("\nPress enter to continue...")
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
#               "physical_parts": "9319",
#               "social_type": "21"}
# tichu.set_multi_details(details_in)
# print(tichu.get_all_details())
# # {'min_num_players': '2', 'max_num_players': '6', 'min_duration': '60', 'max_duration': '120',
# # 'min_age': '12', 'complexity': '5', 'difficulty': '9', 'topic': '1', 'skills': '23',
# # 'physical_parts': '139', 'social_type': '12'}
# print(tichu.get_detail("physical_parts"))
# # 139
# print(tichu.get_detail_str("physical_parts"))
# # The physical part (board, cards, dice, supplementals, other) of Tichu is: cards, supplementals, other

# tichu.ask_detail("min_duration")
# # --> enter 4
# print(tichu.get_detail("min_duration"))
# # 4

# tichu.ask_detail("social_type")
# print(tichu.get_detail("min_duration"))

# tichu.ask_all_details()
# print(tichu.get_all_details())



