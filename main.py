# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    running = True
    dt = 0
    framerate = 60
    pygame.init
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoot = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shoot, updatable, drawable)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)



        for asteroid in asteroids:
            if asteroid.Collisions(player):
                print("Game over!")
                sys.exit()
            for bullet in shoot:
                if asteroid.Collisions(bullet):
                    bullet.kill()
                    asteroid.split()

        pygame.display.flip()

        dt = time.tick(framerate) / 1000

if __name__ == "__main__":
    main()
