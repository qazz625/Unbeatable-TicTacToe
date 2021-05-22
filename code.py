import pygame
import time
import random
import logic

#turn=0 for player
#turn=1 for computer
turn = 0
end = 0
turn_number = 0


def text_objects(text, font):
	textSurface = font.render(text, True, 'black')
	return textSurface, textSurface.get_rect()

def introButton(msg, x, y, w, h, active, inactive):
	global turn
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x <= mouse[0] <= x+w and y <= mouse[1] <= y+h:
		pygame.draw.rect(screen, active, (x, y, w, h))
		if click[0] == 1:
			if msg == "Go First":
				turn = 0
			else:
				turn = 1
			time.sleep(0.2)
			game_loop()
	else:
		pygame.draw.rect(screen, inactive, (x, y, w, h))

	fontSize = pygame.font.Font("freesansbold.ttf", 20)
	textSurf, textRect = text_objects(msg, fontSize)
	textRect.center = ( x+w//2, y+h//2 )
	screen.blit(textSurf, textRect)

def gameButton(x, y, w, h, active, inactive, curstate, row, col):
	global turn_number, turn
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x <= mouse[0] <= x+w and y <= mouse[1] <= y+h:
		pygame.draw.rect(screen, active, (x, y, w, h))
		if click[0] == 1 and turn == 0 and curstate[row][col] == '':
			curstate[row][col] = 'O'
			turn_number += 1
			turn ^= 1
	else:
		pygame.draw.rect(screen, inactive, (x, y, w, h))

	msg = curstate[row][col]
	fontSize = pygame.font.Font("freesansbold.ttf", 60)
	textSurf, textRect = text_objects(msg, fontSize)
	textRect.center = ( x+w//2, y+h//2 )
	screen.blit(textSurf, textRect)

def endgameButton(msg, x, y, w, h, active, inactive):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x <= mouse[0] <= x+w and y <= mouse[1] <= y+h:
		pygame.draw.rect(screen, active, (x, y, w, h))
		if click[0] == 1:
			time.sleep(0.2)
			return False
	else:
		pygame.draw.rect(screen, inactive, (x, y, w, h))

	fontSize = pygame.font.Font("freesansbold.ttf", 20)
	textSurf, textRect = text_objects(msg, fontSize)
	textRect.center = ( x+w//2, y+h//2 )
	screen.blit(textSurf, textRect)
	return True

def computer_plays(curstate):
	global turn, turn_number
	if turn_number <= 0:
		arr = []
		turn_number += 1
		for i in range(3):
			for j in range(3):
				if curstate[i][j] == '':
					arr += [(i, j)]
		tup = random.choice(arr)
		curstate[tup[0]][tup[1]] = 'X'

	else:
		row, col = logic.solve(curstate)
		curstate[row][col] = 'X'
		time.sleep(0.2)

	turn ^= 1

def game_intro():
	global end, turn_number
	intro = True
	while intro:
		end = 0
		turn_number = 0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro = False
		screen.fill((233, 237, 161))
		mouse = pygame.mouse.get_pos()
		introButton("Go First", 150, 450, 200, 70, 'green', 'white')
		introButton("Go Second", 450, 450, 200, 70, 'green', 'white')
		pygame.display.update()

def game_loop():
	global end, turn, turn_number
	running = True
	curstate = [['', '', ''], ['', '', ''], ['', '', '']]
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		if turn == 0 and end == 0:
			screen.fill((233, 237, 161))
			cell_width = 120
			cell_height = 120
			for i in range(3):
				for j in range(3):
					curx = 220+cell_height*i
					cury = 100+cell_width*j
					gameButton(curx+2, cury+2, cell_height-4, cell_width-4, 'green', 'white', curstate, j, i)
		elif turn == 1 and end == 0:
			computer_plays(curstate)
		else:
			running = False
		end = logic.check_win(curstate)
		pygame.display.update()
	game_end(curstate, end)

def game_end(curstate, msg):
	endscreen = True
	fontSize = pygame.font.Font("freesansbold.ttf", 40)
	textSurf, textRect = text_objects(msg, fontSize)
	textRect.center = ( 400, 50 )
	screen.blit(textSurf, textRect)
	cell_height = 120
	cell_width = 120
	while endscreen:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				endscreen = False
		endscreen = endscreen and endgameButton("Try Again", 300, 500, 200, 70, 'green', 'white')
		for i in range(3):
			for j in range(3):
				curx = 220+cell_height*i + 2
				cury = 100+cell_width*j + 2
				w = cell_width - 4
				h = cell_height - 4
				pygame.draw.rect(screen, 'white', (curx+2, cury+2, w-4, h-4))
				msg = curstate[j][i]
				fontSize = pygame.font.Font("freesansbold.ttf", 60)
				textSurf, textRect = text_objects(msg, fontSize)
				textRect.center = ( curx+w//2, cury+h//2 )
				screen.blit(textSurf, textRect)

		pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Unwinnable TicTacToe")
game_intro()






