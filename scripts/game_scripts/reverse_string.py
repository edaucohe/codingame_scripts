from scripts.game_scripts.views import ScriptTerminalView


def run():
    view = ScriptTerminalView()

    title = "REVERSE CHARACTER STRING IN GROUPS OF TWO"
    description = "Enter a character string and the script will return it " \
                  "reversed in groups of two characters. " \
                  "For exemple: good > ogdo "

    view.display_game_description(title=title, description=description)
    character_chain = view.enter_character_chain()
    character_chain_as_list = list(character_chain)

    if len(character_chain) % 2 == 1:
        length = len(character_chain) + 1
        character_chain_as_list.append(" ")
    else:
        length = len(character_chain)

    new_character_chain = ""
    for index in range(int(length / 2)):
        new_character_chain += character_chain_as_list.pop(1)
        new_character_chain += character_chain_as_list.pop(0)

    view.display_result(result=new_character_chain)
