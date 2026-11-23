import ui
import datatype
import passgen

version = "1.1.0"

def main():
    ui.header(f"Password Generator {version}")

    ui.header("Character pool")
    upper = datatype.strInputToBool("Uppercase?")
    lower = datatype.strInputToBool("Lowercase?")
    numbers = datatype.strInputToBool("Numbers?")
    symbols = datatype.strInputToBool("Symbols/punctuation?")

    ui.header("Other settings")
    length = datatype.getIntInput("Length")

    # generate password
    while True:
        print("PASSWORD")
        pw = passgen.generatePassword(upper, lower, numbers, symbols, length)
        print(pw)
        exitChoice = input("press enter to generate a new password, or type anything and then press enter to end the program")
        if exitChoice != "":
            break

try:
    main()
except KeyboardInterrupt:
    raise SystemExit