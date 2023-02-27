from enum import Enum

from .game_scripts import max_number, reverse_string, if_string_is_number


class Script(Enum):
    MAX_NUMBER = 1, max_number.run
    REVERSE_STRING = 2, reverse_string.run
    IF_STRING_IS_JUST_A_NUMBER = 3, if_string_is_number.run
    EXIT = 0, "exit"

    def __init__(self, index, function):
        self.index = index
        self.function = function

    @classmethod
    def get_function(cls, choice):
        for script in cls:
            if choice == script.index:
                return script.function

    @classmethod
    def is_a_valid_choice(cls, number: str):
        value = int(number)
        assert 0 <= value < len(cls)
        return value
