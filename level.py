import pygame
from configs import *
from support import import_csv_layout
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):

        # for style, layout in layouts.items():
        #     for row_index,row in enumerate(layout):
        #         for col_index, col in enumerate(row):
        #             x = col_index * TILESIZE
        #             y = row_index * TILESIZE
        #             if style == 'boundary':
        #                 Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'invisible' )
        #         if col == 'x':
        #             Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
        #         if col == 'p':
        #             self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)

        self.player = Player((120, 120), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        #creating the floor
        self.floor_surf_original = pygame.image.load('./pics/Map1.png').convert()
        self.floor_rect = self.floor_surf_original.get_rect(topleft=(0,0))

        # self.zoom_factor = 1
        #
        # self.scale_floor_to_fit_screen()

    # def scale_floor_to_fit_screen(self):
    #     screen_width, screen_height = self.display_surface.get_size()
    #
    #     map_width, map_height = self.floor_surf_original.get_size()
    #
    #     # Calculate scale factor to fit screen
    #     scale_x = screen_width / map_width
    #     scale_y = screen_height / map_height
    #
    #     # Use the minimum scale factor to maintain aspect ratio
    #     scale_factor = min(scale_x, scale_y) * self.zoom_factor
    #
    #     # Scale the map image
    #     new_map_size = (int(map_width * scale_factor), int(map_height * scale_factor))
    #     self.floor_surf = pygame.transform.smoothscale(self.floor_surf_original, new_map_size)
    #
    #     # Update the floor rect for the scaled map
    #     self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))
    #
    # def set_zoom(self, zoom_factor):
    #     """ Sets a new zoom factor and rescales the floor. """
    #     self.zoom_factor = zoom_factor
    #     self.scale_floor_to_fit_screen()

    def custom_draw(self,player):

        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf_original, floor_offset_pos)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
