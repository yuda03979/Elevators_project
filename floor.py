import pygame as pg

from functions_and_settings import *
from timer import *
from show_button import *
from button import *

class Floor:
    """
    responsebility:
    - drow and update the floor, including floor background, black line, show_button, and timer
    - if floor are occupied (elevator on the way) or not 

    API:
    - drow_floor()
    - update_floor()
    - check_user_input()
    - occupied_floor()
    - release_floor()
    """

    def __init__(self, building_number:int, floor_number:int, x:int, y:int) -> None:
        """
        get x, y from building
        """

        self.building_number = building_number
        self.floor_number = floor_number
        self.x = x
        self.y = y

        #if elevator in the floor or on the way to the floor. on the begining all elevators in floor 0
        self.occupied = False if self.floor_number != 0 else True


        self.timer = Timer(self.x, self.y)
        self.button = Button(self.x, self.y) #the real button. can be the all floor or only the button
        self.show_button = ShowButton(self.floor_number, self.x, self.y) #the button that the user see
        
        #the floor background
        self.img_brakes_wall = pg.transform.scale(pg.image.load(IMG_BRAKES_WALL), FLOOR_IMG_SCALE)
        self.black_img = pg.transform.scale(pg.image.load(BLACK_IMAGE), BLACK_LINE_SCALE)

    
    def drow_floor(self, world: pg.surface, font: pg.font):
        """
        get our world and font, and responsible to drow the all floor -> floor background, black line, timer, and show_button
        """
        world.blit(self.img_brakes_wall, (self.x, self.y + BLACK_LINE_SCALE[1]))
        #if not self.floor_number == FLOOR_NUMBER_ARRAY[self.floor_number - 1] - 1:
        if self.floor_number != FLOOR_NUMBER_ARRAY[self.building_number] - 1:
            world.blit(self.black_img, (self.x, self.y))
        self.timer.drow_timer(world, font)
        self.show_button.drow_show_button(world, font)

    def update_floor(self, time_past:float):
        
        self.show_button.update_show_button(self.timer.if_timer_positive()) # if timer positive, thats mean elevator on the way, so the button is green. else button is grey
        self.timer.update_timer(time_past)

    def occupied_floor(self, arrival_time: float):
        """
        when elevator should arrive, the floor is occupied, we have a timer and the show button is green
        """
        self.occupied = True
        self.timer.set_timer(arrival_time)
        self.show_button.change_show_button_to_green()

    def release_floor(self):
        self.occupied = False

    def check_user_input(self, event: tuple):
        #return if the call should happpen 
        if not self.occupied:
            if self.button.check_user_input(event):
                return True