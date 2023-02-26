import pygame
import sys
from  config_3 import *
from  grass import Grass
from  road import Road
from car import Car
pygame.font.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
grass=Grass("grass.jpg",screen)
road=Road("road_3.png",screen)
car=Car("car.png",screen,(SCREEN_WIDTH)//2,(SCREEN_HEIGHT)//2)
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            
        
        clock.tick(FPS)
        grass.update()
        road.update()
        car.update()
        screen.fill(BLACK)
        grass.draw()

        road.draw()
        car.draw()
        pygame.display.update()
