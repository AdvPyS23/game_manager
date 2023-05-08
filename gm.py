"""
This is the main script to run the game manager.

Classes:
    Game
        _summary_
    Collection
        _summary_
    History
        _summary_

Functions:
    _summary_
"""

from datetime import datetime
from itertools import chain, repeat
import numpy as np
import pandas as pd

# Define the number of points to give for details such as complexity and difficulty
NUM_POINTS =  10
# Define the values to choose from for details such as topics, skills etc.
TOPICS = ("Fantasy", "Science Fiction", "Real World", "Abstract", "Adaptation", "other")
SKILLS = ("Logics", "Dexterity", "Intuition", "Creativity", "Knowledge", "Strategy", "Negotiation", "Luck", "Roleplay")
PHYSICAL_PARTS = ("board", "cards", "dice", "supplementals", "other")
SOCIAL_TYPES = ("cooperative", "one_vs_all", "teams", "all_vs_all", "other")
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
DETAILS_COLS = ("string", "type", "allowed_values")
DETAIL_DF = pd.DataFrame(np.array( [["minimum number of players", "int", ">=1"],
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
GAME__PROPERTIES = { ">=1": [">=1"],
                    ">=min_num_players" : [">=minimum number of players"],
                    ">=min_duration" :[">=minimum duration"],
                    "1 - NUM_POINTS": [f"1 - {NUM_POINTS}"],
                    "TOPICS": TOPICS,
                    "SKILLS": SKILLS,
                    "PHYSICAL_PARTS": PHYSICAL_PARTS,
                    "SOCIAL_TYPES": SOCIAL_TYPES,
                    "GAME_DETAILS": GAME_DETAILS,
                    "DETAIL_DF": DETAIL_DF}

class Game:
    """
    _summary_

    ...

    Attributes
    ----------
    id : _type_
        _summary_
    name : _type_
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
        self.id = f"game_{datetime.now():%Y%m%d%H%M%S%f}"
        self.name = name
        self.details = {detail: "NA" for detail in GAME_DETAILS}
    def __str__(self):
        return f"Game: {self.name} (ID: {self.id})"

    def ask_details(self):
        for detail in GAME_DETAILS:
            prompts = chain([f"What is the {DETAIL_DF.loc[detail, 'string']}?"], repeat(f"Sorry, the input must be {', '.join(GAME__PROPERTIES[DETAIL_DF['allowed_values'][detail]])}. Try again:"))
            replies = map(input, prompts)
            if DETAIL_DF.loc[detail, 'type'] == "int":
                valid_response = next(filter(lambda replies: (replies.isdigit() and int(replies)>0), replies))
            elif DETAIL_DF.loc[detail, 'type'] == "int_range":
                valid_response = next(filter(lambda replies: (replies.isdigit() and 1 <= int(replies) <= NUM_POINTS), replies))
            elif DETAIL_DF.loc[detail, 'type'] == "string":
                valid_response = next(filter(GAME__PROPERTIES[DETAIL_DF['allowed_values'][detail]].__contains__, replies))
            self.details[detail] = valid_response
    def get_details(self):
        return self.details
    def print_details(self):
        for detail in self.details:
            print(f"The {DETAIL_DF.loc[detail, 'string']} of {self.name} is {self.details[detail]}")

    def set_single_detail(self, detail, value):
        if DETAIL_DF.loc[detail, 'type'] == "int" and int(value)>0:
            self.details[detail] = value
        elif DETAIL_DF.loc[detail, 'type'] == "int_range" and value.isdigit() and 1 <= int(value) <= NUM_POINTS:
            self.details[detail] = value
        elif DETAIL_DF.loc[detail, 'type'] == "string" and value in GAME__PROPERTIES[DETAIL_DF['allowed_values'][detail]]:
            self.details[detail] = value
    def get_single_detail(self, detail):
        return self.details[detail]
    def print_single_detail(self, detail):
        print(f"The {DETAIL_DF.loc[detail, 'string']} of {self.name} is {self.details[detail]}")

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
    _name_:
        _summary_
    """

    def __init__(self, name):
        self.id = f"col_{datetime.now():%Y%m%d%H%M%S%f}"
        self.name = name
        self.list = []
    def __str__(self):
        return f"Collection: {self.name} (ID: {self.id})"


class History:
    """
    _summary_

    ...

    Attributes
    ----------
    id : _type_
        _summary_
    name : _type_
        _summary_

    Methods
    -------
    _name_:
        _summary_
    """

    def __init__(self, name):
        self.id = f"history_{datetime.now():%Y%m%d%H%M%S%f}"
        self.name = name
    def __str__(self):
        return f"Game:{self.name} (ID: {self.id})"


# gm = initialise_gm""
# print(gm["NUM_POINTS"])

# initialise_gm()
# print(DETAIL_DF)
# tichu = Game("Tichu")
# print(tichu)
# tichu.ask_details()
# print(tichu.get_details())
# tichu.print_details()
# tichu.set_single_detail("topic", "Science Fiction")
# print(tichu.get_single_detail("topic"))
# tichu.print_single_detail("topic")
