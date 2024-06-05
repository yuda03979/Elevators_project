import pygame as pg

from functions_and_settings import *
from timer import *
from show_button import *
from button import *

class Floor:

    def __init__(self, floor_number:int, x:int, y:int) -> None:
        """
        get x, y from building
        """

        self.floor_number = floor_number
        self.x = x
        self.y = y

        self.occupied = False #if elevator in the floor or on the way to the floor

        self.timer = Timer(self.x, self.y)
        self.button = Button(self.x, self.y)
        self.show_button = ShowButton(self.floor_number, self.x, self.y)
        
        self.img_brakes_wall = pg.transform.scale(pg.image.load(IMG_BRAKES_WALL), FLOOR_IMG_SCALE)
        self.black_img = pg.transform.scale(pg.image.load(BLACK_IMAGE), BLACK_LINE_SCALE)

    
    def drow_floor(self, screen, font):
        screen.blit(self.img_brakes_wall, (self.x, self.y + BLACK_LINE_SCALE[1]))
        screen.blit(self.black_img, (self.x, self.y))
        self.timer.drow_timer(screen, font)
        self.show_button.drow_show_button(screen, font)

    def update_floor(self, time_past:float):
        self.show_button.update_show_button(self.timer.if_timer_positive()) # if timer positive, thats mean elevator on the way, so the button is green. else button is grey
        self.timer.update_timer(time_past)

    def occupied_floor(self, arrival_time):
        self.occupied = True
        self.timer.set_timer(arrival_time)
        self.show_button.change_show_button_to_green()

    def release_floor(self):
        self.occupied = False

    def check_user_input(self, event):
        if not self.occupied:
            if self.button.check_user_input(event):
                return True