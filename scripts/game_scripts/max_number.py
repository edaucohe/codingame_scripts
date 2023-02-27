from scripts.game_scripts.views import ScriptTerminalView


def run():
    view = ScriptTerminalView()

    title = "MAX REVERSED NUMBER BETWEEN NUMBERS IN A STRING"
    description = "Enter INTEGER numbers in a character chain " \
                  "separated by spaces and script will return " \
                  "the max reversed number considering absolutes. " \
                  "For exemple: 21 -94 39 will return 93."

    view.display_game_description(title=title, description=description)
    character_chain = view.enter_character_chain()

    old_number = 0
    character_chain_list = character_chain.split()
    try:
        for number in character_chain_list:
            abs_number = abs(int(number))
            reverse_number = str(abs_number)[::-1]
            new_number = int(reverse_number)
            if old_number < new_number:
                old_number = new_number

        view.display_result(result=old_number)

    except ValueError:
        error_message = "Please enter just INTEGER numbers separated by spaces"
        view.display_result(result=error_message)
