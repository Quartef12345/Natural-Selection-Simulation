import random
import math

import state
import bins
import bush


def inicializeBushes(nr_of_bushes):
    i = 0
    while i < nr_of_bushes:
        state.bush_array.append(bush.Bush((random.randrange(40,state.GRID_WIDTH-40), random.randrange(40,state.GRID_HEIGTH-40))))#puts the bush in a random postition betwen the edgeds of the grid
        i += 1

def bushesTick(bush_array):
    for bush in bush_array:
        if(bush.fruits < bush.max_fruits):
            bush.timer += state.dt #the time cotnrls when the next fruit grows
            if bush.timer >= bush.growth_time:
                bush.timer = 0
                bush.growth_time = random.uniform(bush.min_growth_time, bush.max_growth_time) #make a new qouta, for the timer to reach
                bush.fruits += 1



def inicializeBins(nr_of_bins):
    i = 0
    while i < nr_of_bins:   #Bins only spawn in the edge of the world
        a = random.randint(1,2)# a determines if the bin will vary in the x value, or the y value 
        #if a = 1 then the bin will vary in the x axis, but be stuck at the edges of the field

        b = random.randint(1,2)# b determins if the bin will vary in the upper/left or downer/rigth part of the edge

        if a == 1:
            x = random.randrange(state.GRID_WIDTH)
            if b == 1:                                      
                y = 0
            else:
                y = state.GRID_HEIGTH
            state.bins_array.append(bins.Bin((x,y)))
        else:
            y = random.randrange(state.GRID_HEIGTH)
            if b == 1:
                x = 0
            else:
                x = state.GRID_WIDTH
            state.bins_array.append(bins.Bin((x,y)))
        i += 1


def binTick(bins_array, bush_array):
    dead_bins_array = []
    for bin in bins_array:
        bin.age += state.dt


        bin.digest()
        bin.reproduce()
        bin.move(bush_array)


        offspring_cost = 0  #calculates energy of pregnancy
        if bin.pregnant:
            offspring_cost = state.OFFSPRING_COST * bin.fertility

        bin.energy -= ((bin.speed**2) + bin.metabolism/5 + bin.awareness/200 + offspring_cost) * state.dt        #total energy consumption

        if bin.energy <= 0 or bin.age >= 500:#makes a list of dead bins
            dead_bins_array.append(bin)
    
    for bin in dead_bins_array:
        bins_array.remove(bin)  #removes dead bins

