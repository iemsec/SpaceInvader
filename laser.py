import pygame
import ship
import config as conf
import player

class Laser:
    def __init__(self, x, y, img, vel, obj):
        self.x = x
        self.y = y
        self.img = img
        self.vel =vel
        self.mask = pygame.mask.from_surface(self.img)
        self.counting_image = 0
        self.is_player = isinstance(obj, player.Player)

    def draw(self, window):
        if self.is_player:
            if self.counting_image % 2 == 0 and self.counting_image % 3 == 0:
                self.img = conf.YELLOW_LASER
            elif self.counting_image % 2 == 0:
                self.img = conf.YELLOW_LASER_BRIGHT
            else:
                self.img = conf.YELLOW_LASER_WHITE
            self.counting_image += 1
        window.blit(self.img, (self.x, self.y))

    def move(self):
        self.y += self.vel

    def off_screen(self):
        return not(self.y > 0 and self.y < conf.HEIGHT)

    def collision(self, obj):
        if isinstance(obj, ship.Ship) or isinstance(obj, Laser):
            offset_x = obj.x - self.x
            offset_y = obj.y - self.y
            return self.mask.overlap(obj.mask, (offset_x, offset_y)) != None
