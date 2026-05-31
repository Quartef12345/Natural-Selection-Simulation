import pygame
import math

import creatures
import state

bushes = creatures.bush_array #the array of the bushes objects
bush_radius = state.BUSH_RADIUS
fruits_radius = state.FRUITS_RADIUS

bins = creatures.bins_array
bins_radius = state.BIN_RADIUS


pygame.font.init()
display_surface = pygame.display.set_mode((state.x, state.y))

# set the pygame window name
pygame.display.set_caption('Show Text')

grid_font = pygame.font.Font('freesansbold.ttf', 10)
panel_font = pygame.font.Font('freesansbold.ttf', 20)



#Render Main
def drawScreen(grid_size,surface):
    surface.fill("#1f304d")
    render_field(surface, grid_size)
    for bin in bins:
        renderBins(bin,grid_size,surface)
    for bush in bushes:
        renderBush(bush, grid_size, surface)
        renderFruits(bush, grid_size, surface)
    renderPanel(bins, bushes, grid_size, surface)
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
    pygame.draw.circle(surface, "#00662e", (grid[0] + bush.position[0], grid[1] + bush.position[1]), bush_radius*0.9)#center

def renderFruits(bush, grid, surface):
    i = 0
    while i < bush.fruits:
        fruit_x = grid[0] + bush.position[0] + bush_radius * math.sin(i * math.pi / 2)    #Depending on i,the position changes 45º around the bush
        fruit_y = grid[1] + bush.position[1] + bush_radius * math.cos(i * math.pi / 2)

        pygame.draw.circle(surface, "#702d09", (fruit_x, fruit_y), fruits_radius)#outline
        pygame.draw.circle(surface, "#c95414",  (fruit_x, fruit_y), fruits_radius*0.9)#center
        i += 1

def renderPanel(bins, bushes, grid, surface):
        
        #Population
        population_text = grid_font.render(f"Population: {len(bins)}", True, "#FFFFFF")
        population_surface = population_text.get_rect()
        population_surface.center = (grid[0] + grid[2] + 20, state.GRID_Y)
        surface.blit(population_text, population_surface)

def renderUtilities(bins, bushes, grid, surface):

        for bin in bins:
            if state.RENDER_AWARENESS:
                pygame.draw.circle(surface, "#FFFFFF", (grid[0] + bin.position[0], grid[1] + bin.position[1]), state.STARTING_AWARENESS, 1)
            if state.RENDER_ENERGY:
                energy_text = grid_font.render(f"{math.floor(bin.energy)}", True, "#1A9A1A")
                energy_surface = energy_text.get_rect()
                energy_surface.center = (bin.position[0] + grid[0], bin.position[1] + grid[1] + state.BIN_RADIUS*5)
                surface.blit(energy_text, energy_surface)
            if state.RENDER_RAW_ENERGY:
                rawn_energy_text = grid_font.render(f"{math.floor(bin.raw_energy)}", True, "#9A1A1A")
                rawn_energy_surface = rawn_energy_text.get_rect()
                rawn_energy_surface.center = (bin.position[0] + grid[0], bin.position[1] + grid[1] + state.BIN_RADIUS*10)
                surface.blit(rawn_energy_text, rawn_energy_surface)
            if state.RENDER_NAMES:
                name_text = grid_font.render(f"{bin.name}", True, "#FFFFFF")
                name_surface = name_text.get_rect()
                name_surface.center = (bin.position[0] + grid[0], bin.position[1] + grid[1] - state.BIN_RADIUS*5)
                surface.blit(name_text, name_surface)
            if state.RENDER_AGE:
                age_text = grid_font.render(f"{round(bin.age, 1)}", True, "#FFFFFF")
                age_surface = age_text.get_rect()
                if state.RENDER_NAMES:
                    age_surface.center = (bin.position[0] + grid[0] + 30, bin.position[1] + grid[1] - state.BIN_RADIUS*5)
                else:
                    age_surface.center = (bin.position[0] + grid[0], bin.position[1] + grid[1] - state.BIN_RADIUS*5)
                surface.blit(age_text, age_surface)
            if state.RENDER_HORMONES:
                pregnant_text = grid_font.render(f"{bin.pregnant}", True, "#FF00BF")
                pregnant_surface = pregnant_text.get_rect()
                pregnant_surface.center = (bin.position[0] + grid[0], bin.position[1] + grid[1] + state.BIN_RADIUS*14)
                surface.blit(pregnant_text, pregnant_surface)

                gestation_text = grid_font.render(f"{round(bin.gestation_timer, 2)}/{bin.gestation_period}", True, "#FFFFFF")
                gestation_surface = gestation_text.get_rect()
                gestation_surface.center = (bin.position[0] + grid[0] + state.BIN_RADIUS * 10, bin.position[1] + grid[1] + state.BIN_RADIUS * 3)
                surface.blit(gestation_text, gestation_surface)

                refractory_text = grid_font.render(f"{round(bin.refractory_timer, 2)}/{bin.refractory_period}", True, "#FFFFFF")
                refractory_surface = refractory_text.get_rect()
                refractory_surface.center = (bin.position[0] + grid[0] + state.BIN_RADIUS * 15, bin.position[1] + grid[1] + state.BIN_RADIUS * 8)
                surface.blit(refractory_text, refractory_surface)

                fertility_text = grid_font.render(f"{bin.fertility}", True, "#FFFFFF")
                fertility_surface = fertility_text.get_rect()
                fertility_surface.center = (bin.position[0] + grid[0] + state.BIN_RADIUS * 15, bin.position[1] + grid[1] + state.BIN_RADIUS * 14)
                surface.blit(fertility_text, fertility_surface)