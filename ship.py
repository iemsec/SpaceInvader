import pygame


class Ship:

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

    def get_ship_width(self):
        return self.ship_img.get_width()

    def get_ship_height(self):
        return self.ship_img.get_height()
