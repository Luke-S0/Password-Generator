import secrets
import string
import ui
import datatype

version = "1.0.2"

# Merge buildPool with generatePassword - the pool is constructed in password generation.
def generatePassword(upper, lower, numbers, symbols, length):
    pw = ""
    pool = ""
    if upper: 
        pool += string.ascii_uppercase
        pw += secrets.choice(string.ascii_uppercase)
        
    if lower: 
        pool += string.ascii_lowercase
        pw += secrets.choice(string.ascii_lowercase)
        
    if numbers: 
        pool += string.digits
        pw += secrets.choice(string.digits)
        
    if symbols: 
        pool += string.punctuation
        pw += secrets.choice(string.punctuation)

    for i in range(length-len(pw)):
        pw += secrets.choice(pool)

    pw = list(pw)
    secrets.SystemRandom().shuffle(pw)
    pw = "".join(pw)
    return pw

ui.header("Password Generator")

upper = datatype.strInputToBool("Uppercase?")
lower = datatype.strInputToBool("Lowercase?")
numbers = datatype.strInputToBool("Numbers?")
symbols = datatype.strInputToBool("Symbols/punctuation?")
length = datatype.getIntInput("Length")

pw = generatePassword(upper, lower, numbers, symbols, length)

print(pw)