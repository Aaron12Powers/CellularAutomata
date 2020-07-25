from pygame.locals import *
import numpy as np
from random import randint
import pygame
import module



WIDTH = 45
HEIGHT = 45
MARGIN = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

columns = 8
rows = 15

cells = []

for row in range(0, rows):
    for column in range(0, columns):
        cells.append(module.Cell(row, column))

for cell in cells:
    print(cell.row, cell.column)

window_height = (((HEIGHT + MARGIN) * rows) + MARGIN) 
window_width = (((WIDTH + MARGIN) * columns) + MARGIN)

screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Cellular Automata')

count = 0
for cell in cells:
    if count % 3 == 0:
        cell.color = 0
    elif count % 3 == 1:
        cell.color = 1
    else:
        cell.color = 2

    count += 1



grid = []
for row in range(6):
    grid.append([])
    for column in range(8):
        grid[row].append(0)

pygame.init()

running = True

clock = pygame.time.Clock()

tick_count = 0

while running:
    # grid = newCube
    for event in pygame.event.get():  # User interacted with program
        if event.type == pygame.QUIT:  
            running = False  # Exit loop/ close pygame when x is clicked

    # HEIGHT = module.setHEIGHT()

    screen.fill(BLACK)


    for cell in cells:
        if cell.color == 0:
            color = WHITE
        elif cell.color == 1:
            color = BLACK
        else:
            color = GREY

        pygame.draw.rect(screen,
                    color,
                    [(MARGIN + WIDTH) * cell.column + MARGIN,
                    (MARGIN + HEIGHT) * cell.row + MARGIN,
                    WIDTH, HEIGHT])

    # for row in range(rows):
    #     for column in range(columns):
    #         color = GREY
    #         pygame.draw.rect(screen,
    #                          color,
    #                          [(MARGIN + WIDTH) * column + MARGIN,
    #                           (MARGIN + HEIGHT) * row + MARGIN,
    #                           WIDTH, HEIGHT])

    tick_count += 1
    clock.tick(60)
   
    pygame.display.flip()