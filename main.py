import pygame, sys
from pygame.locals import QUIT
from random import randint
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, ROWS, COLS, BLACK
from board import Board
from tetrimino import Tetrimino

pygame.init()
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()




# create a board
board = Board(ROWS, COLS)

# set this code up so that every 3-5 seconds a new block starts moving down the screen
start=0
current=pygame.time.get_ticks()
	

while True:
	pygame.display.set_caption(f'Tetris: {round(clock.get_fps(),2)}')
	
	# set black background
	WIN.fill(BLACK)
	
	# draw objects 
	board.update(WIN)
		
	# event loop
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_DOWN or event.key==pygame.K_s:
				board.shift_piece('down')
			elif event.key==pygame.K_LEFT or event.key==pygame.K_a:
				board.shift_piece('left')
			elif event.key==pygame.K_RIGHT or event.key==pygame.K_d:
				board.shift_piece('right')
			elif event.key==pygame.K_SPACE:
				board.rotate()
			elif event.key==pygame.K_p:
				board.print_grid()
				
				
	# update graphics
	pygame.display.update()
	clock.tick(60)