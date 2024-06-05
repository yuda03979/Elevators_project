from functions_and_settings import *
from settings import *

import pygame as pg

class Button:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        self.button_erea = pg.Rect(self.define_button_area())
    

    def define_button_area(self):
        if DEFINE_BUTTON:
            return(self.x, self.y, FLOOR_SIZE[0], FLOOR_SIZE[1])
        else:
            return(self.x, self.y, SHOW_BUTTON_SCALE[0], SHOW_BUTTON_SCALE[1])

    def check_user_input(self, event):
        """
        checks if button is not green and make the call
        """
        if self.button_erea.collidepoint(event):
            return True

