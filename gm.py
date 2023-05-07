import numpy as np
import pandas as pd
from datetime import datetime

def initialise_gm():
    global NUM_POINTS
    global TOPICS
    global SKILLS
    global PHYSICAL_PARTS
    global SOCIAL_TYPES
    global GAME_DETAILS
    global DETAIL_DF
    # Define the number of points to give for details such as complexity and difficulty
    NUM_POINTS =  10
    # Define the values to choose from for details such as topics, skills etc.
    TOPICS = ("Fantasy", "Science Fiction", "Real World", "Abstract", "Adaptation", "other")
    SKILLS = ("Logics", "Dexterity", "Intuition", "Creativity", "Knowledge", "Strategy", "Negotiation", "Luck", "Roleplay")
    PHYSICAL_PARTS = ("board", "cards", "dice", "supplementals", "other")
    SOCIAL_TYPES = ("cooperative", "one_v_all", "teams", "all_v_all", "other")
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
    DETAIL_COLS = ("string", "type", "allowed_values")
    DETAIL_DF = pd.DataFrame(np.array([["minimum number of players", "int", ""],
                                          ["maximum number of players", "int", ""],
                                          ["minimum duration (minutes)", "int", ""],
                                          ["maximum duration (minutes)", "int", ""],
                                          ["minimum age (years)", "int", ""],
                                          [f"complexity level (1 - {NUM_POINTS})", "int_range", "NUM_POINTS"], # tuple(n+1 for n in range(NUM_POINTS))],
                                          [f"difficulty level (1 - {NUM_POINTS})", "int_range", "NUM_POINTS"],  # tuple(n+1 for n in range(NUM_POINTS))],
                                          [f"topic ({', '.join(TOPICS)})", "choice", "TOPICS"], # TOPICS],
                                          [f"skill needed ({', '.join(SKILLS)})", "choice", "SKILLS"], # SKILLS],
                                          [f"physical part ({', '.join(PHYSICAL_PARTS)})", "choice", "PHYSICAL_PARTS"], # PHYSICAL_PARTS],
                                          [f"social type ({', '.join(SOCIAL_TYPES)})", "choice", "SOCIAL_TPYES"]]), # SOCIAL_TYPES]]))
                                columns = DETAIL_COLS,
                                index = GAME_DETAILS)
    # Consolidate and return in a dictionary
    GAME_PROPERTIES = {"NUM_POINTS": tuple(n+1 for n in range(NUM_POINTS)),
                       "TOPICS": TOPICS,
                       "SKILLS": SKILLS,
                       "PHYSICAL_PARTS": PHYSICAL_PARTS,
                       "SOCIAL_TYPES": SOCIAL_TYPES,
                       "GAME_DETAILS": GAME_DETAILS,
                       "DETAIL_DF": DETAIL_DF}
    return GAME_PROPERTIES

class game:
    def __init__(self, name):
        self.id = "game_" + "{:%Y%m%d%H%M%S%f}".format(datetime.now())
        self.name = name
        self.details = {detail: "NA" for detail in GAME_DETAILS}
    def __str__(self):
        return f"Game: {self.name} (ID: {self.id})"

    def ask_details(self):
        for detail in GAME_DETAILS:
            self.details[detail] = input(f"What is the {DETAIL_DF.loc[detail, 'string']}? ")
    def get_details(self):
        return self.details
    def print_details(self):
        for detail in self.details:
            print(f"The {DETAIL_DF.loc[detail, 'string']} of {self.name} is {self.details[detail]}")

    def set_single_detail(self, detail, value):
        self.details[detail] = value
    def get_single_detail(self, detail):
        return self.details[detail]
    def print_single_detail(self, detail):
        print(f"The {DETAIL_DF.loc[detail, 'string']} of {self.name} is {self.details[detail]}")

class collection:
    def __init__(self, name):
        self.id = "col_" + "{:%Y%m%d%H%M%S%f}".format(datetime.now())
        self.name = name
        self.list = []
    def __str__(self):
        return f"Collection: {self.name} (ID: {self.id})"


class history:
    def __init__(self, name):
        self.id = "history_" + "{:%Y%m%d%H%M%S%f}".format(datetime.now())
        self.name = name
    def __str__(self):
        return f"Game:{self.name} (ID: {self.id})"


# gm = initialise_gm""
# print(gm["NUM_POINTS"])

initialise_gm()
# print(DETAIL_DF)
tichu = game("Tichu")
print(tichu)
tichu.ask_details()
print(tichu.get_details())
tichu.print_details()
tichu.set_single_detail("topic", "SciFi")
print(tichu.get_single_detail("topic"))
tichu.print_single_detail("topic")
