import ui
import datatype
import passgen

version = "1.1.0"

ui.header(f"Password Generator {version}")

ui.header("Character pool")
upper = datatype.strInputToBool("Uppercase?")
lower = datatype.strInputToBool("Lowercase?")
numbers = datatype.strInputToBool("Numbers?")
symbols = datatype.strInputToBool("Symbols/punctuation?")

ui.header("Other settings")
length = datatype.getIntInput("Length")

# generate password
pw = passgen.generatePassword(upper, lower, numbers, symbols, length)

print(pw)