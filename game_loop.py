import pygame, sys
from pygame.locals import *
import random
import math

pygame.init()

#FPS
FPS = 35
fpsClock = pygame.time.Clock()

#angular constant
rotate_delta = 10
#translational constant
translate_delta = 5

#Colors
BLACK = (  0,   0,   0, 255)
WHITE = (255, 255, 255, 255)
RED   = (255,   0,   0 , 255)
GREEN = (  0, 255,   0, 255)
BLUE  = (  0,   0, 255, 255)

#Screen
(width, height) = (700,700)
screen = pygame.display.set_mode((width,height))

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
        self.canvas = pygame.Surface((self.radius*2 + self.gun_length-self.radius,self.radius*2))
        self.canvas.fill(WHITE)
        
    def draw(self):
        self.intify()
        center = self.canvas.get_rect(center=(self.x, self.y))
        self.canvas = pygame.Surface((self.radius*2 + self.gun_length-self.radius,self.radius*2))
        pygame.draw.circle(self.canvas, self.color, (self.radius, self.radius), self.radius)
        pygame.draw.rect(self.canvas, BLUE, (self.radius,self.radius-self.gun_width/2,self.gun_length,self.gun_width))
        self.canvas = pygame.transform.rotate(self.canvas, -self.theta)
        screen.blit(self.canvas, center)

    def clamp(self):
        if self.x < self.radius:
            self.x = self.radius
        if self.x > width-self.radius:
            self.x = width-self.radius
        if self.y < self.radius:
            self.y = self.radius
        if self.y > width-self.radius:
            self.y = width-self.radius

    def intify(self):
        self.x=int(self.x)
        self.y=int(self.y)

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


    def shoot(self):
        # shoot out bullet in towards given thet
        return
    
    def update(self):
        self.draw()
        
    def aim(self):
        return


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self, theta):
        # Call the parent class (Sprite) constructor
        super(Bullet, self).__init__()
        self.radius = 5
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.theta = theta
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y += math.sin(math.radians(self.theta)) * 30
        self.rect.x += math.cos(math.radians(self.theta)) * 30     
        

#pygame.display.set_caption('')

players = pygame.sprite.Group()

#Game initialization
def init(numPlayers):
    screen.fill(BLACK)
    # This is a list of every sprite.
    for i in range(numPlayers):
        x = random.randint(50,650)
        y = random.randint(50,650)
        player = Player(x,y,RED)
        players.add(player)
        player.draw()
    pygame.display.update()

# This is a list of every sprite. All blocks and the player block as well.
# all_sprites_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

def detectHit(bullet, player):
    return player.x < bullet.rect.x < player.x + player.radius and player.y < bullet.rect.y < player.y + player.radius

def gameLoop():
    init(1)
    while True:
        screen.fill(BLACK)
        pressed = pygame.key.get_pressed()
        for player in players:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    # if( pygame.key.get_pressed()[pygame.K_UP] != 0 ):
            if pressed[K_SPACE]:
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet(player.theta)
                
                # Set the bullet so it is where the player is
                bullet.rect.x = player.x + math.cos(math.radians(player.theta)) * (player.radius + 4)
                bullet.rect.y = player.y + math.sin(math.radians(player.theta)) * (player.radius + 4)
                
                # Add the bullet to the lists
                bullet_list.add(bullet)
            
            #For testing purposes
            if pressed[K_RIGHT]:
                player.rotate(False)
            if pressed[K_LEFT]:
                player.rotate(True)
            if pressed[K_UP]:
                player.translate(True)
            if pressed[K_DOWN]:
                player.translate(False)
            for bullet in bullet_list:
                # See if bullet hits player
                if detectHit(bullet, player):
                    print("HIT")
                    bullet_list.remove(bullet)

                # Remove the bullet if it flies off the screen
                if bullet.rect.y < -10 or bullet.rect.y > height + 10 or bullet.rect.x < -10 or bullet.rect.x > width + 10:
                    bullet_list.remove(bullet)

        players.update()
        bullet_list.draw(screen)
        bullet_list.update()
        pygame.display.update()
        fpsClock.tick(FPS)


gameLoop()