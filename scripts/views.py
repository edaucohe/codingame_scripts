from scripts.models import Script
from .tools.input_verifications import verify_input


class MainMenuTerminalView:
    def __init__(self, script=Script):
        self.script = script

    def display_menu(self):
        for game in self.script:
            print(f"{game.index}) {game.name}")

    def enter_choice(self):
        number: int = verify_input(
            "\nEnter a choice : ",
            parse_function=self.script.is_a_valid_choice
        )
        return number
