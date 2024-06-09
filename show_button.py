import pygame as pg

from settings import *
from source import *
from functions_and_settings import *


class ShowButton:
    """
    responsible to drow the button and the floor number, including green or grey
    """

    def __init__(self, floor_number:int, x:int, y:int) -> None:
        self.color = 0 # 0 = gray, 1 = green
        self.x, self.y = x, y
        self.floor_number = floor_number
        self.green_button = pg.transform.scale(pg.image.load(BUTTON_IMG_GREEN), SHOW_BUTTON_SCALE)
        self.grey_button = pg.transform.scale(pg.image.load(BUTTON_IMG_GREY), SHOW_BUTTON_SCALE)
        self.button_color = [self.grey_button, self.green_button] #button_color[0] drow grey, [1] drow green
        self.button_rect = pg.Rect(self.x, self.y, SHOW_BUTTON_SCALE[0], SHOW_BUTTON_SCALE[1]) # needs for putting the floor number in the middle
        self.text_surface = None
        self.text_rect = None


    def change_show_button_to_green(self):
        self.color = 1
    
    def update_show_button(self, timer_positive:bool):
        """
        if timer >= 0 then button should be green, if  timer < the
        """
        self.color = 1 if timer_positive else 0


    def drow_show_button(self, world: pg.surface, font: pg.font):
        """
        drow the button and the floor number in the world
        """
        world.blit(self.button_color[self.color], (self.x, self.y))
        if not self.text_rect:
            self.text_surface = font.render(str(self.floor_number), True, BLACK)
            self.text_rect = self.text_surface.get_rect()
            self.text_rect.center = self.button_rect.center
        world.blit(self.text_surface, self.text_rect)