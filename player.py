import pygame
from ship import Ship

class Player(Ship):

    def __init__(self,x, y, ship_img, laser_img, health=100):
        super().__init__(x, y, health=health)
        self.ship_img = ship_img
        self.laser_img = laser_img
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers[:]:
            laser.move()
            if laser.off_screen(750):
                self.lasers.remove(laser)
            else:
                for obj in objs[:]:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)

