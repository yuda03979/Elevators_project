from functions_and_settings import *
from building import *
from accessories import *
from user_input import *
import time

class GameManager:
    """
    responsebility:
    - creates buildings as the user enter
    - drow the all screen

    API:
    - drow()
    - update()
    - read_user_input()
    """

    def __init__(self) -> None:
        self.building_array = self.initialize_building_array()

        #using for timer
        self.start = time.time()
        self.end = time.time()
        self.time_past = time.time()
    

    def initialize_building_array(self) -> list[Building]:
        """
        initialize building array , each building get x, y
        """
        arr = []
        updated_x, y = FIRST_BUILDING_BOTTOM_LEFT[0], FIRST_BUILDING_BOTTOM_LEFT[1]
        for building_number in range(BUILDING_NUMBERS):
            arr.append(Building(building_number, updated_x, y))
            updated_x = arr[-1].get_right_side_index() + (TIMER_SIZE[0] * 2)
        return arr
    

    def update_manager_timer(self):
        """
        return the time past
        """
        self.start = self.end
        self.end = time.time()
        return self.end - self.start

    def drow(self, world: pg.surface, font: pg.font):
        """
        drow everything
        """
        for building in self.building_array:
            building.drow_building(world, font)
    
    def update(self):
        """
        update everything that do not needs input
        """
        self.time_past = self.update_manager_timer() # calculate the timer and the elevator moovmenet the time that past 
        for building in self.building_array:
            building.update_building(self.time_past)
    

    def read_user_input(self, event: pg.event, scrool_x: int, scrool_y: int):
            """
            update everything that require user input
            """
            if event.type == pg.MOUSEBUTTONDOWN:
                for building in self.building_array:
                    building.check_user_input(event, scrool_x, scrool_y)