import ui

def strInputToBool(message):
    string = ""
    while True:
        string = ui.inputField(message).lower()

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
            integer = int(ui.inputField(message))
            break
        except:
            pass
    return integer