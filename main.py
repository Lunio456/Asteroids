# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print("Screen width: " + str(constants.SCREEN_WIDTH))
    print("Screen height: " + str(constants.SCREEN_HEIGHT))
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        pygame.display.flip()



if __name__ == "__main__":
    main()