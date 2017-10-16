import pygame

class Card(pygame.sprite.Sprite):
    """ Base card """
    def __init__(self,iWidth,iHeight,imgCardback):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([iWidth,iHeight])
        self.image = pygame.image.load(imgCardback)
        
        self.rect = self.image.get_rect()
pygame.init()
fps=pygame.time.Clock()
screen = pygame.display.set_mode((640,480))
#screen.fill((255,255,255))
card = Card(50,100,'d:\\2.gif')

while True:
    screen.fill((255,255,255))
    screen.blit(card.image,card.rect.fit(((10,220),(50,100))))
    #card.rect=card.rect.fit((0,0),(50,100))
    pygame.display.flip()
    pygame.display.update()
    fps.tick(60)

