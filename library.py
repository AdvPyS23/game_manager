"""
This is a module containing the class Library of the game manager and helper functions.
It is required to run the tool.
It itself requires the module game to run.

Classes:
    Library
        _summary_

Functions:
    _summary_
"""

# import os
import csv
# import numpy as np
# import pandas as pd
from datetime import datetime
from game import Game, GAME_DETAILS


###################################
### CLASS DEFINITION
###################################

class Library:
    """
    This is the class for a game library.
    It stores the games, including all their informations (as instances of class Game).
    It does not store information about the history/events of playing a game.
    """

    def __init__(self):
        self.games = {}

    def __str__(self):
        return "    * " + "\n    * ".join(self.games.keys())

    def load(self, library_path):
        """
        Loads a library from a file given by library_path and creates all games defined in the file
        """
        # Go through all games and create instances for them inside the library dict
        with open(library_path, "r", encoding='UTF8') as library_file:
            reader = csv.reader(library_file)
            for game in reader:
                gm_id, name, detail_string = game
                details = detail_string.split(",")
                detail_dict = dict(zip(GAME_DETAILS.values(), details))
                self.games[name] = Game(gm_id, name, detail_dict)

    def save(self, library_path):
        """
        Saves the library into a file given by library_path
        """
        # Save all the games into the library file
        with open(library_path, 'w', encoding='UTF8', newline='') as library_file:
            writer = csv.writer(library_file)
            for name, game in self.games.items():
                gm_id = game.get_id()
                name = game.get_name()
                ### MAYBE CHECK THAT NO GAME OBJECT HAS DIFFERENT NAME THAN ENTRY IN LIBRARY...
                details = ",".join(game.get_all_details().values())
                writer.writerow([gm_id, name, details])

    def add(self):
        """
        Asks the user for the name of a new game and creates a game with this name
        Also asks the user to enter all the details for this new game
        """
        gm_id = f"game_{datetime.now():%Y%m%d%H%M%S%f}"
        name = self.ask_new_name("Please enter the name of the new game: ")
        self.games[name] = Game(gm_id, name)
        self.games[name].ask_all_details()

    def delete(self):
        """
        Asks the user for the name of a game and deletes this game from the library
        """
        name = self.ask_name("Please enter the name of the game to delete. ")
        if input(f"Are you sure to delete this game: {name}?\
                 \nEnter 'y' to delete or anything else to abort: ") == "y":
            self.games.pop(name)

    def modify(self):
        """
        Asks the user for the name of a game and a detail and let's them change this detail
        """
        name = self.ask_name("Please enter the name of the game to change. ")
        detail = choose_detail()
        self.games[name].ask_detail(detail)

    def show(self):
        """
        Asks the user for the name of a game and shows all the details of this game
        """
        name = self.ask_name("Please enter the name of the game to see. ")
        title = "============ " + name + " ============"
        bottom = "=" * (26 + len(name))
        print("\n" + title + "\n\n" + self.games[name].get_all_details_str() + "\n\n" + bottom)

    def rename(self):
        """
        Asks the user for a game and a new name and sets the name of the game to this new name
        """
        # Ask for the existing name of the game to change
        name = self.ask_name("Please enter the name of the game to rename. ")
        # Get the old id, it should be retained
        gm_id = self.games[name].get_id()
        # Get all the details of the game
        details = self.games[name].get_all_details()
        # Ask for the new name, and make sure it does not yet exist
        new_name = self.ask_new_name("Please enter the name of the new game: ")
        # Delete the old game
        self.games.pop(name)
        # Create a new game with the same id and details but the new name
        self.games[new_name] = Game(gm_id, new_name, details)

    def ask_name(self, input_string = "What is the name of the game? "):
        """
        Asks the user to give a name of a game in the library; repeats until succeeds
        """
        # Ask for the existing name of the game
        name = input(input_string)
        while name not in self.games:
            name = input("There is no game with this name in the library.\nPlease enter a valid name (case sensitive): ")
        return name

    def ask_new_name(self, input_string = "What is the name of the game? "):
        """
        Asks the user to give a name of a new game, i.e. NOT already in the library; repeats until succeeds
        """
        # Ask for the new name, and make sure it does not yet exist
        new_name = input(input_string)
        while new_name in self.games:
            new_name = input("There is already a game with this name in the library.\nPlease enter another name: ")
        return new_name


###################################
### HELPER FUNCTIONS
###################################

def choose_detail():
    """
    Creates a checklist of details and returns the detail chosen by the user
    """
    detail_checklist = '\n'.join([f'{det_letter}: {det_str}' for det_letter, det_str in GAME_DETAILS.items()])
    detail_key = input("\nChoose a detail (enter a single letter):\n" + detail_checklist + "\n\n")
    while detail_key not in GAME_DETAILS:
        detail_key = input("\nThat didn't work. Try again (enter a single letter):\n")
    detail = GAME_DETAILS[detail_key]
    return detail
