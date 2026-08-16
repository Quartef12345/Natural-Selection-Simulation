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
    "Time": [],
    "Population": [],
    "Max Population":[]
}

graph = qpg.Graph(screen, [state.GRID_X + state.GRID_WIDTH + 5, state.GRID_Y + 40, 450,235], "Time", ["Population", "Max Population"], ["#FFFFFF", "#111111", "#5555FF", "#B22E2E"])
graph.active = True

max_pop = 0

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

    population = len(state.bins_array)
    if population > max_pop:
        max_pop = population

    if len(data["Time"]) == 0:
        data["Time"].append(state.dt)
    else:
        data["Time"].append(data["Time"][-1] + state.dt)
    data["Population"].append(population)
    data["Max Population"].append(max_pop)


    qpg.update_graphs(data)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 120

pygame.quit()



