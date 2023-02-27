from scripts.game_scripts.views import ScriptTerminalView


def run():
    view = ScriptTerminalView()

    title = "CHARACTER CHAIN IS JUST A NUMBER ?"
    description = "Enter a character chain and the script will return " \
                  "INTEGER if chain contains JUST integer numbers or " \
                  "FLOAT if chain contains JUST float numbers."

    view.display_game_description(title=title, description=description)
    character_chain = view.enter_character_chain()

    try:
        int(character_chain)
        result = "The input is just an INTEGER number"
    except ValueError:
        try:
            float(character_chain)
            result = "The input is just a FLOAT number"
        except ValueError:
            result = "The input is not a valid number"

    view.display_result(result=result)
