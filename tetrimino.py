import pygame
from settings import SHAPES,BLOCK_SIZE
from random import choice

class Tetrimino():
	def __init__(self):
		# self.shape_key = choice(list(SHAPES)
		self.shape_dict=SHAPES[0]
		self.shape_index = self.shape_dict['index']
		self.shape = self.shape_dict['rotations'][0]
		self.num_of_rotations=len(self.shape_dict['rotations'])
		self.color = self.shape_dict['color']
		
		self.r = 0
		self.c = 10
		
	def move_down(self):
		self.r+=1
		
	def move_left(self):
		self.c-=1

	def move_right(self):
		self.c+=1

	def draw(self,WIN):
		# pygame.draw.rect(WIN,self.color,self.rect)
		for r in range(len(self.shape)):
			for c in range(len(self.shape[r])):
				if self.shape[r][c]==1:
					x=self.c*BLOCK_SIZE+c*BLOCK_SIZE
					y=self.r*BLOCK_SIZE+r*BLOCK_SIZE
					pygame.draw.rect(WIN,self.color,(x,y,BLOCK_SIZE,BLOCK_SIZE))

	def rotate(self):
		if self.shape_index>self.num_of_rotations-1:
			self.shape_index=0
		else:
			self.shape_index += 1
		self.shape = self.shape_dict['rotations'][self.shape_index]
				