# Tool for automatically loading mods into minecraft forge
import logging
from pathlib import Path

LOG = logging.getLogger(__name__)
HOME = str(Path.home())
MODS_FOLDER = Path(HOME + "/AppData/Roaming/.minecraft/mods")

def main_console():
    print("Welcome to the minecraft mod swapper, a python script designed to take some of " \
          "the hassle with swapping out mods")
    

if __name__ == "__main__":
    main_console()
