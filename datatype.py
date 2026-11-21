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