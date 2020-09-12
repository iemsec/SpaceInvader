import pygame
from laser import Laser


class Ship:
    COOLDOWN = 10

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        # test rectangle
        #pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.w, self.h))
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def get_ship_width(self):
        return self.ship_img.get_width()

    def get_ship_height(self):
        return self.ship_img.get_height()

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self, vel):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img, vel)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers[:]:
            laser.move(vel)
            if laser.off_screen(750):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)
