import pygame
import os
import time
import random
from ship import Ship

pygame.font.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader")

# load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


def main():
    run = True
    fps = 60
    level = 0
    lives = 5
    main_font= pygame.font.SysFont("comicsans", 50)

    player_vel = 5

    ship = Ship(300, 650)
    clock = pygame.time.Clock()

    def redraw_window():
        # display background
        WIN.blit(BG, (0, 0))
        # draw text
        lives_label = main_font.render(f"Lives : {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level : {level}", 1, (255, 255, 255))
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        # draw ship
        ship.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(fps)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ship.x -= player_vel
        if keys[pygame.K_RIGHT]:
            ship.x += player_vel
        if keys[pygame.K_UP]:
            ship.y -= player_vel
        if keys[pygame.K_DOWN]:
            ship.y += player_vel


if __name__ == '__main__':
    main()

