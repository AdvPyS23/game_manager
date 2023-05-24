"""
This is a module containing the class History of the game manager and helper functions.
It is required to run the tool.

Classes:
    History
        _summary_

Functions:
    _summary_
"""


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

