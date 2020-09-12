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
    "red": (conf.RED_SPACE_SHIP, conf.RED_LASER),
    "green": (conf.GREEN_SPACE_SHIP, conf.GREEN_LASER),
    "blue": (conf.BLUE_SPACE_SHIP, conf.BLUE_LASER)
            }


def redraw_window(player, enemies):
    # display background
    WIN.blit(conf.BG, (0, 0))
    # draw text
    lives_label = conf.main_font.render(f"Lives : {player.lives}", 1, (255, 255, 255))
    level_label = conf.main_font.render(f"Level : {player.level}", 1, (255, 255, 255))
    WIN.blit(lives_label, (10, 10))
    WIN.blit(level_label, (conf.WIDTH - level_label.get_width() - 10, 10))

    # draw enemies
    for enemy in enemies:
        enemy.draw(WIN)

    # draw ship
    player.draw(WIN)

    if player.lost():
        lost_label = conf.lost_font.render("Rage quit now looser !!!", 1, (255, 255, 255))
        WIN.blit(lost_label, (conf.WIDTH // 2 - lost_label.get_width() // 2, conf.HEIGHT // 2))

    pygame.display.update()


def main():
    run = True
    fps = 60

    # Define enemies
    enemies = []
    wave_length = 5

    # init speed movement of the player
    player_vel = 6

    # define the player
    player = Player(300, 650, conf.YELLOW_SPACE_SHIP, conf.YELLOW_LASER, player_vel)
    lost_count = 0

    clock = pygame.time.Clock()

    # main loop
    while run:
        clock.tick(fps)
        redraw_window(player, enemies)

        if player.lost():
            lost_count += 1
            if player.lost():
                if lost_count > fps * 3:
                    run = False
                else:
                    continue

        if len(enemies) == 0:
            player.level += 1
            wave_length += 5
            for i in range(wave_length):
                color = random.choice(tuple(COLOR_MAP.keys()))
                # put 7 by default having a more dynamic way will be better (issue solved can't shoot blue)
                x = random.randint(7, conf.WIDTH-100)
                y = random.randint(-1500, 0)
                vel = random.randint(1, 2)
                enemies.append(Enemy(x, y, (COLOR_MAP[color]), vel))

        # move enemies
        for enemy in enemies[:]:
            enemy.move()
            enemy.move_lasers(enemy.vel, player)
            if enemy.y + enemy.get_ship_height() > conf.HEIGHT:
                player.lives -= 1
                enemies.remove(enemy)

        player.move_lasers(player.vel, enemies)
        # method get_pressed return a dict of all key if pressed or not
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # move with player_vel until reach origin it can do last move to reach 0
            if player.x - player.vel > 0:
                player.x -= player.vel
            else:
                player.x = 0
        if keys[pygame.K_RIGHT]:
            if player.x < conf.WIDTH - player.get_ship_width():
                player.x += player.vel
            else:
                player.x = conf.WIDTH - player.get_ship_width()
        if keys[pygame.K_UP]:
            if player.y - player.vel > 0:
                player.y -= player.vel
            else:
                player.y = 0
        if keys[pygame.K_DOWN]:
            if player.y < conf.HEIGHT - player.get_ship_height():
                player.y += player.vel
            else:
                player.y = conf.HEIGHT - player.get_ship_height()
        if keys[pygame.K_SPACE]:
            player.shoot(-player.vel)

        # Quit on cross click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == '__main__':
    main()
