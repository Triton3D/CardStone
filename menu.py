import pygame
import sys

pygame.init()

size = width, height = 640, 480

black = 0, 0 ,0
white = 255, 255, 255
red = 255, 0, 0


def menu_button(screen,posx=0,posy=0,text="Button",active=False):
    screen.draw.rect
    


screen = pygame.display.set_mode(size)



while 1:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    screen.fill(white)
    pygame.display.flip()
