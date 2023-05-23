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
    elif command == "mod":
        game = input("Please enter the id of the game to change. ")
# TEST VALID INPUT HERE!!!
        detail = input("Please enter the detail of the game to change. ")
# TEST VALID INPUT HERE!!!
        game.ask_detail(detail, input("What value?"))
    elif command == "see":
        game = input("Please enter the id of the game to see. ")
        print("Here should come the info about the game")
    elif command != "exit":
        print("This was not a valid command.")
        input("Press Enter to continue...")
    return lib

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

def command_screen(col):
    '''
    Defines and returns the command screen depending on the loaded collection
    '''

    command_screen = f'''
Your collection contains the following games:
{col.get_details_string()}
Choose your option by typing one of the following commands into the console:

- Add a new game:               "new"
- Remove a game:                "del"
- See details of a game:        "see"
- Modify a detail of a game:    "mod"
'''
    return command_screen

# main()






tichu = Game("Tichu")
print(tichu)
# Game: Tichu (ID: game_*
tichu.set_detail("min_num_players", 3)
print(tichu.get_detail("min_num_players"))
# 3
tichu.set_detail("min_num_players", 0)
# Error
print(tichu.get_detail("min_num_players"))
# 3
#### !!!!!!!!!!!!!   WRONG RESULT   !!!!!!!!!!!!! #############
tichu.set_detail("max_num_players", 24)
print(tichu.get_detail("max_num_players"))
# 24
tichu.set_detail("complexity", 7)
print(tichu.get_detail("complexity"))
# 7
tichu.set_detail("complexity", 24)
# Error
print(tichu.get_detail("complexity"))
# 7
#### !!!!!!!!!!!!!   WRONG RESULT   !!!!!!!!!!!!! #############
tichu.set_detail("social_type", "13")
print(tichu.get_detail("social_type"))
# 13
print(tichu.get_detail_str("social_type"))
# The social type (cooperative, one_vs_all, teams, all_vs_all, other) of Tichu is: one_vs_all, all_vs_all


details_in = {"min_num_players": "2",
              "max_num_players": "6",
              "min_duration": "60",
              "max_duration": "120",
              "min_age": "12",
              "complexity": "5",
              "difficulty": "9",
              "topic": "1",
              "skills": "23",
              "physical_parts": "9319",
              "social_type": "21"}
tichu.set_multi_details(details_in)
print(tichu.get_all_details())
# {'min_num_players': '2', 'max_num_players': '6', 'min_duration': '60', 'max_duration': '120',
# 'min_age': '12', 'complexity': '5', 'difficulty': '9', 'topic': '1', 'skills': '23',
# 'physical_parts': '139', 'social_type': '12'}
print(tichu.get_detail("physical_parts"))
# 139
print(tichu.get_detail_str("physical_parts"))
# The physical part (board, cards, dice, supplementals, other) of Tichu is: cards, supplementals, other

tichu.ask_detail("min_duration")
# --> enter 4
print(tichu.get_detail("min_duration"))
# 4

tichu.ask_detail("social_type")
print(tichu.get_detail("min_duration"))

tichu.ask_all_details()
print(tichu.get_all_details())


# tichu.ask_topic_test()
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
