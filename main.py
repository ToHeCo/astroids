# Packages
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
#Main 
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field= AsteroidField()

   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:

            if player.collisions(asteroid) == True:
                print("Game Over!")
                exit(0)
            for shot in shots:
                if shot.collisions(asteroid):
                    shot.kill()
                    asteroid.split()
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #Framerate
        dt = clock.tick(FRAMES_PER_SECOND)/1000    

        



#Ensuring that main can't be run as a module
if __name__ == "__main__":
    main()

