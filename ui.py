import os
import globals
def header(message):
    print(f"┌{"─"*len(message)}─────┐") # Prints the first line of box to fit the message
    print("│ " + message     + "    │") # Prints the message with space on right side to align │ with the rest of the box. 
    print(f"└{"─"*len(message)}─────┘") # Prints the last line of box to fit the message

def inputField(prompt):
    for i in range(0,len(prompt.splitlines())):
        output = f"│ {prompt.splitlines()[i]} "
        if i == len(prompt.splitlines())-1: # on last line, add end = "" so that input is on the same line.
            print(output, end="")
        else:
            print(output)
    value = input()
    return value

def clearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print(f"│ {globals.name} (v{globals.version})")