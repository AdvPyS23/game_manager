"""
This is a module containing the classes game and collection of the game manager.
It is required to run the tool.

Classes:
    Game
        _summary_
    Collection
        _summary_

Functions:
    _summary_
"""

from datetime import datetime
from itertools import chain, repeat
import os
import csv
import numpy as np
import pandas as pd

# Define the number of points to give for details such as complexity and difficulty
NUM_POINTS =  10
# Define the values to choose from for details such as topics, skills etc.
TOPICS = ("fantasy",
          "science fiction",
          "real world",
          "abstract",
          "adaptation",
          "other")

SKILLS = ("logics",
          "dexterity",
          "intuition",
          "creativity",
          "knowledge",
          "strategy",
          "negotiation",
          "luck",
          "roleplay",
          "other")

PHYSICAL_PARTS = ("board",
                  "cards",
                  "dice",
                  "supplementals",
                  "other")

SOCIAL_TYPES = ("cooperative",
                "one_vs_all",
                "teams",
                "all_vs_all",
                "other")

# Define all the details a game has information about
GAME_DETAILS = ("name",
                "min_num_players",
                "max_num_players",
                "min_duration",
                "max_duration",
                "min_age",
                "complexity",
                "difficulty",
                "topic",
                "skills",
                "physical_parts",
                "social_type")

# Definie data structure
DETAILS_COLS = ("string",
                "type",
                "allowed_values")

# Create data frame with the details a game can have
DETAIL_DF = pd.DataFrame(np.array([["name of the game", "string", "any"],
                                   ["minimum number of players", "int", ">=1"],
                                   ["maximum number of players", "int", ">=min_num_players"],
                                   ["minimum duration (minutes)", "int", ">=1"],
                                   ["maximum duration (minutes)", "int", ">=min_duration"],
                                   ["minimum age (years)", "int", ">=1"],
                                   [f"complexity level (1 - {NUM_POINTS})", "int_range", "1 - NUM_POINTS"],
                                   [f"difficulty level (1 - {NUM_POINTS})", "int_range", "1 - NUM_POINTS"],
                                   [f"topic ({', '.join(TOPICS)})", "string_choice", "TOPICS"],
                                   [f"skill needed ({', '.join(SKILLS)})", "string_choice", "SKILLS"],
                                   [f"physical part ({', '.join(PHYSICAL_PARTS)})", "string_choice", "PHYSICAL_PARTS"],
                                   [f"social type ({', '.join(SOCIAL_TYPES)})", "string_choice", "SOCIAL_TYPES"]]),
                                columns = DETAILS_COLS,
                                index = GAME_DETAILS)
ALLOWED_VALUES_DICT = {"any":["any"],
                    ">=1":[">=1"],
                   ">=min_num_players":[">=minimum number of players"],
                   ">=min_duration":[">=minimum duration"],
                   "1 - NUM_POINTS":[f"1 - {NUM_POINTS}"],
                   "TOPICS":TOPICS,
                   "SKILLS":SKILLS,
                   "PHYSICAL_PARTS":PHYSICAL_PARTS,
                   "SOCIAL_TYPES":SOCIAL_TYPES}

class Game:
    """
    This is the class for an individual game.
    It stores all the intrinsic properties of a game (see attributes)
    It does not store information about the history/events of playing a game

    Attributes
    ----------
    game_id : _type_
        _summary_
    game_name : _type_
        _summary_
    detail : _type_
        _summary_

    Methods
    -------
    ask_details(self):
        _summary_
    get_details(self):
        _summary_
    print_details(self):
        _summary_
    
    set_single_detail(self, detail, value):
        _summary_
    get_single_detail(self, detail):
        _summary_
    print_single_detail(self, detail, value):
        _summary_
    """

    def __init__(self, name):
        self.game_id = f"game_{datetime.now():%Y%m%d%H%M%S%f}"
        self.game_name = name
        self.details = {detail: "NA" for detail in GAME_DETAILS}

    def __str__(self):
        return f"Game: {self.game_name} (ID: {self.game_id})"

    def ask_details(self):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        for detail in GAME_DETAILS:
            # Create a iterator of prompts (as strings)
            # with the first being the initial prompt for the detail
            # and possibly infinite requests for correcting the input
            prompts = chain([f"What is the {DETAIL_DF.loc[detail, 'string']}? "],
                            repeat(f"Sorry, the input must be {', '.join(ALLOWED_VALUES_DICT[DETAIL_DF['allowed_values'][detail]])}. Try again: "))
            # Check the detail type
            detail_type = DETAIL_DF.loc[detail, "type"]
            # Convert to lowercase for string_choice inputs
            if detail_type == "string_choice":
                replies = map(lambda x: x.lower(), map(input, prompts))
            else:
                # Run input function with all the prompts to get the reply
                replies = map(input, prompts)
            # Check if the values are valid for that type
            if detail_type == "int":
                valid_response = next(filter(lambda reply: (reply.isdigit() and int(reply)>0), replies))
            elif detail_type == "int_range":
                valid_response = next(filter(lambda reply: (reply.isdigit() and 1 <= int(reply) <= NUM_POINTS), replies))
            elif detail_type == "string_choice":
                valid_response = next(filter(ALLOWED_VALUES_DICT[DETAIL_DF["allowed_values"][detail]].__contains__, replies))
            elif detail_type == "string":
                valid_response = input(f"What is the {DETAIL_DF.loc[detail, 'string']}? ")
            self.details[detail] = valid_response
        return self.details
    
    def get_details(self):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        return self.details
    
    def print_details(self):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        for detail in self.details:
            print(f"The {DETAIL_DF.loc[detail, 'string']} of {self.game_name} is {self.details[detail]}")

    def set_single_detail(self, detail, value):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        detail_type = DETAIL_DF.loc[detail, "type"]
        if detail_type == "int" and int(value)>0:
            self.details[detail] = value
        elif detail_type == "int_range" and value.isdigit() and 1 <= int(value) <= NUM_POINTS:
            self.details[detail] = value
        elif detail_type == "string_choice" and value.lower() in ALLOWED_VALUES_DICT[DETAIL_DF["allowed_values"][detail]]:
            self.details[detail] = value.lower()
        elif detail_type == "any":
            self.details[detail] = value
        else: raise ValueError("""There was something wrong with the value.
                               Nothing was changed. Try again.""")

    def get_single_detail(self, detail):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        return self.details[detail]
    
    def print_single_detail(self, detail):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        print(f"The {DETAIL_DF.loc[detail, 'string']} of {self.game_name} is {self.details[detail]}")


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
        if self.name == "library": self.id = "library"
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

    def print(self):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        for game_id, game_details in self.dict.items():
            print(game_id, game_details)
    
    def get_string(self):
        out = ""
        for game_id, game_details in self.dict.items():
            out += str(game_id) + ": " + str(game_details) + "\n"
        return out

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
