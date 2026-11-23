import ui
import datatype
import passgen

version = "1.1.0"

def main():
    ui.clearScreen()
    ui.header("Character pool")
    upper = datatype.strInputToBool("Uppercase?")
    lower = datatype.strInputToBool("Lowercase?")
    numbers = datatype.strInputToBool("Numbers?")
    symbols = datatype.strInputToBool("Symbols/punctuation?")

    ui.header("Other settings")
    length = datatype.getIntInput("Length")

    # generate password
    while True:
        ui.clearScreen()
        pw = passgen.generatePassword(upper, lower, numbers, symbols, length)
        ui.header(f"Password = {pw}")
        exitChoice = input("press enter to generate a new password, or type anything and then press enter to end the program")
        if exitChoice != "":
            break

try:
    main()
except KeyboardInterrupt:
    raise SystemExit