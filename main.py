import ui
import datatype
import passgen

version = "1.0.2"

ui.header("Password Generator")

upper = datatype.strInputToBool("Uppercase?")
lower = datatype.strInputToBool("Lowercase?")
numbers = datatype.strInputToBool("Numbers?")
symbols = datatype.strInputToBool("Symbols/punctuation?")
length = datatype.getIntInput("Length")

pw = passgen.generatePassword(upper, lower, numbers, symbols, length)

print(pw)