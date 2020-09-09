import pygame


class Ship:

    def __init__(self, x, y, w=50, h=50, health=100):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.w, self.h))

