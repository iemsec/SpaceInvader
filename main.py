import pygame
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


# just for test will be remove when implementing Game class
def collide(obj1, obj2):
    offset_x = obj1.x - obj2.x
    offset_y = obj1.y - obj2.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None or obj2.mask.overlap(obj1.mask,
                                                                                               (offset_x,
                                                                                                offset_y)) is not None


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
    while run:
        WIN.blit(conf.BG, (0, 0))
        title_label = conf.title_font.render("Press the mouse to begin...", 1, (255, 255, 255))
        WIN.blit(title_label, (conf.WIDTH // 2 - title_label.get_width() // 2, conf.HEIGHT // 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_game()


def main_game():
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

        if player.lost():
            lost_count += 1
            if lost_count > fps * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            player.level += 1
            wave_length += 5
            for i in range(wave_length):
                color = random.choice(tuple(COLOR_MAP.keys()))
                # put 7 by default having a more dynamic way will be better
                # (issue solved can't shoot blue when pop between 0 and 6)
                x = random.randint(7, conf.WIDTH - 100)
                y = random.randint(-1500, 0)
                vel = random.randint(1, 2)
                enemies.append(Enemy(x, y, (COLOR_MAP[color]), vel))

        # move enemies
        for enemy in enemies[:]:
            enemy.move()
            enemy.move_lasers(enemy.vel, player)
            if random.randint(0, 120) == 1:
                enemy.shoot(enemy.vel + 1)
            if enemy.y + enemy.get_ship_height() > conf.HEIGHT:
                player.lives -= 1
                enemies.remove(enemy)
            elif collide(player, enemy):
                player.health -= 10
                enemies.remove(enemy)

        player.move_lasers(player.vel, enemies)
        # method get_pressed return a dict of all key if pressed or not

        player.listen_event()

        # Quit on cross click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

        redraw_window(player, enemies)


if __name__ == '__main__':
    main()
