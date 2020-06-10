import pygame, random
pygame.init()

#
# SNAKE in pygame
#
# Author: RatajX
# Youtube: https://www.youtube.com/channel/UC60mWeZtUi9ao-lwUDgAMbw

resolution = [800, 600]
window = pygame.display.set_mode( (resolution[0], resolution[1] ) )
snake = pygame.Rect(0, 0, 10, 10) 
apple = pygame.Rect(10 * random.randint(0 , 80), 10 * random.randint(0 , 60), 10, 10)
eat_apple = False
clock = pygame.time.Clock()
delta = 0.0 
tps = 10.0

def new_apple():
	global eat_apple
	if eat_apple:
		apple.x = 10 * random.randint(0 , 80)
		apple.y = 10 * random.randint(0 , 60)
		eat_apple = False

site = 1
def move(keys):
	pixel = 10
	global site
	if site == 1:
		if not snake.y == resolution[1]-10:
			snake.y += pixel
		else:
			snake.y = 0
	elif site == 2:
		if not snake.x == resolution[0]-10:
			snake.x += pixel
		else:
			snake.x = 0
	elif site == 3:
		if not snake.y == 0:
			snake.y -= pixel
		else:
			snake.y = resolution[1]-10
	elif site == 4:
		if not snake.x == 0:
			snake.x -= pixel
		else:
			snake.x = resolution[0]-10
	
def start():
	for x in range(10):
		print(x)
parts = 0
last_pos = []

def snakess():
	global last_pos
	if parts > 0:
		for s in range(parts):
			part = pygame.draw.rect(window, (255,0,0), pygame.Rect(last_pos[len(last_pos)-(5	+s)][0], last_pos[len(last_pos)-(1+s)][1], 10,10))

while True:
	# wydarzenie window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit(0)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
			if site == 4:
				site = 1
			else:
				site += 1
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
			if site == 1:
				site = 4
			else:
				site -= 1
	key = pygame.key.get_pressed() #
	delta += clock.tick()/1000.0
	while delta > 1/tps:
		delta -= 1/tps 
		move(key)
	last_pos.append([snake.x, snake.y])
	if snake.x == apple.x and snake.y == apple.y:
		eat_apple = True 
		new_apple()
		parts += 50 
	window.fill((0,0,0)) # czysczenie okna
	for lines in range(80):
		pygame.draw.line(window, (63,63,65), (10*lines,0), (10*lines, resolution[1]))
	for lines_y in range(60):
		pygame.draw.line(window, (63,63,65), (0,10 * lines_y), (resolution[0], 10*lines_y))
	if not eat_apple: 
		pygame.draw.rect(window, (0, 255 ,0), apple)
	snakess()
	pygame.draw.rect(window, (255, 0 ,0), snake)
	pygame.display.flip()