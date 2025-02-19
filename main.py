# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *



def main():
    running = True
    black = (0, 0, 0)
    dt = 0
    framerate = 60
    pygame.init
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    time = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()

        dt = time.tick(framerate) / 1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
