from configs import *
import pygame
import sys
from os.path import *
from pytmx.util_pygame import load_pygame
from level import Level

class Game:
    def __init__(self):
        #setup
        pygame.init()
        
        pygame.display.set_caption("Dai Chien FiFai")
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.clock = pygame.time.Clock();

        self.level = Level()

    def run (self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
