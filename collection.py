"""
This is a module containing the class collection of the game manager.
It is required to run the tool.

Classes:
    Collection
        _summary_

Functions:
    _summary_
"""

from datetime import datetime
#from itertools import chain, repeat
import os
import csv
# import numpy as np
# import pandas as pd

###################################
### GLOBAL CONSTANTS
###################################



###################################
### CLASS DEFINITION
###################################

class Collection:
    """
    _summary_

    ...

    Attributes
    ----------
    id : _type_
        _summary_
    name : _type_
        _summary_
    list : _type_
        _summary_

    Methods
    -------
    load_file(self):
        _summary_
    print(self):
        _summary_
    save(self):
        _summary_
    add_game(self, game_id, game_details):
        _summary_
    remove_game(self, game_id):
        _summary_
    """

    def __init__(self, name):
        self.id = f"col_{datetime.now():%Y%m%d%H%M%S%f}"
        self.name = name
        if self.name == "library":
            self.id = "library"
        self.dict = {}
        self.games_dict = {}

    def __str__(self):
        return f"Collection: {self.name} (ID: {self.id})"

    def load_file(self, id):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        data_file = f"./{id}.gmcol"
        if os.path.isfile(data_file):
            with open(data_file, newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.dict = {"game_id":row["game_id"], "game_detail":row["game_details"]}
        else:
            print(f"There is no collection with the id {id} available.")

    def save(self):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        data_file = f"./{self.id}.gmcol"
        with open(data_file, "a", newline="") as csvfile:
            fieldnames = ["game_id", "game_details"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for game_id, game_details in self.dict.items():
                writer.writerow({"game_id": game_id, "game_details": game_details})

    def add_game(self, game_id, game_details):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        self.dict[game_id] = game_details
        return self.dict

    def new_game(self):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        game_id = f"game_{datetime.now():%Y%m%d%H%M%S%f}"
        self.dict[game_id] = "Here should come the game details"
# ADJUST THIS ACCORDING TO CHOSEN DATA STRUCTURE !!!

    def remove_game(self, game_id):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        del self.dict[game_id]
        return self.dict

    def get_game_ids(self):
        return self.dict.keys()

    def get_details_string(self):
        out = ""
        for game_id, game_details in self.dict.items():
            out += str(game_id) + ": " + str(game_details) + "\n"
        return out

    def print(self):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        for game_id, game_details in self.dict.items():
            print(game_id, game_details)


###################################
### HELPER FUNCTIONS
###################################
