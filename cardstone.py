#utf-8
import pygame
import sys


# Constants
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480

# Colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0 ,0

MENU_ITEMS_NEW_GAME = {0:'NEW GAME', 1:'SETTINGS', 2:'EXIT'}
MENU_ITEMS_IN_GAME = {0:'RESUME', 1:'NEW GAME', 2:'SETTINGS', 3:'EXIT'}


#############################################################################


def main():
	
	print("Game start")
	initialisation()
	
	while True:
		
		get_events()
		
		update()
		
		draw()
	

def initialisation():
	print("Game initialisation")
	global DISPLAY, GAME_SCREEN, LOCATION, GAME_STATE
	global FONT,EVENT,MENU_ITEMS,MENU_ACT_ITEM,FPSCLOCK
	global FPS,PLAYER, MENU_MESSAGE, MENU_ITEMS_RECT
	pygame.init()
	DISPLAY = pygame.display
	GAME_SCREEN = DISPLAY.set_mode(WINDOW_SIZE)
	DISPLAY.set_caption('CardStone')
	FONT = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 18)
	LOCATION = 'menu'
	MENU_ACT_ITEM = 0
	MENU_ITEMS = MENU_ITEMS_NEW_GAME
	MENU_ITEMS_RECT = []
	FPSCLOCK = pygame.time.Clock()
	EVENT='None'
	FPS = 10
	GAME_STATE = 'firstrun'
	PLAYER = 'player'
	MENU_MESSAGE = 'Welcome!'
	print(MENU_ACT_ITEM)
	
def get_events():
	global EVENT, KEY, MOUSE_POS
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			game_exit()

		elif event.type == pygame.MOUSEBUTTONDOWN:
			
			EVENT = 'MOUSE_BUTTON_DOWN'
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				EVENT = 'DOWN'
			elif event.key == pygame.K_UP:
				EVENT = 'UP'
			elif event.key == pygame.K_RETURN:
				EVENT = 'ENTER'	 
			elif event.key == pygame.K_ESCAPE:
				EVENT = 'ESC'
			elif event.key>=pygame.K_a and event.key<=pygame.K_z:
				EVENT = 'TYPE'
				KEY = event.key
			elif event.key == pygame.K_BACKSPACE:
				EVENT = 'BACKSPACE'
				
		elif event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
			EVENT = 'None'
				
def update():
	global MENU_ACT_ITEM,LOCATION,MENU_ITEMS,PLAYER, MENU_MESSAGE,MOUSE_POS
	MOUSE_POS = MOUSEX, MOUSEY = pygame.mouse.get_pos()	
	if LOCATION == 'menu':
		for item in MENU_ITEMS.keys():
			if len(MENU_ITEMS_RECT)>1:
				if MENU_ITEMS_RECT[item].collidepoint(MOUSE_POS):
					MENU_ACT_ITEM=item

		if EVENT == 'DOWN':
			MENU_ACT_ITEM+=1

			
		elif EVENT == 'UP':
			MENU_ACT_ITEM-=1

		elif EVENT == 'ENTER' or EVENT == 'MOUSE_BUTTON_DOWN':
			if MENU_ITEMS[MENU_ACT_ITEM]=='NEW GAME' or MENU_ITEMS[MENU_ACT_ITEM] == 'RESUME':
				LOCATION = 'game'
			elif MENU_ITEMS[MENU_ACT_ITEM]=='SETTINGS':
				MENU_MESSAGE = "Not working yet! Sorry"
			elif MENU_ITEMS[MENU_ACT_ITEM]=='EXIT':
				game_exit()
				
		if MENU_ACT_ITEM < 0:
			MENU_ACT_ITEM = 0
			
		elif MENU_ACT_ITEM > (len(MENU_ITEMS)-1):
			MENU_ACT_ITEM = len(MENU_ITEMS)-1

		if MENU_ITEMS[MENU_ACT_ITEM] == 'NEW GAME':
			MENU_MESSAGE = "Start new game"
		elif MENU_ITEMS[MENU_ACT_ITEM] == 'RESUME':
			MENU_MESSAGE = "Continue game"
		elif MENU_ITEMS[MENU_ACT_ITEM] == 'SETTINGS':
			MENU_MESSAGE = "Setting your game"
		elif MENU_ITEMS[MENU_ACT_ITEM] == 'EXIT':
			MENU_MESSAGE = "Exit to OS"
	
	if LOCATION == 'game':
		if EVENT == 'ESC':
			LOCATION = 'menu'
			MENU_MESSAGE = "Game paused!"
		elif EVENT == 'TYPE':
			if GAME_STATE == 'choose':
				PLAYER+=pygame.key.name(KEY)
		elif EVENT == 'BACKSPACE':
			if GAME_STATE == 'choose':
				PLAYER = PLAYER[:-1]

		if GAME_STATE == 'choose':
			MENU_ITEMS = MENU_ITEMS_IN_GAME

def draw():
	if LOCATION == 'menu':
		menu(MENU_ITEMS,MENU_ACT_ITEM,MENU_MESSAGE)
	elif LOCATION == 'game':
		game()
	DISPLAY.flip()
	DISPLAY.update()
	FPSCLOCK.tick(FPS)
	
def game_exit():
	print("Game exit")
	pygame.quit()
	sys.exit()
   
def menu(items,act_item,message):
	global MENU_ITEMS_RECT
	MENU_ITEMS_RECT=[]
	FPS = 10
	GAME_SCREEN.fill(WHITE)
	for i in items:
		if i == act_item:
			color = RED
		else:
			color = BLACK
		menuItemSrf = FONT.render(items[i], True, color)
		menuItemRect = menuItemSrf.get_rect()
		menuItemRect.topleft = (WINDOW_WIDTH/2 - menuItemRect.centerx,WINDOW_HEIGHT/2 - (menuItemRect.height+10)*(len(items)- i))
		MENU_ITEMS_RECT.append(menuItemRect)
		GAME_SCREEN.blit(menuItemSrf,menuItemRect)
	game_message(message)
def game():
	global GAME_STATE,textinput
#	FPS = 60
	
	if GAME_STATE == 'firstrun':
		GAME_SCREEN.fill(WHITE)
		GAME_STATE = 'choose'
	if GAME_STATE == 'choose':
	   GAME_SCREEN.fill(WHITE)
	   game_message('Call your name!')
	   playerNameSrf = FONT.render(PLAYER,True,RED)
	   playerNameRect = playerNameSrf.get_rect()
	   playerNameRect.topleft = (WINDOW_WIDTH/2 - playerNameRect.centerx,WINDOW_HEIGHT/2-playerNameRect.centery)
	   GAME_SCREEN.blit(playerNameSrf,playerNameRect)
		
		
		

def game_message(text):
	messageSrf = FONT.render(text,True,BLACK)
	messageRect = messageSrf.get_rect()
	messageRect.topleft = (10, WINDOW_HEIGHT - 30)
	GAME_SCREEN.blit(messageSrf, messageRect)

if __name__ == "__main__":
	main()


