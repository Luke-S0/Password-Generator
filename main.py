import secrets
import string
import ui
import datatype

version = "1.0.2"



def buildPool(upper, lower, numbers, symbols):
    pool = ""

    if upper: 
        pool += string.ascii_uppercase
    if lower: 
        pool += string.ascii_lowercase
    if numbers: 
        pool += string.digits
    if symbols: 
        pool += string.punctuation

    return pool

def generatePassword(pool, length):
    pw = ""
    if upper: 
        pw += secrets.choice(string.ascii_uppercase)
    if lower: 
        pw += secrets.choice(string.ascii_lowercase)
    if numbers: 
        pw += secrets.choice(string.digits)
    if symbols: 
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

pool = buildPool(upper, lower, numbers, symbols)
pw = generatePassword(pool, length)

print(pw)