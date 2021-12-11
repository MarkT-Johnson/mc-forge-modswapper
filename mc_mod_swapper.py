# Tool for automatically loading mods into minecraft forge
import logging
import datetime
import os
from pathlib import Path

# Constants
LOG_PATH = Path.cwd()
HOME = str(Path.home())
MODS_FOLDER = Path(HOME + "AppData/Roaming/.minecraft/mods")

def main_console():
    _cls()
    print("Welcome to the minecraft mod swapper, a python script designed to remove some of " \
          "the hassle with swapping out mods\n")

    # Main menu loop
    while(True):
        log.debug("Entered menu loop")
        choice = input("What would you like to do?:\n" \
                       "1) Swap current package\n" \
                       "2) Add new mod\n" \
                       "3) Create new package\n" \
                       "4) Configure options\n" \
                       "5) Exit\n\n" \
                       "Choose: ")

        log.debug("User chose: " + choice)

        # Determine user choice
        if choice == "1":
            log.info("User selected 'Swap current package'")
            _cls()

        elif choice == "2":
            log.info("User selected 'Add new mod'")
            _cls()

        elif choice == "3":
            log.info("User selected 'Create new package'")
            _cls()

        elif choice == "4":
            log.info("User selected 'Configure options'")
            _cls()

        elif choice == "5":
            log.info("User selected 'Exit'")
            _cls()
            break

        else:
            log.info("Could not interpret user choice: " + choice)
            _cls()
            print("Sorry, your choice could not be interpreted. Plesae choose one of the " \
                  "following by typing the number of the option you would like.")

    print("Goodbye!")

# Helper to clear the screen and keep things looking neat
def _cls():
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == "__main__":
    log_level = logging.DEBUG
    today = datetime.date.today().strftime("%Y-%m-%d")
    cwd = Path.cwd()
    log_name = "logs/" + today + ".log"
    log_file = cwd / log_name

    # If debugging, save logs to debug log instead
    if log_level == logging.DEBUG:
        log_file = cwd / "logs/debug/debug.log"

        # Delete old debug logs
        if log_file.exists():
            try:
                os.remove(str(log_file))
            except Exception as e:
                print("Error: could not remove old debug file")
                print(str(e))

    # Check if log folder exists, if not create it
    if not log_file.parent.exists():
        os.makedirs(log_file.parent)

    # Set logging basic configs
    logging.basicConfig(filename=log_file, encoding='utf-8', level=log_level)
    log = logging.getLogger(__name__)

    now = datetime.datetime.now().strftime("%H:%M:%S")
    log.info("####################### BEGINNING NEW LOGGING SESSION #######################")
    log.info("################################# " + now + " ##################################")
    
    main_console()
