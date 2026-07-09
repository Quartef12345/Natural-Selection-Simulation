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
        self.growth_time = random.uniform(self.min_growth_time, self.max_growth_time)