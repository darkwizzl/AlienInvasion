import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_game):
        super().__init__( )
        self.screen = ai_game.screen
        #load the alien image and set its starting position
        self.image = pygame.image.load('/home/bharadwaj/Desktop/test/AlienInvasion/images/ENEMY.png')
        self.rect = self.image.get_rect()