"""
Main function of the RPG. Short game description follows as soon as title and content of the game are designed
This file is made up of two parts:
    The initiation to init all parameters that need to be initiated only once
    The while loop that runs until the game is stopped somehow
"""

import pygame
import os
from files.gamestate import gamestate
import time # only for fps

##environment variables
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))#for Fullscreen: (0, 0), pygame.FULLSCREEN
pygame.display.set_caption("RPG")





## constants
FPS = 60
SHOWFPS = True


def main():
    ##inits
    clock = pygame.time.Clock()
    game_state = gamestate(WIN,pygame)

    game_state.load()


    ##loop
    while game_state.run:
        start_time = time.time()# for FPS calculation
        game_state.gamestate_manager()

        clock.tick(FPS)
        if SHOWFPS:
            print("FPS:" ,1/(time.time() -start_time))




if __name__ == "__main__":
    main()