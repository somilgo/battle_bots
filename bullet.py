import pygame, sys, math
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self, theta):
        # Call the parent class (Sprite) constructor
        super(Bullet, self).__init__()
        self.radius = 5
        self.canvas = pygame.Surface([10, 10])
        # pygame.draw.circle(self.canvas, WHITE, (self.radius, self.radius), self.radius)
        self.theta = theta
        self.rect = self.canvas.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.y += math.sin(math.radians(self.theta)) * 30
        self.rect.x += math.cos(math.radians(self.theta)) * 30
