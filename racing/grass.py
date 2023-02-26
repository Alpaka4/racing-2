from config_3 import *
import pygame
class Grass(pygame.sprite.Sprite):
    def __init__(self,filename, screen):
        self.screen=screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
    def update(self):
        pass
    def draw(self):
        self.screen.blit(self.image, self.rect)
