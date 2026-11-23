import ui
import datatype
import passgen
import globals

def settings():
    
    # SECTION 1 - CHARACTER POOL
    
    while True:
        ui.clearScreen()
        ui.header("Character pool")
        upper = datatype.strInputToBool("Uppercase?")
        lower = datatype.strInputToBool("Lowercase?")
        numbers = datatype.strInputToBool("Numbers?")
        symbols = datatype.strInputToBool("Symbols/punctuation?")

        if not(upper) and not(lower) and not(numbers) and not(symbols):
            input("\n!! Password must have at least one type of character. Press ENTER to continue")
            pass
        else:
            
            break

    # SECTION 2 - PASSWORD LENGTH
    while True:
        ui.clearScreen()
        ui.header("Other settings")
        length = datatype.getIntInput("Length")
        minLength = sum([upper, lower, numbers, symbols])
        if length < minLength:
            input(f"\n!! Password must have at least {minLength} characters. Press ENTER to continue")
            pass
        else:
            break

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