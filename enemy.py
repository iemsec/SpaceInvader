import pygame
from ship import Ship

class Enemy(Ship):

    def __int__(self, x, y, imgs, vel, health=100):
        super.__init__(x, y, health)
        self.ship_img, self.laser_img = imgs
        self.vel = vel
        print(vel)
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self):
        self.y += self.vel