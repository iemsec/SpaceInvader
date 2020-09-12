import pygame
from ship import Ship
import config as conf

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

    def listen_event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.x - self.vel > 0:
                self.x -= self.vel
            else:
                self.x = 0
        if keys[pygame.K_RIGHT]:
            if self.x < conf.WIDTH - self.get_ship_width():
                self.x += self.vel
            else:
                self.x = conf.WIDTH - self.get_ship_width()
        if keys[pygame.K_UP]:
            if self.y - self.vel > 0:
                self.y -= self.vel
            else:
                self.y = 0
        if keys[pygame.K_DOWN]:
            if self.y < conf.HEIGHT - self.get_ship_height():
                self.y += self.vel
            else:
                self.y = conf.HEIGHT - self.get_ship_height()
            if self.x - self.vel > 0:
                self.x -= self.vel
            else:
                self.x = 0
        if keys[pygame.K_RIGHT]:
            if self.x < conf.WIDTH - self.get_ship_width():
                self.x += self.vel
            else:
                self.x = conf.WIDTH - self.get_ship_width()
        if keys[pygame.K_UP]:
            if self.y - self.vel > 0:
                self.y -= self.vel
            else:
                self.y = 0
        if keys[pygame.K_DOWN]:
            if self.y < conf.HEIGHT - self.get_ship_height():
                self.y += self.vel
            else:
                self.y = conf.HEIGHT - self.get_ship_height()
        if keys[pygame.K_SPACE]:
            self.shoot(-self.vel)