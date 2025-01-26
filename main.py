# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import pygame
from constants import *
import player
import asteroid
import asteroidfield
import shot

def main():
    print("Starting asteroids!")
    print("Screen width: " + str(constants.SCREEN_WIDTH))
    print("Screen height: " + str(constants.SCREEN_HEIGHT))
    pygame.init
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (updatable, drawable, shots)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player1 = player.player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = asteroidfield.AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            if a.checkCollisions(player1):
                print("Game over!")
                return
            for s in shots:
                if a.checkCollisions(s):
                    a.split()
                    s.kill()
        screen.fill("black")
        for u in drawable:
            u.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()