import secrets
import string

version = "1.0.1"

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

upper = strInputToBool("Uppercase?")
lower = strInputToBool("Lowercase?")
numbers = strInputToBool("Numbers?")
symbols = strInputToBool("Symbols/punctuation?")
length = getIntInput("Length")

pool = ""
if upper: pool += string.ascii_uppercase
if lower: pool += string.ascii_lowercase
if numbers: pool += string.digits
if symbols: pool += string.punctuation

pw = ""
for i in range(length):
    pw += secrets.choice(pool)

print(pw)