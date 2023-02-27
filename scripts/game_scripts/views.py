from typing import Any


class ScriptTerminalView:
    @staticmethod
    def display_game_description(title: str, description: str):
        print(title + "\n" + description)

    @staticmethod
    def display_result(result: Any):
        print(str(result) + "\n")

    @staticmethod
    def enter_character_chain():
        valid_character_chain: str = input("\nEnter a character chain : ")
        return valid_character_chain
