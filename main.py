"""
main.py is responsible for presenting the menu screen and handling user input to launch different modules of the software suite.
It imports modules to allow the menu to be a main menu for various software.
At present, only converter.py is functional.
Please refer to github and gitlab pages for future updates!
- Rotting Deputy aka Nexanoth
"""

import os, sys, time
import random
import converter  # Assumes converter.py is in the same directory
import to_do # Assumes to_do.py is in the same directory
from fun_facts import fun_facts

## Function for aestheic slow typing simulation
def slowprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

# Function for clearing screen. Aesthetic and also helps to ensure users read error messages. 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear()
    slowprint("+-+-+-+-+-+-+-+-+-+-+\n")
    slowprint("      MAIN  MENU     \n")
    slowprint("+-+-+-+-+-+-+-+-+-+-+\n")
    slowprint("1. converter.py\n")
    slowprint("2. map_maker.py [WIP]\n")
    slowprint("3. to_do.py [WIP]\n")
    slowprint("4. Option [WIP]\n")
    slowprint("z. Quit [or ENTER]\n")
    handler()

def return_option():
    slowprint("+-+-+-+-+-+-+-+-+-+-+\n")
    slowprint("Return to main menu?\n")
    x = input("1. Yes\nANY for no\n> ")
    if x == str(1):
        slowprint("Returning to main menu...")
        menu()
    else:
        clear()
        quit_message()
        quit()

def quit_message():
    slowprint("Software shutdown initiated...\n")
    fact = random.choice(fun_facts)
    slowprint(f"Did you know {fact}?\n")
    slowprint("\nGoodbye!\n")
    input()
    clear()
    quit()

def handler():
    x = input("> ")
    if x == "1":
        clear()
        slowprint("+-+-+-+-+-+-+-+-+-+-+\n")
        slowprint("converter.py [In Development]\n\n")
        slowprint("converter.py will convert just about anything. For now it only takes a decimal input for conversion.\n")
        slowprint("This tool will check input against decimal, binary, octal, hex.\n")
        slowprint("Then, it will convert to the other three and print everything to the screen.\n\n")
        converter.converter(input("Enter a number to convert: "))
        slowprint("Copy before continuing...\n")
        input()
        clear()
        return_option()
    elif x == "2":
        clear()
        slowprint("+-+-+-+-+-+-+-+-+-+-+\n")
        slowprint("map_maker.py [In Development]\n\n")
        slowprint("map_maker.py is an attempt to create a map editor in the console.\n")
        slowprint("Users can view maps and create their own maps.\n")
        slowprint("Software will also compare indexes of maps and ask for definitions on differences.\n\n")
        slowprint("Return to main menu?\n1. Yes\nANY for no\n")
        x = input("> ")
        if x == "1":
            slowprint("Returning to main menu...")
            menu()
        else:
            clear()
            quit_message()
    elif x == "3":
        clear()
        slowprint("+-+-+-+-+-+-+-+-+-+-+\n")
        slowprint("to_do.py [In Development]\n")
        slowprint("to_do.py is a simple to-do list manager.\n")
        slowprint("Entries will be saved to todo.md in the current directory.\n\n")
        slowprint("Return to main menu?\n1. Yes\nANY for no\n")
        x = input(">")
        if x == "1":
            slowprint("Returning to main menu...")
            clear()
            menu()
        else:
            clear()
            quit_message()
    elif x == "4":
        clear()
        slowprint("+-+-+-+-+-+-+-+-+-+-+\n")
        slowprint("Option 4\n")
        slowprint("Return to main menu?\n1. Yes\nANY for no\n")
        x = input()
        if x == "1":
            slowprint("Returning to main menu...")
            clear()
            menu()
        else:
            clear()
            quit_message()
    elif x == "z":
        clear()
        quit_message()
    elif str(x) == "":
        clear()
        quit_message()

def main():
    menu()

if __name__ == "__main__":
    # code that should only run when executing converter.py directly
    main()
