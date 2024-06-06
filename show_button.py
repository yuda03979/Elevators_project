import pygame as pg

from settings import *
from source import *
from functions_and_settings import *


class ShowButton:

    def __init__(self, floor_number:int, x:int, y:int) -> None:
        self.color = 0 # 0 = gray, 1 = green
        self.x, self.y = x, y
        self.floor_number = floor_number
        self.green_button = pg.transform.scale(pg.image.load(BUTTON_IMG_GREEN), SHOW_BUTTON_SCALE)
        self.grey_button = pg.transform.scale(pg.image.load(BUTTON_IMG_GREY), SHOW_BUTTON_SCALE)
        self.button_color = [self.grey_button, self.green_button] #button_color[0] drow grey, [1] drow green
        #self.button_rect = pg.Rect(self.define_button_area()) # needs for putting the floor number in the middle

    def change_show_button_to_green(self):
        self.color = 1
    
    def update_show_button(self, timer_positive:bool):
        """
        if timer >= 0 then button should be green, if  timer < the
        """
        self.color = 1 if timer_positive else 0


    def drow_show_button(self, screen, font):
        screen.blit(self.button_color[self.color], (self.x, self.y))
        screen.blit(font.render(str(self.floor_number), True, (0, 0, 0)), (self.x, self.y))