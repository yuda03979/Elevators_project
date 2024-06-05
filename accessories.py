from settings import *
import pygame as pg
import random
from settings import *
from functions_and_settings import *


NUMBER_OF_CLOUDS = 3


class Accessories:
    
    def __init__(self):
        self.array_clouds = [Cloud() for i in range(NUMBER_OF_CLOUDS)]
        self.ground = Ground()
        self.car = Car()
    
    def update_accessories(self, mouse_pos):
        [i.update_indexes(mouse_pos) for i in self.array_clouds]
        self.car.update_indexes(mouse_pos)
    
    def plot_accessories(self, screen):
        [i.plot_cloud(screen) for i in self.array_clouds]
        self.ground.plot_ground(screen)
        self.car.plot_car(screen)

class Cloud:

    def __init__(self) -> None:
        self.cloud_img = pg.transform.scale(pg.image.load(CLOUD_IMG), ((SCREEN_SIZE[1] // 20) * 1.5, SCREEN_SIZE[1] // 20))
        self.x = random.randint(0, SCREEN_SIZE[0])
        self.y = random.randint(0, SCREEN_SIZE[1] // 5)
    
    def plot_cloud(self, screen):
        screen.blit(self.cloud_img, (int(self.x), int(self.y)))

    def update_indexes(self, mouse_pos):
        add_x = -1 if mouse_pos[0] < self.x else 1 #(self.x - mouse_pos[0]) * -1
        self.x += add_x * 0.05 #(add_x / 500)
        self.x = self.x % SCREEN_SIZE[0]
    

class Ground:

    def __init__(self) -> None:
        self.ground_img = pg.transform.scale(pg.image.load(GROUND), (SCREEN_SIZE[0], FIRST_BUILDING_BOTTOM_LEFT[1] + SCREEN_SIZE[1]))
        self.x = 0
        self.y = SCREEN_SIZE[1] - FIRST_BUILDING_BOTTOM_LEFT[1] + SCREEN_SIZE[1] + FLOOR_SIZE[1]

        self.floor_area = pg.Rect(self.x, self.y, SCREEN_SIZE[0], 3) # rect floor for man
    
    
    def plot_ground(self, screen):
        screen.blit(self.ground_img, (self.x, self.y))


class Car:

    def __init__(self) -> None:
        self.car_img = pg.transform.scale(pg.image.load(CAR_IMG), (FLOOR_SIZE[1], FLOOR_SIZE[1] * 0.5))
        self.x = 0
        self.y = SCREEN_SIZE[1] - FIRST_BUILDING_BOTTOM_LEFT[1] + SCREEN_SIZE[1] + FLOOR_SIZE[1] * 0.5
    
    def plot_car(self, screen):
        screen.blit(self.car_img, (int(self.x), int(self.y)))

    def update_indexes(self, mouse_pos):
        add_x = (self.x - mouse_pos[0]) * -1
        self.x += add_x / 100
        self.x = self.x % SCREEN_SIZE[0]