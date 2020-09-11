import pygame
from ship import Ship

class Laser:
    def __init__(self, x, y, img, vel):
        self.x = x
        self.y = y
        self.img = img
        self.vel =vel
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self):
        self.y += self.vel

    def off_screen(self, height):
        return self.y > 0 and self.y < height

    def collision(self, obj):
        if obj is Ship:
            offset_x = obj.x - self.x
            offset_y = obj.y - self.y
            return