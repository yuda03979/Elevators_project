from settings import *
from source import *


# (x, y)

ELEVATOR_SPEED_PER_FLOOR = 0.5

WAITING_TIME = 2

FLOOR_SIZE = (floor_height * 3, floor_height)

BLACK_LINE_SCALE = (FLOOR_SIZE[0], 7)

FLOOR_IMG_SCALE = (FLOOR_SIZE[0], FLOOR_SIZE[1] - BLACK_LINE_SCALE[1])

SHOW_BUTTON_SCALE = (FLOOR_SIZE[1], FLOOR_SIZE[1])

TIMER_SIZE = (FLOOR_SIZE[1] * 2, FLOOR_SIZE[1])

ELEVATOR_SIZE = (FLOOR_SIZE[1], FLOOR_SIZE[1])

IMG_ELEVATOR_SCALE = (ELEVATOR_SIZE[0], ELEVATOR_SIZE[1])

WORLD_SIZE = [(50 * 4) + (BUILDING_NUMBERS * 250) + (sum(ELEVATOR_NUMBER_ARRAY) * ELEVATOR_SIZE[0]), 100 +(max(FLOOR_NUMBER_ARRAY) * 50)]

SCREEN_SIZE = (1500 if 1000 < WORLD_SIZE[0] else WORLD_SIZE[0], 1000 if 800 < WORLD_SIZE[1] else WORLD_SIZE[1]) 

FIRST_BUILDING_BOTTOM_LEFT = (50 * 4, WORLD_SIZE[1] - 100)






DEFINE_BUTTON = False # False if only the button True for all floor

BACKGROUND = (255, 255, 255)

BLACK = (0, 0, 0)

SPEED = 1 / (FLOOR_SIZE[1] / ELEVATOR_SPEED_PER_FLOOR) #warning!!! devision by zero



def check_settings():
    if BUILDING_NUMBERS < 1:
        print("not enough buildingd")
        return False
    if min(FLOOR_NUMBER_ARRAY) < 2:
        print("num of floors must be > 1")
        return False
    if min(ELEVATOR_NUMBER_ARRAY) < 1:
        print("num of floors must be > 0")
        return False
    if len(FLOOR_NUMBER_ARRAY) != BUILDING_NUMBERS:
        print("len of floors array must be == number of buildings")
        return False
    if len(ELEVATOR_NUMBER_ARRAY) != BUILDING_NUMBERS:
        print("len of floors array must be == number of buildings")
        return False
    if max(FLOOR_NUMBER_ARRAY) > 100:
        print("to much floors")
        return False
    if max(ELEVATOR_NUMBER_ARRAY) > 100:
        print("to much floors")
        return False
    return True
