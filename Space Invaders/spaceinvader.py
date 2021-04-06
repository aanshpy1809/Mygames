import pygame
import random
import math
from pygame import mixer
pygame.init()

gamedisplay=pygame.display.set_mode((800, 600))
clock=pygame.time.Clock()
pygame.display.set_caption('Space Invaders')
icon=pygame.image.load('rocket.png')
pygame.display.set_icon(icon)
playerImg=pygame.image.load('spaceship.png')

background=pygame.image.load('bg3.png')
mixer.music.load("background.wav")
mixer.music.play(-1) # -1 plays it on loop
exit=False
playerX=368
playerY=480
player_change=0
number_of_enemies=6
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
for i in range(number_of_enemies):
	enemyImg.append(pygame.image.load('alien.png'))
	enemyX.append(random.randrange(0, 735))
	enemyY.append(random.randrange(50, 150))
	enemyX_change.append(5)
	enemyY_change.append(40)
bulletImg=pygame.image.load('bullet2.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state=0
score=0
font=pygame.font.Font("freesansbold.ttf",25)
over_font=pygame.font.Font("freesansbold.ttf",64)
textX=10
textY=10

def score_value(text,x,y):
	result=font.render("Score: "+str(text), True, (0, 255, 0))
	gamedisplay.blit(result, (x,y))

def game_over_text():
	over_text=over_font.render("GAME OVER", True, (0, 255, 0))
	gamedisplay.blit(over_text, (200,250))


def player(x,y):
	gamedisplay.blit(playerImg, (x,y))


def enemy(x,y, i):
	gamedisplay.blit(enemyImg[i], (x,y))

def fire_bullet(x,y):
	global bullet_state
	bullet_state=1
	gamedisplay.blit(bulletImg, (x+16,y))

def iscollision(enemyX, enemyY, bulletX, bulletY):
	distance=math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
	if distance<27:
		return True
	else:
		return False

while not exit:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			exit=True
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				player_change=-5
			if event.key==pygame.K_RIGHT:
				player_change=5
			if event.key==pygame.K_SPACE:
				if bullet_state==0:
					bullet_sound=mixer.Sound("laser.wav")
					bullet_sound.play()
					bulletX=playerX
					fire_bullet(bulletX, bulletY)
		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
				player_change=0

	
	playerX+=player_change
	if playerX<=0:
		playerX=0
	elif playerX>=736:
		playerX=736
	gamedisplay.fill((0, 0, 0))
	gamedisplay.blit(background, (0,0))


	for i in range(number_of_enemies):

		if enemyY[i]>440:
			for j in range(number_of_enemies):
				enemyY[j]=2000
			game_over_text()
			break


		enemyX[i]+=enemyX_change[i]
		
		if enemyX[i]<=0:
			enemyX_change[i]=5
			enemyY[i]+=enemyY_change[i]

		elif enemyX[i]>=736:
			enemyX_change[i]=-5
			enemyY[i]+=enemyY_change[i]

		collision= iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
		if collision:
			explosion_sound=mixer.Sound("explosion.wav")
			explosion_sound.play()
			bulletY=480
			bullet_state=0
			score+=1
			enemyX[i]=random.randrange(0, 735)
			enemyY[i]=random.randrange(50, 150)


		enemy(enemyX[i], enemyY[i], i)
	
	
	player(playerX, playerY)
	
	if bulletY<=0:
		bullet_state=0
		bulletY=480

	if bullet_state==1:
		fire_bullet(bulletX, bulletY)
		bulletY-=bulletY_change
	score_value(score, textX, textY)
	

	pygame.display.update()
	clock.tick(60)
