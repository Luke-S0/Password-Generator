import os

def header(message):
    print(f"┌{"─"*len(message)}─────┐") # Prints the first line of box to fit the message
    print("│ " + message     + "    │") # Prints the message with space on right side to align │ with the rest of the box. 
    print(f"└{"─"*len(message)}─────┘") # Prints the last line of box to fit the message

def inputField(prompt):
    value = input(f"│ {prompt} ")
    return value

def clearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    header(f"Password Generator")