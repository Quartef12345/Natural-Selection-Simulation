import pygame
import math

import creatures
import state

bushes = creatures.bush_array #the array of the bushes objects
bush_radius = state.BUSH_RADIUS
fruits_radius = state.FRUITS_RADIUS

bins = creatures.bins_array
bins_radius = state.BIN_RADIUS

#Render Main
def drawScreen(grid_size,surface):
    surface.fill("#1f304d")
    render_field(surface, grid_size)
    for bin in bins:
        renderBins(bin,grid_size,surface)
    for bush in bushes:
        renderBush(bush, grid_size, surface)
        renderFruits(bush, grid_size, surface)
    renderUtilities(bins, bushes, grid_size, surface)




#Render Functions

def render_field(surface, grid_size): 
    pygame.draw.rect(surface, "#0f240a", (grid_size[0], grid_size[1], grid_size[2], grid_size[3])) #Outline
    pygame.draw.rect(surface, "#3f782f", (grid_size[0]+5, grid_size[1]+5, grid_size[2]-10, grid_size[3]-10)) #Grass Field for the Bins

def renderBins(bin,grid,surface):
    pygame.draw.circle(surface, "#0f214d", (grid[0] + bin.position[0], grid[1] + bin.position[1]), bins_radius)
    pygame.draw.circle(surface, "#406edb", (grid[0] + bin.position[0], grid[1] + bin.position[1]), bins_radius*0.9)

def renderBush(bush,grid,surface):   #Bush is an objet of the class bush(see creatures), grid is the grid info(currently only size), surface is the pygam surface
    pygame.draw.circle(surface, "#123020", (grid[0] + bush.position[0], grid[1] + bush.position[1]), bush_radius)#outline
    pygame.draw.circle(surface, "#28c76f", (grid[0] + bush.position[0], grid[1] + bush.position[1]), bush_radius*0.9)#center

def renderUtilities(bins, bushes, grid, surface):
    if state.RENDER_AWARENESS:
        for bin in bins:
            pygame.draw.circle(surface, "#FFFFFF", (grid[0] + bin.position[0], grid[1] + bin.position[1]), state.STARTING_AWARENESS, 1)

def renderFruits(bush, grid, surface):
    i = 0
    while i < bush.fruits:
        fruit_x = grid[0] + bush.position[0] + bush_radius * math.sin(i * math.pi / 2)    #Depending on i,the position changes 45º around the bush
        fruit_y = grid[1] + bush.position[1] + bush_radius * math.cos(i * math.pi / 2)

        pygame.draw.circle(surface, "#702d09", (fruit_x, fruit_y), fruits_radius)#outline
        pygame.draw.circle(surface, "#c95414",  (fruit_x, fruit_y), fruits_radius*0.9)#center
        i += 1