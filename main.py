import ui
import datatype
import passgen
import globals

def settings():
    ui.clearScreen()
    # SECTION 1 - CHARACTER POOL
    ui.header("Character pool")
    upper = datatype.strInputToBool("Uppercase?")
    lower = datatype.strInputToBool("Lowercase?")
    numbers = datatype.strInputToBool("Numbers?")
    symbols = datatype.strInputToBool("Symbols/punctuation?")

    # SECTION 2 - PASSWORD LENGTH
    ui.header("Other settings")
    length = datatype.getIntInput("Length")

    # RETURN NEW CONFIGURATION VALUES
    return upper, lower, numbers, symbols, length

def main():
    # PRESENT SETTINGS WHEN USER OPENS PROGRAM
    upper, lower, numbers, symbols, length = settings()
    # generate password
    while True:
        ui.clearScreen()
        pw = passgen.generatePassword(upper, lower, numbers, symbols, length)
        ui.header(f"Password = {pw}")
        action = ui.inputField("Press ENTER to regenerate\nOR type settings / exit").lower()
        if action == "":
            pass
        elif action == "settings":
            upper, lower, numbers, symbols, length = settings()
        elif action == "exit":
            break
        else:
            input("Invalid command. Press ENTER to continue")

try:
    main()
except KeyboardInterrupt:
    raise SystemExit