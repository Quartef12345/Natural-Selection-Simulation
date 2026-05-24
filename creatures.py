import random


import state

class Bush:                         #Bushes, will allow bins to eat and gain energy
    def __init__(self, position):
        self.position = position
        self.max_fruits = state.MAX_FRUITS
        self.fruits = 0  #how many fruits it currently has
        self.timer = 0
        self.min_growth_time = state.MIN_GROWTH_TIME #the amount of time before a new fruit appears
        self.max_growth_time = state.MAX_GROWTH_TIME
        self.growth_time = random.randint(self.min_growth_time, self.max_growth_time)

bush_array = []

def inicializeBushes(nr_of_bushes):
    i = 0
    while i < nr_of_bushes:
        bush_array.append(Bush((random.randrange(40,state.GRID_WIDTH-40), random.randrange(40,state.GRID_HEIGTH-40))))#puts the bush in a random postition betwen the edgeds of the grid
        i += 1

def bushes_tick(bush_array):
    for bush in bush_array:
        if(bush.fruits < bush.max_fruits):
            bush.timer += 1 #the time cotnrls when the next fruit grows
            if bush.timer >= bush.growth_time:
                bush.timer = 0
                bush.growth_time = random.randint(bush.min_growth_time, bush.max_growth_time) #make a new qouta, for the timer to reach
                bush.fruits += 1
    

def generateName():
    name = "bin" + random.choice(state.BIN_NAMES)
    return name

class Bin:
    def __init__(self, position):
        self.position = position
        self.direction = (0,0)
        self.energy = state.STARTING_ENERGY
        self.speed = state.STARTING_SPEED
        self.mutation_chance = state.MUTATION_CHANCE
        self.name = generateName()


bins_array = []

def inicializeBins(nr_of_bins):
    i = 0
    while i < nr_of_bins:
        a = random.randint(1,2)# a determines if the bin will vary in the x value, or the y value 
        #if a = 1 then the bin will vary in the x axis, but be stuck at the edges of the field

        b = random.randint(1,2)# b determins if the bin will vary in the upper/left or downer/rigth part of the edge

        if a == 1:
            x = random.randrange(state.GRID_WIDTH)
            if b == 1:                                      
                y = 0
            else:
                y = state.GRID_HEIGTH
            bins_array.append(Bin((x,y)))
        else:
            y = random.randrange(state.GRID_HEIGTH)
            if b == 1:
                x = 0
            else:
                x = state.GRID_WIDTH
            bins_array.append(Bin((x,y)))
        i += 1



