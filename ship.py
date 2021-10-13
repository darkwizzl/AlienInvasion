import pygame

class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #load player image and get its rect
        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    