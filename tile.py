import pygame
from configs import *

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
		super().__init__(groups)
		self.sprite_type = sprite_type
		self.image = surface
		self.image = pygame.image.load('./pics/Stones.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)