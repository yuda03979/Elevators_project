from functions_and_settings import *


import pygame as pg
import sys



def gui(game_manager:object):

    pg.init()
    pg.font.init()
    screen = pg.display.set_mode(SCREEN_SIZE)
    clock = pg.time.Clock()

    # the font for char that on the screen
    font = pg.font.Font(FONT, FLOOR_SIZE[1] // 3)


    # here initialize items

    world = pg.Surface((WORLD_SIZE[0], WORLD_SIZE[1]))
    world.fill(BACKGROUND)


    # Variables to track the offset of the visible window within the larger world

    scroll_x, scroll_y = 0, WORLD_SIZE[1] - SCREEN_SIZE[1]
    scroll_speed = 20  # Pixels per key press


    while True:
        clock.tick(60)
        world.fill(BACKGROUND)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            game_manager.read_user_input(event, scroll_x, scroll_y)
        
        keys = pg.key.get_pressed()

        # Update scroll position based on arrow key presses
        if keys[pg.K_LEFT]:
            scroll_x = max(scroll_x - scroll_speed, 0)
        if keys[pg.K_RIGHT]:
            scroll_x = min(scroll_x + scroll_speed, WORLD_SIZE[0] - SCREEN_SIZE[0])
        if keys[pg.K_UP]:
            scroll_y = max(scroll_y - scroll_speed, 0)
        if keys[pg.K_DOWN]:
            scroll_y = min(scroll_y + scroll_speed, WORLD_SIZE[1] - SCREEN_SIZE[1])
 
        
        game_manager.update()
        game_manager.drow(world, font)  
        screen.blit(pg.transform.scale(world, WORLD_SIZE), (0, 0), (scroll_x, scroll_y, SCREEN_SIZE[0] , SCREEN_SIZE[1]))      


        pg.display.update()
