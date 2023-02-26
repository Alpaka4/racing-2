from config_3 import *
import pygame
class Road(pygame.sprite.Sprite):
    def __init__(self,filename, screen,):
        self.screen=screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect(center=(400,SCREEN_HEIGHT//2))
    def update(self):
        pass
    def draw(self):
        
        self.screen.blit(self.image, self.rect)
        
