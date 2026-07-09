import pygame
import time
import state
import creatures
import render



#Creatures
#	-Traits
#		-Speed
#			-How fast it moves
#	-Stats
#		-Energy
#			-Uses energy to walk, more speed more energy
#			-It collect fruits from the ground
#		-Reproduceness
#	-Die and be Born and Reproduce
#		- Die if energy less than x
#		- Reproduce if energy more than y for z seconds
#	-Random chance of altering sligtly a value on birth (Mutations)

#Enviroment
#	-Resources - Food

# Display
#	-Graphs
#	-Representation of Populataion

pygame.init()
screen = pygame.display.set_mode((state.x, state.y))
clock = pygame.time.Clock()
running = True

creatures.inicializeBushes(state.BUSH_AMOUNT)
creatures.inicializeBins(state.STARTING_BIN_AMOUNT)

# pygame setup


last_dt = time.time()


while running:

    state.dt = time.time() - last_dt
    last_dt = time.time()

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


    creatures.bushesTick(state.bush_array)
    creatures.binTick(state.bins_array, state.bush_array)

    render.drawScreen(state.GRID_SIZE, screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 120

pygame.quit()



