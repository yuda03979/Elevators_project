import pygame as pg

from settings import *
from source import *
from functions_and_settings import *


class Elevator:

    def __init__(self, x, y, floor_0):
        self.queue = []
        self.x = x
        self.y = y
        self.img_elevator = pg.transform.scale(pg.image.load(IMG_ELEVATOR), IMG_ELEVATOR_SCALE)
        self.last_used = floor_0


    def get_arivel_time(self, floor):
        """
        return: how much time will take to arrive into the floor
        """
        if self.queue:
            return self.queue[-1].timer.get_timer() + self.distance_betwin_floors(self.queue[-1].floor_number, floor.floor_number) + WAITING_TIME
        return self.last_used.timer.get_timer() + self.distance_betwin_floors(self.last_used.floor_number, floor.floor_number) + WAITING_TIME
        

    def update_last_used(self):
        if self.queue:
            if self.last_used.timer.get_timer() <= -2:
                self.last_used.release_floor()
                self.last_used = self.queue.pop(0)


    def update_indexes(self, time_past):
        if self.y > self.last_used.y and self.y - (time_past / SPEED)  < self.last_used.y:
            self.y = self.last_used.y
        elif self.y < self.last_used.y and self.y + (time_past / SPEED)  > self.last_used.y:
            self.y = self.last_used.y
        elif self.y > self.last_used.y:
            self.y -= time_past / SPEED
        elif self.y < self.last_used.y:
            self.y += time_past / SPEED
        #pg.mixer.Sound(DING).play()
        


    def drow_elevator(self, screen):
        screen.blit(self.img_elevator, (int(self.x),int(self.y)))
        
    
    def distance_betwin_floors(self, number_floor_1:int, number_floor_2:int):
        """
        param: number_floor_1 -> the number of begining floore
        param: number_floor_2 -> the number of ending floore
        return:int -> the time its takes

        makes it positive number
        """
        floors_distance = number_floor_1 - number_floor_2
        floors_distance = floors_distance if floors_distance > 0 else floors_distance * -1
        time_distance = self.convert_floors_to_time(floors_distance)
        return time_distance
    

    def convert_floors_to_time(self, floors_distance:int):
        """
        param: floors_distance -> the distance betwin 2 floors
        return: type(int) -> the time its take

        gets the speed of the elevator on settings.py
        """
        # floors_distance *= FLOOR_SIZE[1]
        return floors_distance * ELEVATOR_SPEED_PER_FLOOR

