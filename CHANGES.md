# Improving the structure with abstraction and decomposition

## Decomposition
We divided the software into, up to now, three parts. The first part is the script to run the tool. Then there are two modules: [game_collection](./game_collection.py) containing the classes *Game* and *Collection* (the library of games), and [history](./history.py) with the class *History* representing the histroy of events (playing the games and rating the experience). 

## Abstraction
The definition of games, collections and histories as classes inside modules, allows us to hide the details about those entities in the main code. Also, we are planning to use more helper functions to reach more Abstraction in the code inside the classes (not implemented yet).