import sys
import pygame
from demo_pygame.src.main.Game import Game

g = Game()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
