"""
This is the file to run the game manager.
It requires the modules game, library and history to run.
"""

import os
#import numpy as np
#import pandas as pd
#import csv
#from datetime import datetime
#from game import Game, GAME_DETAILS
from library import Library
#from history import History


# Change working directory to the path of the script
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(DIR_PATH)
LIBRARY_PATH = "./library.gm"

def main():

    # Initiate object library (empty)
    library = Library()
    # If there is already a saved file for the library, load it
    if os.path.isfile(LIBRARY_PATH):
        library.load(LIBRARY_PATH)

    # Start the user interaction
    input(WELCOME_SCREEN)
    library = user_interaction(library)

    # Save the library into the file
    if input("Do you want to save the library before you quit? Enter 'y' if so: ") == "y":
        library.save(LIBRARY_PATH)


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
    return f'''

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
    valid = False
    while not valid:
        valid = True
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
            command = input("This was not a valid command. Try again:\n")
            valid = False
    return lib

def user_interaction(lib):
    command_input = input(command_screen(lib))
    choose_action(command_input, lib)
    while command_input != "exit":
        command_input = input(command_screen(lib))
        lib = choose_action(command_input, lib)
    return lib

main()
