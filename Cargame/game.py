import pygame
import time
import random

display_width=800
display_height=600
block_color=(29, 234, 205)
car_width=73
white=(255, 255, 255)
black=(0, 0, 0)
red=(200,0,0)
green=(0,200,0)
bright_red=(250,0,0)
bright_green=(0,250,0)
blue=(0,0,255)
pause=False
pygame.init()
gameDisplay=pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("RUN BABY RUN")
clock=pygame.time.Clock()

carImg=pygame.image.load('aanshcar.png')


def car(x,y):
	gameDisplay.blit(carImg, (x,y))

def crashed():
	mediumText=pygame.font.Font("freesansbold.ttf", 60)
	TextSurf, TextRect=text_objects("YOU CRASHED!", mediumText)
	TextRect.center=((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)


	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()

		
		
		button("PLAY AGAIN", 150, 450, 150, 70, bright_green, green, game_loop)
		button("EXIT", 550, 450, 100, 70, bright_red, red, quit_game)
		pygame.display.update()
		clock.tick(15)

def message_display(text):
	largeText=pygame.font.Font("freesansbold.ttf", 115)
	TextSurf, TextRect=text_objects(text, largeText)
	TextRect.center=((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(2)
	game_loop()

def text_objects(text, font):
	textsurface=font.render(text, True, black)
	return textsurface, textsurface.get_rect()

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def dodged_count(dodged):
	font=pygame.font.SysFont(None, 25)
	text=font.render("Dodged: "+str(dodged), True, black)
	gameDisplay.blit(text, (0,0))

def quit_game():
	pygame.quit()
	quit()

def button(msg, x, y, w, h, ic, ac,action=None):
	mouse=pygame.mouse.get_pos()
	click=pygame.mouse.get_pressed()

	if x<mouse[0]<x+w and y<mouse[1]<y+h:
		pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
		if click[0]==1 and action!=None:
			action()
		


	else:
		pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
	
	smallText=pygame.font.Font("freesansbold.ttf", 20)
	TextSurf, TextRect=text_objects(msg, smallText)
	TextRect.center=((x+(w/2)),(y+(h/2)))
	gameDisplay.blit(TextSurf, TextRect)

def unpaused():
	global pause
	pause=False


def paused():
	
	while pause:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(white)
		mediumText=pygame.font.Font("freesansbold.ttf", 60)
		TextSurf, TextRect=text_objects("PAUSED", mediumText)
		TextRect.center=((display_width/2),(display_height/2))
		gameDisplay.blit(TextSurf, TextRect)
		button("CONTINUE", 150, 450, 120, 70, bright_green, green, unpaused)
		button("EXIT", 550, 450, 100, 70, bright_red, red, quit_game)
		pygame.display.update()
		clock.tick(15)

def game_intro():
	intro=True
	while intro:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(white)
		mediumText=pygame.font.Font("freesansbold.ttf", 60)
		TextSurf, TextRect=text_objects("RUN BABY RUN", mediumText)
		TextRect.center=((display_width/2),(display_height/2))
		gameDisplay.blit(TextSurf, TextRect)
		button("GO!", 150, 450, 100, 70, bright_green, green, game_loop)
		button("EXIT", 550, 450, 100, 70, bright_red, red, quit_game)
		pygame.display.update()
		clock.tick(15)



def game_loop():
	x=display_width*0.45
	y=display_height*0.8
	gameExit=False
	x_change=0
	thing_x=random.randrange(0, display_width)
	thing_y=-600
	thing_width=100
	thing_height=100
	speed=7
	dodged=0
	global pause

	while not gameExit:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()

			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					x_change=-5
				elif event.key==pygame.K_RIGHT:
					x_change=5
				elif event.key==pygame.K_p:
					pause=True
					paused()

			if event.type==pygame.KEYUP:
				if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
					x_change=0



		x+= x_change
		if x>display_width-car_width or x<0:
			crashed()



		gameDisplay.fill(white)
		dodged_count(dodged)
		things(thing_x, thing_y, thing_width, thing_height, block_color)
		thing_y+=speed
		if thing_y>display_height:
			thing_y=0-display_height
			thing_x=random.randrange(0, display_width)
			dodged+=1
			if dodged%2==0:
				speed+=1

		if y<thing_y+thing_height:
			if x> thing_x and x<thing_x+thing_width or x+car_width>thing_x and x+car_width<thing_x+thing_width:
				crashed()

		car(x,y)
		pygame.display.update()
		clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()