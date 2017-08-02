import pygame, sys
from pygame.locals import *
from player import Player
from bullet import Bullet
import random
import math
import time

pygame.init()

#FPS
FPS = 35
fpsClock = pygame.time.Clock()

#Colors
BLACK = (  0,   0,   0, 255)
WHITE = (255, 255, 255, 255)
RED   = (255,   0,   0 , 255)
GREEN = (  0, 255,   0, 255)
BLUE  = (  0,   0, 255, 255)

#Screen
(width, height) = (700,700)
screen = pygame.display.set_mode((width,height))

#Sprite groups
players = pygame.sprite.Group()
bullets = pygame.sprite.Group()

#Game initialization
def init(numPlayers):
    # This is a list of every sprite.
    for i in range(numPlayers):
        x = random.randint(50,650)
        y = random.randint(50,650)
        player = Player(x,y,RED)
        players.add(player)

def detectHit(bullet, player):
    return player.x < bullet.rect.x < player.x + player.radius and player.y < bullet.rect.y < player.y + player.radius

def gameLoop():
    init(1)
    #Background used when clearing sprites at end of gameloop
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)
    screen.blit(background, (0,0))
    last_bullet = 0
    while True:
        screen.fill(BLACK)
        pressed = pygame.key.get_pressed()
        for player in players:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    # if( pygame.key.get_pressed()[pygame.K_UP] != 0 ):
            if pressed[K_SPACE] and time.time() - last_bullet > .7:
                # Fire a bullet if the user clicks the mouse button
                last_bullet=time.time()
                bullet = Bullet(player.theta)

                # Set the bullet so it is where the player is
                bullet.rect.x = player.x + math.cos(math.radians(player.theta)) * (player.radius + player.gun_length -10)
                bullet.rect.y = player.y + math.sin(math.radians(player.theta)) * (player.radius + player.gun_length-10)

                # Add the bullet to the lists
                bullets.add(bullet)

            #For testing purposes
            if pressed[K_RIGHT]:
                player.rotate(False)
            if pressed[K_LEFT]:
                player.rotate(True)
            if pressed[K_UP]:
                player.translate(True)
            if pressed[K_DOWN]:
                player.translate(False)
            for bullet in bullets:
                # See if bullet hits player
                if detectHit(bullet, player):
                    bullets.remove(bullet)
                    print("HIT")
                    player.health -= 5;
                    if (player.health <= 0):
                        players.remove(player)

                # Remove the bullet if it flies off the screen
                if bullet.rect.y < -10 or bullet.rect.y > height + 10 or bullet.rect.x < -10 or bullet.rect.x > width + 10:
                    bullets.remove(bullet)

        #CUD (Clear, Update, Display)
        players.clear(screen,background)
        bullets.clear(screen,background)
        players.update()
        bullets.update()
        players.draw(screen)
        bullets.draw(screen)
        pygame.display.update()

        fpsClock.tick(FPS)

#Run game
gameLoop()
