#encoding: utf-8
import pygame
import sys

# Constants
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480

# Colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0 ,0




#############################################################################


def main():
    
    print("Запуск игры")
    initialisation()
    
    while True:
        
        get_events()
        
        update()
        
        draw()
    

def initialisation():
    print("Инициализация игры")
    global DISPLAY, GAME_SCREEN, LOCATION
    global FONT,EVENT,MENU_ITEMS,MENU_ACT_ITEM,FPSCLOCK
    global FPS
    pygame.init()
    DISPLAY = pygame.display
    GAME_SCREEN = DISPLAY.set_mode(WINDOW_SIZE)
    DISPLAY.set_caption('CardStone')
    FONT = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 18)
    LOCATION = 'menu'
    MENU_ACT_ITEM = 0
    MENU_ITEMS = {0:'START', 1:'SETTINGS',2:'EXIT'}
    FPSCLOCK = pygame.time.Clock()
    EVENT='None'
    FPS = 10
    print(MENU_ACT_ITEM)
    
def get_events():
    global EVENT
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game_exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                EVENT = 'DOWN'
                
            if event.key == pygame.K_UP:
                EVENT = 'UP'
            if event.key == pygame.K_RETURN:
                EVENT = 'ENTER'     
        elif event.type == pygame.KEYUP:
            EVENT = 'None'
                
def update():
    global MENU_ACT_ITEM,LOCATION,MENU_ITEMS
    
    if LOCATION == 'menu':
        if EVENT == 'DOWN':
            MENU_ACT_ITEM+=1
            
        elif EVENT == 'UP':
            MENU_ACT_ITEM-=1

        elif EVENT == 'ENTER':
            if MENU_ITEMS[MENU_ACT_ITEM]=='EXIT':
                game_exit()
                
        if MENU_ACT_ITEM < 0:
            MENU_ACT_ITEM = 0
            
        elif MENU_ACT_ITEM > (len(MENU_ITEMS)-1):
            MENU_ACT_ITEM = len(MENU_ITEMS)-1

            
    
    
    if LOCATION == 'game':
        pass
    
def draw():
    
    GAME_SCREEN.fill(WHITE)
    menu(MENU_ITEMS,MENU_ACT_ITEM)
    DISPLAY.flip()
    FPSCLOCK.tick(FPS)
def game_exit():
    print("Завершение игры")
    pygame.quit()
    sys.exit()
   
def menu(items,act_item):
    
    for i in items:
        if i == act_item:
            color = RED
        else:
            color = BLACK
        menuItemSrf = FONT.render(items[i], True, color)
        menuItemRect = menuItemSrf.get_rect()
        menuItemRect.topleft = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2 - (50+10)*(len(items)- i))  
        GAME_SCREEN.blit(menuItemSrf,menuItemRect)
        
if __name__ == "__main__":
    main()


