import secrets
import string
import ui

version = "1.0.2"

def strInputToBool(message):
    string = ""
    while True:
        string = input(message).lower()

        if string != "":
            if string[0] in ["y", "n"]:
                break
    
    if string[0] == "y":
        return True
    elif string[0] == "n":
        return False
    
def getIntInput(message):
    while True:
        try:
            integer = int(input(message))
            break
        except:
            pass
    return integer

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

upper = strInputToBool("Uppercase?")
lower = strInputToBool("Lowercase?")
numbers = strInputToBool("Numbers?")
symbols = strInputToBool("Symbols/punctuation?")
length = getIntInput("Length")

pool = buildPool(upper, lower, numbers, symbols)
pw = generatePassword(pool, length)

print(pw)