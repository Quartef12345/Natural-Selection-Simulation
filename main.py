import pygame
import time
import state
import creatures
import render
import graphs

pygame.init()
screen = pygame.display.set_mode((state.x, state.y))
clock = pygame.time.Clock()
running = True

creatures.inicializeBushes(state.BUSH_AMOUNT)
creatures.inicializeBins(state.STARTING_BIN_AMOUNT)

# pygame setup


last_dt = time.time()

graph = graphs.Graph(screen, [200,200,400,220], "Tick", "Population")
graph.show()

graph2 = graphs.Graph(screen, [800,200, 400, 220], "Tick", "Max Pop")
graph2.show()

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


    #creatures.bushesTick(state.bush_array)
    #creatures.binTick(state.bins_array, state.bush_array)

    #render.drawScreen(state.GRID_SIZE, screen)
    screen.fill("#1f304d")
    graph.draw()
    graph2.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 120

pygame.quit()



