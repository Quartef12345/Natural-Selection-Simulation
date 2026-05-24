import random


import state

class Bush:                         #Bushes, will allow bins to eat and gain energy
    def __init__(self, position):
        self.position = position
        self.fruits = 0  #how many fruits it currently has
        self.timer = 0
        self.min_growth_time = state.MIN_GROWTH_TIME #the amount of time before a new fruit appears
        self.max_growth_time = state.MAX_GROWTH_TIME
        self.growth_time = 0
        self.max_fruits = state.MAX_FRUITS

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
    




bins_array = []

bin = {
    "name": "Binnob",
    "energy": 15,
    "speed": 15,
    "position": (0,0),
    "velocity": (0,0)
}



