import pygame

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

creatures.inicializeBushes(200)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True




while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    creatures.bushes_tick(creatures.bush_array)
    render.drawScreen(state.GRID_SIZE, screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(240)  # limits FPS to 60

pygame.quit()



