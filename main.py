import pygame
import time
import random
import config as conf

from player import Player
from enemy import Enemy


pygame.font.init()


WIN = pygame.display.set_mode((conf.WIDTH, conf.HEIGHT))
pygame.display.set_caption("Space Invader")

COLOR_MAP = {
    "red":(conf.RED_SPACE_SHIP,conf.RED_LASER),
    "green":(conf.GREEN_SPACE_SHIP,conf.GREEN_LASER),
    "blue":(conf.BLUE_SPACE_SHIP,conf.BLUE_LASER)
            }

def redraw_window(player, enemies, lost):
    # display background
    WIN.blit(conf.BG, (0, 0))
    # draw text
    lives_label = conf.main_font.render(f"Lives : {conf.lives}", 1, (255, 255, 255))
    level_label = conf.main_font.render(f"Level : {conf.level}", 1, (255, 255, 255))
    WIN.blit(lives_label, (10, 10))
    WIN.blit(level_label, (conf.WIDTH - level_label.get_width() - 10, 10))

    # draw enemies
    for enemy in enemies:
        enemy.draw(WIN)

    # draw ship
    player.draw(WIN)

    if lost:
        lost_label = conf.lost_font.render("Rage quit now looser !!!", 1, (255, 255, 255))
        WIN.blit(lost_label, (conf.WIDTH // 2 - lost_label.get_width() // 2, conf.HEIGHT // 2))

    pygame.display.update()

def main():
    run = True
    fps = 60

    # Define enemies
    enemies = []
    wave_length = 5

    player_vel = 5

    # define the player
    player = Player(300, 650, conf.YELLOW_SPACE_SHIP, conf.YELLOW_LASER)

    lost = False
    lost_count = 0

    clock = pygame.time.Clock()

    while run:
        clock.tick(fps)
        redraw_window(player, enemies, lost)

        if conf.lives <= 0 or player.health < 0:
            lost = True
            lost_count += 1
            if lost:
                if lost_count > fps * 3:
                    run = False
                else:
                    continue

        if len(enemies)==0:
            conf.level += 1
            wave_length += 5
            for i in range(wave_length):
                color = random.choice(tuple(COLOR_MAP.keys()))
                x = random.randint(0, conf.WIDTH-100)
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
            if enemy.y + enemy.get_ship_height() > conf.HEIGHT:
                conf.lives -= 1
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
            if player.x < conf.WIDTH - player.get_ship_width():
                player.x += player_vel
            else:
                player.x = conf.WIDTH - player.get_ship_width()
        if keys[pygame.K_UP]:
            if player.y - player_vel > 0:
                player.y -= player_vel
            else:
                player.y = 0
        if keys[pygame.K_DOWN]:
            if player.y < conf.HEIGHT - player.get_ship_height():
                player.y += player_vel
            else:
                player.y = conf.HEIGHT - player.get_ship_height()
        if keys[pygame.K_SPACE]:
            player.shoot(-player_vel)



if __name__ == '__main__':
    conf.intialize(0, 5)
    main()

