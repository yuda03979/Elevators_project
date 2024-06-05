from functions_and_settings import *


import pygame as pg
import sys



def gui(game_manager:object):

    pg.init()
    pg.font.init()
    screen = pg.display.set_mode(SCREEN_SIZE)
    clock = pg.time.Clock()
    font = pg.font.Font(FONT, FLOOR_SIZE[1] // 3)


    # here initialize items


    while True:
        clock.tick(60)
        screen.fill(BACKGROUND)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            # here update index of items if depends on input
            game_manager.read_user_input(event)
        
        # here plot everything
        game_manager.update(pg.mouse.get_pos())
        game_manager.drow(screen, font)        
    
        pg.display.update()