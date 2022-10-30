import os
import pygame
from objects.TileMap import TileMap
from utils.collisions import get_multiple_collisions
from utils.colors import colors


class Player(pygame.sprite.Sprite):
    def __init__(self, map: TileMap, screen: pygame.surface.Surface, x=0, y=0, width=40, height=40,):
        super().__init__()
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "texture-tiles", "slime.png")),
            (width, height),
        )
        self.screen = screen
        self.map = map
        self.horizontal_speed = 5
        self.gravity_strength = 5
        self.jump_strength = 20
        self.motion = pygame.Vector2(0, 0)
        self.flip_animation()

    def dash(self, direction_val=-1):
        self.motion.x = 10*direction_val
        return True
        # return False

    def apply_gravity(self):
        self.motion.y += self.gravity_strength
        self.rect.y += self.motion.y

    def flip_animation(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def move(self, delta=0.1):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_d]:
            if key_pressed[pygame.K_SPACE] and self.dash(1):
                pass
            else:
                self.motion.x = 1
            # self.flip_animation()
        elif key_pressed[pygame.K_a]:
            if key_pressed[pygame.K_SPACE] and self.dash(-1):
                pass
            else:
                self.motion.x = -1
            # self.flip_animation()
        else:
            self.motion.x = 0

        if self.motion.y == 0 and key_pressed[pygame.K_w]:
            self.motion.y = -self.jump_strength

        self.rect.x += self.motion.x * self.horizontal_speed
        self.screen.blit(self.image, self.rect)

    def check_y_collisions(self):
        player_collisions = get_multiple_collisions(self.rect, self.map.tiles_data)
        for tile in player_collisions:
            if self.motion.y > 0:
                self.rect.bottom = tile.top
                self.motion.y = 0
            elif self.motion.y < 0:
                self.rect.top = tile.bottom
                self.motion.y = 0

    def check_x_collisions(self):
        player_collisions = get_multiple_collisions(self.rect, self.map.tiles_data)
        for tile in player_collisions:
            if self.motion.x > 0:
                # print("FORWARD COLLISION",self.rect.right, tile.left + self.rect.width)
                self.rect.right = tile.left
                self.motion.x = 0
            elif self.motion.x < 0:
                # print("BACKWARDS COLLISION",self.rect.left, tile.right)
                self.rect.left = tile.right
                self.motion.x = 0

    def update(self):
        self.move()
        self.check_x_collisions()
        self.apply_gravity()
        self.check_y_collisions()
