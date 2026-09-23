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

test_group = qpg.DataGroup(["Time", []], {
    "Test 1": [],
    "Test 2": [],
}, 200, "index_jump", [])

test_graph = qpg.Graph(screen, [50,50,500,200], test_group, ["#FFFFFF", "#111111", "#5555FF", "#B22E2E", "#24D43B"])

test_graph.active = True

"""

simulation_info = qpg.DataGroup(["Time", []], {
    "Population": [],
    "Max Population": []
}, 200, "index_jump", [])

simulation_info_graph = qpg.Graph(screen, [state.GRID_X + state.GRID_WIDTH + 5, state.GRID_Y + 300, 225,120], simulation_info,["#FFFFFF", "#111111", "#5555FF", "#B22E2E", "#24D43B"])
simulation_info_graph.active = True

gene_info = qpg.DataGroup([["Time"], []], {
    "Min Boring Timer": [],
    "Max Boring Timer": [],

    "Reproductive Maturity": [],
    "Gestation Period": [],
    "Refractory Period": [],

    "Metabolism": [],
    "Speed": [],
    "Awareness": []
}, 200, "index_jump", [])

gene_info_graph = qpg.Graph(screen, [state.GRID_X + state.GRID_WIDTH + 5, state.GRID_Y + 40, 450,235], gene_info,[
    "#FFFFFF",
    "#111111", 
    "#5555FF", 
    "#B22E2E", 
    "#24D43B",
    "#FC00CE",
    "#FFB428",
    "#0DD7E6",
    "#006F00",
    "#1F030319"])

gene_info_graph.active = True

max_pop = 0
"""
test = True


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
    if test:
        time.sleep(5)
        test = False
    #creatures.bushesTick(state.bush_array)
    #creatures.binTick(state.bins_array, state.bush_array)

    render.drawScreen(state.GRID_SIZE, screen)

    if len(test_group.data["x"][1]) == 0:
        test_group.add_data("x", state.dt)
    else:
        test_group.add_data("x", test_group.original_data["x"][1][-1] + state.dt)


    if len(test_group.data["y_dic"]["Test 1"]) == 0:
        test_group.add_data("Test 1", state.dt * 20)
    else:
        test_group.add_data("Test 1", test_group.original_data["y_dic"]["Test 1"][-1] + state.dt * 20)  

    if len(test_group.data["y_dic"]["Test 2"]) == 0:
        test_group.add_data("Test 2", state.dt * 10 + 20)
    else:
        test_group.add_data("Test 2", test_group.original_data["y_dic"]["Test 2"][-1] + state.dt * 10)  

    test_group.update_data()
    test_group.update_graphs()
    test_group.draw_data_group()

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(120)  # limits FPS to 120

"""

    population = len(state.bins_array)
    if population > max_pop:
        max_pop = population


    if len(simulation_info.data["x"][1]) == 0:
        simulation_info.add_data("x", state.dt)
        gene_info.add_data("x", state.dt)
    else:
        simulation_info.add_data("x", simulation_info.original_data["x"][1][-1] + state.dt)
        gene_info.add_data("x", gene_info.original_data["x"][1][-1] + state.dt)

    simulation_info.add_data("Population", population)
    simulation_info.add_data("Max Population", max_pop)

    gene_info.add_data("Min Boring Timer", creatures.get_average_genes(state.bins_array)[0])
    gene_info.add_data("Max Boring Timer", creatures.get_average_genes(state.bins_array)[1])
    gene_info.add_data("Reproductive Maturity", creatures.get_average_genes(state.bins_array)[2])
    gene_info.add_data("Gestation Period", creatures.get_average_genes(state.bins_array)[3])
    gene_info.add_data("Refractory Period", creatures.get_average_genes(state.bins_array)[4])
    gene_info.add_data("Metabolism", creatures.get_average_genes(state.bins_array)[5])
    gene_info.add_data("Speed", creatures.get_average_genes(state.bins_array)[6])
    gene_info.add_data("Awareness", creatures.get_average_genes(state.bins_array)[7])


    simulation_info.update_data()
    simulation_info.update_graphs()
    simulation_info.draw_data_group()

    gene_info.update_data()
    gene_info.update_graphs()
    gene_info.draw_data_group()

"""

pygame.quit()



