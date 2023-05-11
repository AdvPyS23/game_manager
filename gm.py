"""
This is the file to run the game manager.
It requires the modules game_collection and history to run.

"""

import os
import csv
import numpy as np
import pandas as pd
from game_collection import Game, Collection
from history import History



tichu = Game("Tichu")
tichu.ask_details()
tichu.set_single_detail("topic", "SCIENCE fiction")

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
# Sabrina.print_colleciton()
# Sabrina.save_collection()
# Sabrina.load_collection()