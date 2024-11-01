# Packages
import pygame
from constants import *

#Main 
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color = (0,0,0))
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')


#Ensuring that main can't be run as a module
if __name__ == "__main__":
    main()

