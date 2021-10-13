import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)


    def run_game(self):
        while True:
            self.screen.fill(self.settings.bg) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  
            pygame.display.flip()
        
ai = AlienInvasion()
ai.run_game()
