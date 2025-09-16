"""
15/09/2025
This program is expected to convert data from one format to another.
Option 1 - Convert between Decimal, Binary, Octal, Hexadecimal; prints result of each
"""
import os, sys, time

## Function for aestheic slow typing simulation
def slowprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

# Function for clearing screen. Aesthetic and also helps to ensure users read error messages. 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



def converter(x):

    try:
        decimal = int(x)
        slowprint(f"Decimal: {decimal}\n")
        slowprint(f"Binary: {bin(decimal)[2:]}\n")
        slowprint(f"Octal: {oct(decimal)[2:]}\n")
        slowprint(f"Hexadecimal: {hex(decimal)[2:]}\n")
    except ValueError:
        slowprint("Invalid input. Please enter a valid number.\n")


if __name__ == "__main__":
    converter()
