import pygame, sys, math
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self, theta):
        # Call the parent class (Sprite) constructor
        super(Bullet, self).__init__()
        self.radius = 5
        self.image = pygame.Surface([10, 10])
        # pygame.draw.circle(self.image, WHITE, (self.radius, self.radius), self.radius)
        self.theta = theta
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.y += math.sin(math.radians(self.theta)) * 30
        self.rect.x += math.cos(math.radians(self.theta)) * 30
        self.draw()

    def draw(self):
        pygame.draw.circle(self.image, (255, 255, 255, 255), (5,5), self.radius)
