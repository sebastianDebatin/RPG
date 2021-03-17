"""
Main function of the RPG. Short game description follows as soon as title and content of the game are designed
This file is made up of two parts:
    The initiation to init all parameters that need to be initiated only once
    The while loop that runs until the game is stopped somehow
"""

import pygame
import os
from files.gamestate import gamestate
from files.game_settings import settings
import time # only for fps

##environment variables
#WIDTH, HEIGHT = 800, 800








def main():
    #constants
    FPS = 60
    SHOWFPS = True

    ##inits
    game_settings = settings()
    clock = pygame.time.Clock()
    WIN = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))#for Fullscreen: (0, 0), pygame.FULLSCREEN
    pygame.display.set_caption(game_settings.game_title)
    game_state = gamestate(WIN,pygame)

    game_state.load() # initial tile load before loop start


    ##loop
    while game_state.run:
        start_time = time.time()# for FPS calculation
        game_state.gamestate_manager()

        clock.tick(FPS)
        if SHOWFPS:
            print("FPS:" ,1/(time.time() -start_time))


    #save game 
    game_settings.save_settings()





if __name__ == "__main__":
    main()