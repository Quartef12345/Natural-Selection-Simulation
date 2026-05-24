import pygame
import math

import creatures
import state

bushes = creatures.bush_array #the array of the bushes objects
bush_radius = state.BUSH_RADIUS
fruits_radius = state.FRUITS_RADIUS

#Render Main
def drawScreen(grid_size,surface):
    surface.fill("#1f304d")
    render_field(surface, grid_size)

    renderBins(70,140,grid_size,surface)
    for bush in bushes:
        renderBush(bush, grid_size, surface)
        renderFruits(bush, grid_size, surface)




#Render Functions
def render_field(surface, grid_size): 
    pygame.draw.rect(surface, "#0f240a", (grid_size[0], grid_size[1], grid_size[2], grid_size[3])) #Outline
    pygame.draw.rect(surface, "#3f782f", (grid_size[0]+5, grid_size[1]+5, grid_size[2]-10, grid_size[3]-10)) #Grass Field for the Bins

def renderBins(x,y,grid,surface):
    pygame.draw.circle(surface, "#0f214d", (grid[0] + x, grid[1] + y), 6)
    pygame.draw.circle(surface, "#406edb", (grid[0] + x, grid[1] + y), 5)

def renderBush(bush,grid,surface):   #Bush is an objet of the class bush(see creatures), grid is the grid info(currently only size), surface is the pygam surface
    pygame.draw.circle(surface, "#123020", (grid[0] + bush.position[0], grid[1] + bush.position[1]), bush_radius)#outline
    pygame.draw.circle(surface, "#28c76f", (grid[0] + bush.position[0], grid[1] + bush.position[1]), bush_radius*0.9)#center

def renderFruits(bush, grid, surface):
    i = 0
    while i < bush.fruits:
        fruit_x = grid[0] + bush.position[0] + bush_radius * math.sin(i * math.pi / 2)    #Dependin on i,the position chagnes 45º around the bush
        fruit_y = grid[1] + bush.position[1] + bush_radius * math.cos(i * math.pi / 2)

        pygame.draw.circle(surface, "#702d09", (fruit_x, fruit_y), fruits_radius)#outline
        pygame.draw.circle(surface, "#c95414",  (fruit_x, fruit_y), fruits_radius*0.9)#center
        i += 1