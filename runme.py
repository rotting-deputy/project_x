"""
runme.py is the launcher for the software suite.
Since you downloaded the zip of the entire package, there is no need for runme.py to check for dependencies.
Please refer to github and gitlab pages for future updates!
- Rotting Deputy aka Nexanoth
"""
import sys, time, os, subprocess

# Function for clearing screen. Aesthetic and also helps to ensure users read error messages. 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# slowprint function for aesthetic typing simulation
def slowprint(str):
    import sys, time
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

def runme():
    clear()
    slowprint("+-+-+-+-+-+-+-+-+-+-+\n")
    slowprint(" runme is activated  \n")
    slowprint("+-+-+-+-+-+-+-+-+-+-+\n")
    slowprint("Checking for dependencies...\n")
    files_in_dir = os.listdir('/'.join(os.path.realpath(__file__).split(os.sep)[:-1]))
    found = []
    for item in check_list: #check_list #dummy
        if item in files_in_dir:
            found.append(item)
    if found == []:
        slowprint("No dependencies found!\n")
        input()
        slowprint("Please redownload the package from github or gitlab!\n")
        slowprint("Github site goes here\n")
        slowprint("Gitlab site goes here\n")
        slowprint("\nExiting...\n")
        input()
        quit()

    for item in found:
        slowprint(f"- {item}\n")
    slowprint("\nAll dependencies found!\n")
    slowprint("Exiting software...\n")
    input()
    quit() # Does not clear in case user wants links on screen

    if len(found) != len(check_list): #dummy # check_list for real use
        slowprint("\nError: Missing dependencies!\n")
        slowprint("Please redownload the package from github or gitlab!")
        slowprint("Github site goes here\n")
        slowprint("Gitlab site goes here\n")
        slowprint("\nExiting...\n")
        input()
        clear()
        quit()

check_list = ["main.py", "converter.py", "to_do.py", "fun_facts.py"]
dummy = []

def checkme():
    files_in_dir = os.listdir('/'.join(os.path.realpath(__file__).split(os.sep)[:-1]))
    for i in files_in_dir:
        if i in check_list:
            print(i)

runme()
#checkme()
