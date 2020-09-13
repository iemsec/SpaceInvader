import pygame
from ship import Ship
from laser import Laser

class Enemy(Ship):

    def __init__(self, x, y, img, vel, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = img
        self.vel = vel
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self):
        self.y += self.vel

    def shoot(self, vel):
        if self.cool_down_counter == 0:
            laser = Laser(self.x - self.ship_img.get_width() // 2, self.y, self.laser_img, vel, self)
            self.lasers.append(laser)
            self.cool_down_counter = 1