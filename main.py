# this allows us to use code
# the open-source pygame library
# throughout this file

import pygame
from constants import *

def main():
    pygame.init()
    # print(pygame.version.ver)
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #setting delta time
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.flip()
        
        
        
        
        dt = clock.tick(60)/1000


if __name__== "__main__":
    main()