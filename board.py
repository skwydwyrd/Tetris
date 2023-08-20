
import pygame
from settings import BLOCK_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, WHITE,GREEN, SHAPES
from random import randint
from tetrimino import Tetrimino




class Board():
	def __init__(self,rows,columns):
		self.start = 0
		self.current = pygame.time.get_ticks()
		self.droptime = 500
		
		self.rows = rows
		self.columns = columns
		self.grid = []
		self.current_piece = Tetrimino()
		self.tetriminos = [self.current_piece]

		for i in range(self.rows):
			self.grid.append([0 for i in range(self.columns)])

		self.insert()
	
	
	def draw_grid(self, WIN):
		for r in range(len(self.grid)):
			for c in range(len(self.grid[r])):
				rect = pygame.Rect((c*BLOCK_SIZE), (r*BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE)
				if self.grid[r][c] == 0:
					pygame.draw.rect(WIN, WHITE, rect, 2)

	def can_rotate(self):
		if self.current_piece.r+1 + len(self.current_piece.shape_dict['rotations'][self.current_piece.shape_index]) > len(self.grid):
			return False

		return True
	

	def rotate(self):
		if self.can_rotate():
		
			self.remove()
			self.current_piece.rotate()
			self.insert()
			
	def print_grid(self):
		for i in self.grid:
			print(i)
		print()
		

	
	# self.shift_piece('down')
	# can_move = self.shift_piece('down')
	
	def shift_piece(self, direction):
		
		if direction == 'right' and self.can_move('right'):
			self.remove()
			self.current_piece.move_right()
			self.insert()
		if direction == 'down' and self.can_move('down'):
			self.remove()
			self.current_piece.move_down()
			self.insert()
		if direction == 'left' and self.can_move('left'):
			self.remove()
			self.current_piece.move_left()
			self.insert()

	
	def insert(self):
		for row in range(len(self.current_piece.shape)):
			for col in range(len(self.current_piece.shape[row])):
				self.grid[row+self.current_piece.r][col+self.current_piece.c] = self.current_piece.shape[row][col]
		
	def remove(self):
		for row in range(len(self.current_piece.shape)):
			for col in range(len(self.current_piece.shape[row])):
				self.grid[row+self.current_piece.r][col+self.current_piece.c] = 0
		

	def draw(self,WIN):
		for tetrimino in self.tetriminos:
			tetrimino.draw(WIN)

	def can_move(self, direction):
		'''
  			Rules:
	  			1. check if piece can move down by checking two things:
		 			a. is the piece at the bottom of the board?
		 			b. is the bottom of the piece hitting another piece below it
		 		2. can the piece move to the left?
				3. can the piece move to the right? 
			Returns:
   				boolean
  		'''
		if self.current_piece.shape != [[1, 1, 1, 1]]:
			biggest_row=max(sum(self.current_piece.shape[0]),sum(self.current_piece.shape[1]))
		else:
			biggest_row=4
		if direction=='left':
			if self.current_piece.c==0:
				return False
				
		if direction=='right':
			print((self.current_piece.c,self.columns+biggest_row))
			if self.current_piece.c==self.columns-biggest_row:
				return False
				
		if direction=='down':
			return not self.check_collision(0,1)
		return True


	def check_collision(self, dx, dy):
		bottom_row=len(self.current_piece.shape)-1
		bottom_col=len()
		if self.current_piece.shape[bottom_row][bottom_piece] == 1:
			next_row = self.current_piece.r + r + dy
			next_col = self.current_piece.c + c + dx
			if  next_row>=0 or next_row<=self.rows:
				# print(next_row,next_col,self.rows,0)
				try:
					if self.grid[next_row][next_col]==1:
						return True
				except IndexError:
					return True
			# check if you collide with something in the next row or either columns
	
			# if next_row < 0 or next_col < 0 or next_row >= self.rows or next_col >= self.columns or \
			#         self.grid[next_row][next_col] != 0:
			#     return True
		return False

	
	
	def update(self,WIN):

		self.current = pygame.time.get_ticks()
		if self.current-self.start >= 750:
			if self.can_move('down'):
				self.shift_piece('down')
				self.start=self.current
			else:
				print('Hiii!')
				self.current_piece=Tetrimino()
				self.tetriminos.append(self.current_piece)
				self.insert()
		
		self.draw(WIN)
		
		self.draw_grid(WIN)
			