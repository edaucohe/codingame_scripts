from typing import Callable

from scripts.models import Script
from scripts.views import MainMenuTerminalView


class Controller:
    def __init__(self, view=MainMenuTerminalView(), script=Script):
        self.view = view
        self.script = script

    def run(self):
        run = True
        while run:
            self.view.display_menu()
            user_choice: int = self.view.enter_choice()
            if user_choice == self.script.EXIT.index:
                run = False
            else:
                function: Callable = self.script.get_function(user_choice)
                function()
