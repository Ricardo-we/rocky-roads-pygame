import pygame
from utils.colors import colors
from objects.TileMap import TileMap
from objects.Player import Player

pygame.init()

FPS = 60
SCREEN_SIZE = (800, 500)
BACKGROUND_IMAGE = pygame.image.load("assets/Rocky Roads/background1.png")
RESIZED_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, SCREEN_SIZE)

running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN_SIZE)
tile_map = TileMap(screen, "maps/map.txt")
player = Player(tile_map, screen, x=40, y=60)

pygame.display.set_caption("Rocky roads")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

    delta_time = clock.tick(FPS)/1000
    screen.fill(colors["LIGHT_BLUE"])
    screen.blit(RESIZED_IMAGE, (0, 0))
    tile_map.map_tiles()
    player.update()
    pygame.display.flip()
    clock.tick(FPS)
