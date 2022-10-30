import pygame
import os
from utils.colors import colors


class TileMap:
    def __init__(self, screen: pygame.surface.Surface, tile_map_path: str, tile_dimensions=30):
        super().__init__()
        self.screen = screen
        self.tile_map_path = tile_map_path
        self.tile_dimensions = tile_dimensions
        self.tiles_data = []
        self.objects_colliding = []

    def scroll_map(self):
        self.screen.scroll(self.screen.get_width() +1, 0)

    def map_tiles(self):
        self.scroll_map()
        tileMap = open(self.tile_map_path).read().split()
        for row_i, row in enumerate(tileMap):
            for col_i, col in enumerate(row):
                if col == "x":
                    texture = pygame.image.load(os.path.join("assets", "texture-tiles", "base-tilepng.png"))
                    texture = pygame.transform.scale(texture, (self.tile_dimensions, self.tile_dimensions))
                    rect = pygame.Rect(col_i * self.tile_dimensions, row_i * self.tile_dimensions,
                                       self.tile_dimensions, self.tile_dimensions)
                    self.screen.blit(texture, rect)
                    self.tiles_data.append(rect)

    def check_collisions(self, rect: pygame.Rect):
        colliding_tile = None
        for tile in self.tiles_data:
            is_colliding = tile.colliderect(rect)
            if is_colliding:
                colliding_tile = tile
        if colliding_tile:
            return colliding_tile
        return False
