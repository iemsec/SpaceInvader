import pygame
import os
import time
import random

from ship import Ship
from player import Player
from enemy import Enemy
from laser import Laser


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

COLOR_MAP = {
    "red":(RED_SPACE_SHIP,RED_LASER),
    "green":(GREEN_SPACE_SHIP,GREEN_LASER),
    "blue":(BLUE_SPACE_SHIP,BLUE_LASER)
            }

def main():
    run = True
    fps = 60
    level = 0
    lives = 5
    main_font= pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    # Define enemies
    enemies = []
    wave_length = 5

    player_vel = 5

    # define the player
    player = Player(300, 650, YELLOW_SPACE_SHIP, YELLOW_LASER)

    lost = False
    lost_count = 0

    clock = pygame.time.Clock()

    def redraw_window():
        # display background
        WIN.blit(BG, (0, 0))
        # draw text
        lives_label = main_font.render(f"Lives : {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level : {level}", 1, (255, 255, 255))
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        # draw enemies
        for enemy in enemies:
            enemy.draw(WIN)

        # draw ship
        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("Rage quit now looser !!!", 1, (255, 255, 255))
            WIN.blit(lost_label,(WIDTH//2 - lost_label.get_width()//2, HEIGHT//2))

        pygame.display.update()

    while run:
        clock.tick(fps)
        redraw_window()

        if lives <= 0 or player.health < 0:
            lost = True
            lost_count += 1
            if lost:
                if lost_count > fps * 3:
                    run = False
                else:
                    continue

        if len(enemies)==0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                color = random.choice(tuple(COLOR_MAP.keys()))
                x = random.randint(0, WIDTH-100)
                y = random.randint(-1500, 0)
                vel = random.randint(1, 4)
                enemies.append(Enemy(x, y, (COLOR_MAP[color]), vel))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # move enemies
        for enemy in enemies[:]:
            enemy.move()
            enemy.move_lasers(enemy.vel, player)
            if enemy.y + enemy.get_ship_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(player_vel, enemies)
        # method get_pressed return a dict of all key if pressed or not
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # move with player_vel until reach origin it can do last move to reach 0
            if player.x - player_vel > 0:
                player.x -= player_vel
            else:
                player.x = 0
        if keys[pygame.K_RIGHT]:
            if player.x < WIDTH - player.get_ship_width():
                player.x += player_vel
            else:
                player.x = WIDTH - player.get_ship_width()
        if keys[pygame.K_UP]:
            if player.y - player_vel > 0:
                player.y -= player_vel
            else:
                player.y = 0
        if keys[pygame.K_DOWN]:
            if player.y < HEIGHT - player.get_ship_height():
                player.y += player_vel
            else:
                player.y = HEIGHT - player.get_ship_height()
        if keys[pygame.K_SPACE]:
            player.shoot(-player_vel)


if __name__ == '__main__':
    main()

