"""
This is the main script to run the game manager.

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
TOPICS = ("Fantasy",
          "Science Fiction",
          "Real World",
          "Abstract",
          "Adaptation",
          "other")

SKILLS = ("Logics",
          "Dexterity",
          "Intuition",
          "Creativity",
          "Knowledge",
          "Strategy",
          "Negotiation",
          "Luck",
          "Roleplay",
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
GAME_DETAILS = ("min_num_players",
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
DETAIL_DF = pd.DataFrame(np.array([["minimum number of players", "int", ">=1"],
                                   ["maximum number of players", "int", ">=min_num_players"],
                                   ["minimum duration (minutes)", "int", ">=1"],
                                   ["maximum duration (minutes)", "int", ">=min_duration"],
                                   ["minimum age (years)", "int", ">=1"],
                                   [f"complexity level (1 - {NUM_POINTS})", "int_range", "1 - NUM_POINTS"],
                                   [f"difficulty level (1 - {NUM_POINTS})", "int_range", "1 - NUM_POINTS"],
                                   [f"topic ({', '.join(TOPICS)})", "string", "TOPICS"],
                                   [f"skill needed ({', '.join(SKILLS)})", "string", "SKILLS"],
                                   [f"physical part ({', '.join(PHYSICAL_PARTS)})", "string", "PHYSICAL_PARTS"],
                                   [f"social type ({', '.join(SOCIAL_TYPES)})", "string", "SOCIAL_TYPES"]]),
                                columns = DETAILS_COLS,
                                index = GAME_DETAILS)
GAME_PROPERTIES = {">=1": [">=1"],
                   ">=min_num_players" : [">=minimum number of players"],
                   ">=min_duration" :[">=minimum duration"],
                   "1 - NUM_POINTS": [f"1 - {NUM_POINTS}"],
                   "TOPICS": TOPICS,
                   "SKILLS": SKILLS,
                   "PHYSICAL_PARTS": PHYSICAL_PARTS,
                   "SOCIAL_TYPES": SOCIAL_TYPES}

class Game:
    """
    _summary_

    ...

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
        for detail in GAME_DETAILS:
            prompts = chain([f"What is the {DETAIL_DF.loc[detail, 'string']}?"], repeat(f"Sorry, the input must be {', '.join(GAME_PROPERTIES[DETAIL_DF['allowed_values'][detail]])}. Try again:"))
            replies = map(input, prompts)
            if DETAIL_DF.loc[detail, 'type'] == "int":
                valid_response = next(filter(lambda replies: (replies.isdigit() and int(replies)>0), replies))
            elif DETAIL_DF.loc[detail, 'type'] == "int_range":
                valid_response = next(filter(lambda replies: (replies.isdigit() and 1 <= int(replies) <= NUM_POINTS), replies))
            elif DETAIL_DF.loc[detail, 'type'] == "string":
                valid_response = next(filter(GAME_PROPERTIES[DETAIL_DF['allowed_values'][detail]].__contains__, replies))
            self.details[detail] = valid_response
        return self.details
    def get_details(self):
        return self.details
    def print_details(self):
        for detail in self.details:
            print(f"The {DETAIL_DF.loc[detail, 'string']} of {self.game_name} is {self.details[detail]}")

    def set_single_detail(self, detail, value):
        if DETAIL_DF.loc[detail, 'type'] == "int" and int(value)>0:
            self.details[detail] = value
        elif DETAIL_DF.loc[detail, 'type'] == "int_range" and value.isdigit() and 1 <= int(value) <= NUM_POINTS:
            self.details[detail] = value
        elif DETAIL_DF.loc[detail, 'type'] == "string" and value in GAME_PROPERTIES[DETAIL_DF['allowed_values'][detail]]:
            self.details[detail] = value
    def get_single_detail(self, detail):
        return self.details[detail]
    def print_single_detail(self, detail):
        print(f"The {DETAIL_DF.loc[detail, 'string']} of {self.game_name} is {self.details[detail]}")

class Collection:
    """
    _summary_

    ...

    Attributes
    ----------
    col_id : _type_
        _summary_
    col_name : _type_
        _summary_
    list : _type_
        _summary_

    Methods
    -------
    print_colleciton(self):
        _summary_
    save_collection(self):
        _summary_
    add_game(self, game_id, game_details):
        _summary_
    remove_game(self, game_id):
        _summary_
    """

    def __init__(self, name):
        self.col_id = f"col_{datetime.now():%Y%m%d%H%M%S%f}"
        self.col_name = name
        self.dict = {}
    def __str__(self):
        return f"Collection: {self.col_name} (ID: {self.col_id})"

    # def load_collection(self):
    #     data_file = "./collection.csv"
    #     if os.path.isfile(data_file):
    #         with open(data_file, "r") as file:
    #             self.list = pd.read_csv(file)
    #             for row in self.list:
    #                 print(row)
    #     else:
    #         print("There is no collection available.")

    def print_colleciton(self):
        for game_id, game_details in self.dict.items():
            print(game_id, game_details)

    def save_collection(self):
        data_file = "./collection.csv"
        if not os.path.isfile(data_file):
            with open(data_file, "a", newline="") as file:
                writer_item = csv.writer(file)
                for new_k, new_v in self.dict.items():
                    writer_item.writerow([new_k, new_v])
        else:
            with open(data_file, "a", newline="") as file:
                writer_item = csv.writer(file)
                for new_k, new_v in self.dict.items():
                    writer_item.writerow([new_k, new_v])

    def add_game(self, game_id, game_details):
        self.dict[game_id] = game_details
        return self.dict

    def remove_game(self, game_id):
        del self.dict[game_id]
        return self.dict







tichu = Game("Tichu")
tichu.ask_details()
tichu.set_single_detail("topic", "Science Fiction")

uno = Game("Uno")
uno.ask_details()
uno.set_single_detail("topic", "Fantasy")

# print(tichu.game_id)
# tichu.print_details()
# print(tichu.get_single_detail("topic"))
# tichu.print_single_detail("topic")

Sabrina = Collection("Sabrina")
Sabrina.add_game(tichu.game_id, tichu.details)
Sabrina.add_game(uno.game_id, uno.details)
Sabrina.remove_game(tichu.game_id)
Sabrina.print_colleciton()
Sabrina.save_collection()
