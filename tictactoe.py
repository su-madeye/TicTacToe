import pygame
import time

pygame.init()

Height = 900
Width = 900

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

screen = pygame.display.set_mode((Width, Height))
screen.fill(white)

grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
player = 1

font = pygame.font.SysFont(None, 70)

game_over = False
winner = 0

def reset_grid():
	global game_over
	global winner
	global grid
	global player
	grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	game_over = False
	winner = 0
	player = 1

def draw_board(i):
	# draw rect
	pygame.draw.rect(screen,black, pygame.Rect(0.2*Width, 0.2*Height, 0.6*Width, 0.6*Height), 5)
	# draw grid lines
	pygame.draw.line(screen, black, [0.4*Width, 0.2*Height], [0.4*Width, 0.2*Height + i], 5)
	pygame.draw.line(screen, black, [0.6*Width, 0.2*Height], [0.6*Width, 0.2*Height + i], 5)
	pygame.draw.line(screen, black, [0.2*Width, 0.4*Height], [0.2*Width + i, 0.4*Height], 5)
	pygame.draw.line(screen, black, [0.2*Width, 0.6*Height], [0.2*Width + i, 0.6*Height], 5)
	# pygame.display.update()

def draw_marker(row, col, player):
	H = Height
	h = 0.6*H
	W = Width
	w = 0.6*W
	centerY, centerX = int(0.15*W + row*(0.2*W) + w/4), int(0.15*H + col*(0.2*H) + h/4)
	if player == 1:
		pygame.draw.line(screen, red, [centerX-0.05*W, centerY-0.05*H], [centerX+0.05*W, centerY+0.05*H], 3)
		pygame.draw.line(screen, red, [centerX+0.05*W, centerY-0.05*H], [centerX-0.05*W, centerY+0.05*H], 3)
	else:
		pygame.draw.circle(screen, red, [centerX, centerY], int(0.05*W), 3)
	# pygame.display.update()


def in_rect(x,y):
	if x > 0.2*Width and x  < 0.8*Width and y > 0.2*Height and y < 0.8*Height:
		return True
	return False

def get_grid_pos(x,y):
	if x < 0.4*Height:
		col = 0
	elif x < 0.6*Height:
		col = 1
	else:
		col = 2
	if y < 0.4*Width:
		row = 0
	elif y < 0.6*Width:
		row = 1
	else:
		row = 2
	return row,col


def check_game_over():
	global game_over
	global winner

	pos = 0
	for x in grid:

		if sum(x) == 3:
			winner = 1
			game_over = True
		if sum(x) == -3:
			winner = 2
			game_over = True

		if grid[0][pos] + grid[1][pos] + grid[2][pos] == 3:
			winner = 1
			game_over = True
		if grid[0][pos] + grid[1][pos] + grid[2][pos] == -3:
			winner = 2
			game_over = True
		pos += 1

	if grid[0][0] + grid[1][1] + grid[2][2] == 3 or grid[0][2] + grid[1][1] + grid[2][0] == 3:
		winner = 1
		game_over = True
	if grid[0][0] + grid[1][1] + grid[2][2] == -3 or grid[0][2] + grid[1][1] + grid[2][0] == -3:
		winner = 2
		game_over = True

	# check tie
	tie = True
	for x in grid:
		for i in x:
			if i == 0:
				tie = False
	if tie:
		winner = 0
		game_over = True

def get_game_over(winner):
	pygame.display.update()
	if winner == 0:
		text = 'Game Draw!'
	else:
		text = 'Player ' + str(winner) + ' wins!!'
	print(text)
	text = font.render(text, True, black)
	screen.blit(text, (0.3*Width, 0.05*Height))
	pygame.display.flip()
	reset_grid()
	time.sleep(5)
	screen.fill(white)

def draw_markers():
	global grid
	for i in range(3):
		for j in range(3):
			if grid[i][j] != 0:
				draw_marker(i,j,grid[i][j])


run = True
i = 0
while run:
	draw_board(i)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			(x,y) = pygame.mouse.get_pos()
			if in_rect(x,y) :
				print('in rect')
				row, col = get_grid_pos(x,y)
				# print(row,col)
				if grid[row][col] == 0:
					grid[row][col] = player
					# draw_marker(row,col,player)
					player *= -1
					print(grid)
	draw_markers()
	check_game_over()
	if i < 0.6*Height:
		i += 2
	else:
		i += 0
	if game_over:
		get_game_over(winner)
		# pygame.quit()		
	pygame.display.update()
pygame.quit()
