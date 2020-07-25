from pygame.locals import *
import numpy as np
from random import randint
import pygame
import module


rule = 70

#Define Cell Sizes
WIDTH = 15
HEIGHT = 15
MARGIN = WIDTH // 5

#Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

#Define Number of Columns
columns = 35
rows = 100


cells = [[module.Cell for i in range(rows)] for j in range(columns)]


for row in range(0, rows):
    for column in range(0, columns):
        cells[column][row]  = (module.Cell(row, column))

for row in range(0, rows):
    for column in range(0, columns):
        print(cells[column][row].row,cells[column][row].column)

window_height = (((HEIGHT + MARGIN) * rows) + MARGIN) 
window_width = (((WIDTH + MARGIN) * columns) + MARGIN)

screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Cellular Automata')


module.StartSim(cells, rows, columns)
module.RunSim(cells, rows, columns, rule)

grid = []
for row in range(6):
    grid.append([])
    for column in range(8):
        grid[row].append(0)

pygame.init()

running = True

clock = pygame.time.Clock()

tick_count = 0

row_step = 0

#Main pygame loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False  # Exit loop/ close pygame when x is clicked

    screen.fill(GREY)

    #update next row every 20 ticks
    if tick_count % 20 == 0:
        row_step += 1

    for row in range(0, rows):
        for column in range(0, columns):
            if row <= row_step:
                if cells[column][row].color == 0:
                    color = WHITE
                elif cells[column][row].color == 1:
                    color = BLACK
                else:
                    color = GREY
                pygame.draw.rect(screen,
                    color,
                    [(MARGIN + WIDTH) * cells[column][row].column + MARGIN,
                    (MARGIN + HEIGHT) * cells[column][row].row + MARGIN,
                    WIDTH, HEIGHT])
            else:
                color = GREY
                pygame.draw.rect(screen,
                    color,
                    [(MARGIN + WIDTH) * cells[column][row].column + MARGIN,
                    (MARGIN + HEIGHT) * cells[column][row].row + MARGIN,
                    WIDTH, HEIGHT])


    if row_step == rows:
        row_step -= 1

    tick_count += 1
    clock.tick(60)
   
    pygame.display.flip()