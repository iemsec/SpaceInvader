import pygame
from ship import Ship

class Player(Ship):

    def __init__(self,x, y, ship_img, laser_img, vel, health=100, lives=5, level=0):
        super().__init__(x, y, health=health)
        self.lives = lives
        self.level = level
        self.ship_img = ship_img
        self.laser_img = laser_img
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.vel = vel

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers[:]:
            laser.move()
            if laser.off_screen():
                self.lasers.remove(laser)
            else:
                for obj in objs[:]:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def lost(self):
        return self.lives <= 0 or self.health < 0