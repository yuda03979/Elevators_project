from game_manager import *
from gui import *
from functions_and_settings import *

def main():
    if check_settings():
        game_manager = GameManager()
        gui(game_manager)


if __name__ == '__main__':
    main()