"""
This is a module containing the class Game of the game manager and helper functions.
It is required to run the tool.

Classes:
    Game
        _summary_

Functions:
    _summary_
"""

# from datetime import datetime
from itertools import chain, repeat
# import os
# import csv
import numpy as np
import pandas as pd

###################################
### GLOBAL CONSTANTS
###################################

# Define all the details a game has information about
GAME_DETAILS = {"a": "min_num_players",
                "b": "max_num_players",
                "c": "min_duration",
                "d": "max_duration",
                "e": "min_age",
                "f": "complexity",
                "g": "difficulty",
                "h": "topic",
                "i": "skills",
                "j": "physical_form",
                "k": "social_type"}

# Define the number of points to give for details such as complexity and difficulty
NUM_POINTS =  10

# Define the values to choose from for details such as topics, skills etc.
TOPICS = {"0": "fantasy",
          "1": "science fiction",
          "2": "real world",
          "3": "abstract",
          "4": "adaptation",
          "9": "other"}

SKILLS = {"0": "logics",
          "1": "dexterity",
          "2": "intuition",
          "3": "creativity",
          "4": "knowledge",
          "5": "strategy",
          "6": "negotiation",
          "7": "luck",
          "8": "roleplay",
          "9": "other"}

PHYSICAL_FORM = {"0": "board",
                  "1": "cards",
                  "2": "dice",
                  "3": "supplementals",
                  "9": "other"}

SOCIAL_TYPES = {"0": "cooperative",
                "1": "one_vs_all",
                "2": "teams",
                "3": "all_vs_all",
                "9": "other"}

# Definie attributes for each detail
DETAIL_ATTRIBUTES = ("string",
                     "type",
                     "allowed_values")

# Create data frame with the details a game can have and its attributes
DETAIL_DF = pd.DataFrame(np.array([["minimum number of players", "int", ">=1"],
                                   ["maximum number of players", "int", ">=min_num_players"],
                                   ["minimum duration (minutes)", "int", ">=1"],
                                   ["maximum duration (minutes)", "int", ">=min_duration"],
                                   ["minimum age (years)", "int", ">=1"],
                                   [f"complexity level (1 - {NUM_POINTS})", "int_range", "1 - NUM_POINTS"],
                                   [f"difficulty level (1 - {NUM_POINTS})", "int_range", "1 - NUM_POINTS"],
                                   [f"topic", "choice", "TOPICS"],
                                   [f"skill needed", "choice", "SKILLS"],
                                   [f"physical form", "choice", "PHYSICAL_FORM"],
                                   [f"social type", "choice", "SOCIAL_TYPES"]]),
                                   columns = DETAIL_ATTRIBUTES,
                                   index = GAME_DETAILS.values())

ALLOWED_VALUES_DICT = {">=1":[">=1"],
                       ">=min_num_players":[">=minimum number of players"],
                       ">=min_duration":[">=minimum duration"],
                       "1 - NUM_POINTS":[f"1 - {NUM_POINTS}"],
                       "TOPICS":TOPICS,
                       "SKILLS":SKILLS,
                       "PHYSICAL_FORM":PHYSICAL_FORM,
                       "SOCIAL_TYPES":SOCIAL_TYPES}


###################################
### CLASS DEFINITION
###################################

class Game:
    """
    This is the class for an individual game.
    It stores all the intrinsic properties of a game (id, name, details).
    It does not store information about the history/events of playing a game.

    Attributes
    ----------
    id : _type_
        _summary_
    name : _type_
        _summary_
    details : _type_
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

    def __init__(self, gm_id, name, details = False):
        self.id = gm_id
        self.set_name(name)
        # Initiate all details to ""
        self.details = {detail: "" for detail in GAME_DETAILS.values()}
        # If there is a details dictionary given, we assign the given details
        if details:
            self.set_multi_details(details)

    def __str__(self):
        return f"Game: {self.name} (ID: {self.id})"

    def set_name(self, name):
        self.name = name

    def set_detail(self, detail, value):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        detail_type = find_detail_attribute(detail, "type")
        allowed_values = find_detail_attribute(detail, "allowed_values")
        error_message = f"The entered value ({value}) is not suitable for this type of detail ('{detail_type}').\
            Values must be {allowed_values}"

        # Test, for the type of detail given, the value entered
        if detail_type == "int":
            try:
                assert int(value) > 0
            except AssertionError:
                print(error_message)
        elif detail_type == "int_range":
            try:
                assert 1 <= int(value) <= NUM_POINTS
            except AssertionError:
                print(error_message)
        elif detail_type == "choice":
            try:
                value = sort_test_choice(value, allowed_values)
                assert value
            except AssertionError:
                print(error_message)
        # If it's of no known type, raise a specific error
        else: raise ValueError(f"There was no test found for this detail type ({detail_type}). \
                               Nothing was changed. Try again.")
        # If all tests are passed and no error raised, set the detail to the entered value
        self.details[detail] = value

    def set_multi_details(self, details_dict):
        for key, val in details_dict.items():
            self.set_detail(key, val)

    def ask_detail(self, detail):
        # get the type, string and allowed values for this detail
        detail_type = find_detail_attribute(detail, "type")
        detail_string = find_detail_attribute(detail, "string")
        allowed_values = find_detail_attribute(detail, "allowed_values")

        if detail_type == "choice":
            valid_response = choice_input(detail_string, allowed_values)
        else:
            valid_response = num_input(detail_type, detail_string, allowed_values)

        self.set_detail(detail, valid_response)
        return self.details

    def ask_all_details(self):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        for detail in GAME_DETAILS.values():
            self.ask_detail(detail)
        return self.details

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_detail(self, detail):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        return self.details[detail]

    def get_all_details(self):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        return self.details

    def get_detail_str(self, detail):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        detail_type = find_detail_attribute(detail, "type")
        detail_string = find_detail_attribute(detail, "string")
        allowed_values = find_detail_attribute(detail, "allowed_values")

        if detail_type == "choice":
            key_string = self.details[detail]
            value_string = ", ".join([allowed_values[num] for num in key_string])
        else:
            value_string = self.details[detail]
        # See how long the longest detail string is
        max_len_detail_strings = np.max([len(det_str) for det_str in DETAIL_DF.loc[:,"string"]])
        # Make padding from the chosen detail_string up to the longest
        padding = " " * (max_len_detail_strings - len(detail_string))
        return f"{detail_string}: {padding}{value_string}"
        
    def get_all_details_str(self):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        return '\n'.join([self.get_detail_str(detail) for detail in self.details])


###################################
### HELPER FUNCTIONS
###################################

def choice_input(detail_string, allowed_values):
    '''
    Asks the user to input a selection for a detail of type "choice"
    Repeats until a valid user input value is given

    Inputs:
        detail_string:  String of the detail (ideally including a list of allowed values)
        allowed_values: List of all allowed values that can be
                        entered by the user

    Returns:
        valid_response: a string containing the keys of the dictionary belonging to the detail of type "choice"
    '''
    # DOING THIS THE OLD FASHIONED WAY TO TRY OUT FUNCTIONALITY, JUST BECAUSE MY BRAIN CAN'T HANDLE CHAIN, REPEAT ETC. RIGHT NOW
    choice_checklist = '\n'.join([f'{k}: {v}' for k, v in allowed_values.items()])
    reply = input(f"What is the {detail_string}?\
                  \nEnter any combination of numbers (without separator):\
                  \n{choice_checklist}\n")
    nums = sorted(set(reply))
    is_valid = np.all([num in allowed_values for num in nums])

    # Repeat if not...
    while not is_valid:
        reply = input(f"Sorry, the input must be any combination of the following numbers (without separator).\
                      \nTry again:\
                      \n{choice_checklist}\n")
        nums = sorted(set(reply))
        is_valid = np.all([num in allowed_values for num in nums])

    # Join back together all the (single and sorted) numbers into one string
    valid_response = "".join(nums)
    return valid_response

def num_input(detail_type, detail_string, allowed_values):
    '''
    Asks the user to input a numeric value for a detail of type "int" or "int_range"
    Repeats until a valid user input value is given

    Inputs:
        detail_type:    "int" or "int_range"
        detail_string:  String of the detail (ideally including a list of allowed values)
        allowed_values: A string describing what numbers are allowed

    Returns:
        valid_response: a string containing the user input number
    '''
    # Create an iterator of prompts (as strings)
    # with the first being the initial prompt for the detail
    # and possibly infinite requests for correcting the input
    prompts = chain([f"What is the {detail_string}? "],
                    repeat(f"Sorry, the input must be {', '.join(allowed_values)}. Try again: "))
    # Run input function with all the prompts to get the reply
    replies = map(input, prompts)
    # Check if the values are valid for that type
    if detail_type == "int":
        valid_response = next(filter(lambda reply: (reply.isdigit() and int(reply)>0), replies))
    elif detail_type == "int_range":
        valid_response = next(filter(lambda reply: (reply.isdigit() and 1 <= int(reply) <= NUM_POINTS), replies))

    return valid_response

def sort_test_choice(input_num_string, allowed_values):
    '''
    Checks if the digits in the input string are all in the allowed values
    
    Inputs:
        input_string:   String to test (should only contain allowed digits)
        allowed_values: The values (digits) that are allowed in the input string
    
    Returns:
        IF TEST PASSED: A string containing the sorted and unique digits of the input string
        IF TEST FAILS:  False

    '''
    # Take apart the numbers (still as strings), remove duplicates and sort
    nums = sorted(set(input_num_string))
    # Test if all numbers are in the allowed vlaues
    is_valid = np.all([num in allowed_values for num in nums])
    if not is_valid:
        return False
    else:
        return "".join(nums)

def find_detail_attribute(detail, attribute):
    '''
    Tests wether a detail has a certain attribute ...
    ... in the DETAIL_DF (and ALLOWED_VALUES_DICT) and returns it

    Inputs:
        detail:     Which detail to test
        attribute:  Which attribute to test (should be "type", "string" or "allowed_values")
    Returns:
        output:     the found attribute for the detail
    '''
    if attribute == "type":
        try:
            output = DETAIL_DF.loc[detail, "type"]
        except:
            print(f"Type of this detail ({detail}) not found in the DETAIL_DF")
    elif attribute == "string":
        try:
            output = DETAIL_DF.loc[detail, "string"]
        except:
            print(f"String of this detail ({detail}) not found in the DETAIL_DF")
    elif attribute == "allowed_values":
        try:
            output = ALLOWED_VALUES_DICT[DETAIL_DF.loc[detail, "allowed_values"]]
        except:
            print(f"Allowed values for this detail ({detail}) not found, \
                    either in the DETAIL_DF or in the ALLOWED_VALUES_DICT")
    return output
