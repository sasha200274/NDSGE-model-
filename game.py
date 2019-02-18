import pygame

pygame.init()
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("GAME")
true= True
false= False
x = 50
y = 425
widh = 40
heit = 60
speed = 15
ijump= False
jumpC=10


run = True
while run:
	pygame.time.delay(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys= pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and x>5:
		x=x-speed	
	if keys[pygame.K_RIGHT] and x<495-widh:
		x=x+speed
	if not(ijump):		
		'''if keys[pygame.K_UP] and y>5:
			y=y-speed	
		if keys[pygame.K_DOWN] and y<495-heit:
			y=y+speed'''	
		if keys[pygame.K_SPACE] :
			ijump =	true
	else:
		if jumpC >= -10:
			if jumpC < 0:
				y+= (jumpC ** 2)/2
			else:	 
				y -= (jumpC ** 2)/2
			jumpC -= 1
		else:
			ijump = False
			jumpC =10			
	win.fill((0,0,0))				
	pygame.draw.rect(win,(0,0,255),(x,y,widh,heit))
	pygame.display.update()
pygamequit()			
