import pygame as pg

from settings import *
from source import *
from functions_and_settings import *


class Timer:

    def __init__(self, x:int, y:int) -> None:

        self.x = x - (TIMER_SIZE[0] // 2)
        self.y = y

        self.arrival_time = -WAITING_TIME # timer: if equal 0 the elevator should be on the floor, + 2 seconds
    
    def set_timer(self, time_distance:int):
        """
        param time_distance allwase positive
        """
        self.arrival_time = time_distance
    
    def get_timer(self):
        return self.arrival_time
    

    def if_timer_positive(self):
        return True if self.arrival_time >= 0 else False
    
    def update_timer(self, time_past: int):
        """
        sub from the timer the time that past
        """
        if self.arrival_time > -2:
            self.arrival_time -= time_past

    def drow_timer(self, world: pg.surface, font: pg.font):
        if self.if_timer_positive():
            world.blit(font.render(str(round(self.arrival_time, 1)), True, (0, 0, 0)), (self.x, self.y))