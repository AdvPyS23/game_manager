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

import os
from datetime import datetime
import numpy as np
import pandas as pd
import csv
from game import Game, GAME_DETAILS

class Library:
    """
    This is the class for a game library.
    It stores the games.
    It does not store information about the history/events of playing a game
    """

    def __init__(self):
        self.games = {}

    def __str__(self):
        return "    * " + "\n    * ".join(self.games.keys())
    
    def load(self, library_path):
        # Go through all games and create instances for them inside the library dict
        with open(library_path, "r") as library_file:
            reader = csv.reader(library_file)
            for game in reader:
                id, name, detail_string = game
                details = detail_string.split(",")
                detail_dict = dict(zip(GAME_DETAILS, details))
                self.games[name] = Game(id, name, detail_dict)
    
    def save(self, library_path):
        # Save all the games into the library file
        with open(library_path, 'w', encoding='UTF8', newline='') as library_file:
            writer = csv.writer(library_file)
            for name, game in self.games.items():
                id = game.get_id()
                name = game.get_name()
### MAYBE CHECK THAT NO GAME OBJECT HAS DIFFERENT NAME THAN ETNRY IN LIBRARY...
                details = ",".join(game.get_all_details().values())
                writer.writerow([id, name, details])    

    def add(self):
        id = f"game_{datetime.now():%Y%m%d%H%M%S%f}"
        name = input("Please enter the name of the new game: ")
        while name in self.games.keys():
            name = input("There is already a game with this name in the library. Please enter another name: ")
        self.games[name] = Game(id, name)
        self.games[name].ask_all_details()
        
    def delete(self):
        name = input("Please enter the name of the game to delete. ")
        while name not in self.games.keys():
            name = input("There is no game with this name in the library. Please enter a valid name: ")
        if input(f"Are you sure to delete this game: {name}? Enter 'y' if so: ") == "y":
            self.games.pop(name)
    
    def modify(self):
        name = input("Please enter the name of the game to change. ")
        while name not in self.games.keys():
            name = input("There is no game with this name in the library. Please enter a valid name: ")
        detail = input("Please enter the detail of the game to change. ")
        while detail not in GAME_DETAILS:
            detail = input("There is no such detail. Please enter a valid detail: ")
        self.games[name].ask_detail(detail)

    def show_game(self):
        name = input("Please enter the name of the game to see. ")
        while name not in self.games.keys():
            name = input("There is no game with this name in the library. Please enter a valid name: ")
        print("\n" + self.games[name].get_all_details_str())
    
    def rename(self):
        # Ask for the existing name of the game to change
        name = input("Please enter the name of the game to rename. ")
        while name not in self.games.keys():
            name = input("There is no game with this name in the library. Please enter a valid name: ")
        # Get the old id, it should be retained
        id = self.games[name].get_id()
        # Get all the details of the game
        details = self.games[name].get_all_details()
        # Ask for the new name, and make sure it does not yet exist
        new_name = input("Please enter the name of the new game: ")
        while new_name in self.games.keys():
            new_name = input("There is already a game with this name in the library. Please enter another name: ")
        # Delete the old game
        self.games.pop(name)
        # Create a new game with the same id and details but the new name
        self.games[new_name] = Game(id, new_name, details)