import pygame

class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        #load player image and get its rect
        self.image = pygame.image.load('/home/bharadwaj/Desktop/test/AlienInvasion/images/PLAYER.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        #movement
        self.moving_right = False
        self.moving_left = False 

        self.x = float(self.rect.x) 


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
