import pygame, sys, math
from pygame.locals import *

#angular constant
rotate_delta = 10
#translational constant
translate_delta = 5

#screen width/height (Ideally player wouldnt need )
(width, height) = (700,700)

class Player (pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, color):
        # Call the parent class (Sprite) constructor
        super(Player, self).__init__()
        self.x = xPos
        self.y = yPos
        self.health = 100
        self.color = color
        self.theta = 20
        self.radius = 20
        self.gun_length = 30
        self.gun_width = 10
        self.image = pygame.Surface((self.radius*2 + self.gun_length-self.radius,self.radius*2))
        self.rect = self.image.get_rect()

    def draw(self):
        center = self.image.get_rect(center=(self.x, self.y))
        self.image = pygame.Surface((self.radius*2 + self.gun_length-self.radius,self.radius*2))
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        pygame.draw.rect(self.image, (0, 0, 255, 255), (self.radius,self.radius-self.gun_width/2,self.gun_length,self.gun_width))
        self.image = pygame.transform.rotate(self.image, -self.theta)
        self.rect.x = center[0]
        self.rect.y = center[1]

    def clamp(self):
        if self.x < self.radius:
            self.x = self.radius
        if self.x > width-self.radius:
            self.x = width-self.radius
        if self.y < self.radius:
            self.y = self.radius
        if self.y > width-self.radius:
            self.y = width-self.radius

    def translate(self, forward):
        print("translate")
        if forward:
            self.y += math.sin(math.radians(self.theta)) * 10
            self.x += math.cos(math.radians(self.theta)) * 10
        else:
            self.y -= math.sin(math.radians(self.theta)) * 10
            self.x -= math.cos(math.radians(self.theta)) * 10
        self.clamp()

    def rotate(self, clockwise):
        print("rotate")
        if not clockwise:
            self.theta += rotate_delta
        else:
            self.theta -= rotate_delta

    # shoot out bullet in towards given theta
    def shoot(self):
        return

    #Does nothing as of now
    def update(self):
        self.draw()

    def aim(self):
        return
