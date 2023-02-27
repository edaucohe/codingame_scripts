from typing import Callable, Any


def verify_input(data: str, parse_function: Callable[[str], Any]) -> Any:
    while True:
        input_value = input(data)
        try:
            return parse_function(input_value)
        except (AssertionError, ValueError):
            print("Choice isn't a valid option")
