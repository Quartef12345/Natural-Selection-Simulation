import pygame
import time
import state
import creatures
import render
import quartef_pygame_graphs as qpg

pygame.init()
screen = pygame.display.set_mode((state.x, state.y))
clock = pygame.time.Clock()
running = True

creatures.inicializeBushes(state.BUSH_AMOUNT)
creatures.inicializeBins(state.STARTING_BIN_AMOUNT)

# pygame setup


last_dt = time.time()

data = {
    "Time": [1],
    "Population": [0],
    "Test":[0]
}

graph = qpg.Graph(screen, [50,50,600,340], "Time", ["Population", "Test"], ["#FFFFFF", "#111111", "#5555FF", "#B22E2E"])
graph.active = True

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
    data["Time"].append(data["Time"][-1] + state.dt)
    data["Population"].append(data["Population"][-1] + 1000000000000000 * state.dt)
    qpg.update_graphs(data)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 120

pygame.quit()



