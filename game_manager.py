from functions_and_settings import *
from building import *
from accessories import *
from user_input import *
import time

class GameManager:

    def __init__(self) -> None:
        self.building_array = self.initialize_building_array()

        self.start = time.time()
        self.end = time.time()
        self.time_past = time.time()
    

    def initialize_building_array(self):
        """
        initialize building array , each building get x, y
        """
        arr = []
        updated_x, y = FIRST_BUILDING_BOTTOM_LEFT[0], FIRST_BUILDING_BOTTOM_LEFT[1]
        for building_number in range(BUILDING_NUMBERS):
            arr.append(Building(building_number, updated_x, y))
            updated_x += arr[-1].get_right_side_index()
        return arr
    

    def update_manager_timer(self):
        self.start = self.end
        self.end = time.time()
        return self.end - self.start

    def drow(self, screen, font):
        for building in self.building_array:
            building.drow_building(screen, font)
    
    def update(self, mouse_pos):
        self.time_past = self.update_manager_timer() # need the time that past for calculate the timer and the elevator moovmenet

        for building in self.building_array:
            building.update_building(self.time_past)
    

    def read_user_input(self, event):
            if event.type == pg.MOUSEBUTTONDOWN:
                for building in self.building_array:
                    building.check_user_input(event)