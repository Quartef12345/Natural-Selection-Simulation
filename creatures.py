import random
import math

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

def bushesTick(bush_array):
    for bush in bush_array:
        if(bush.fruits < bush.max_fruits):
            bush.timer += state.dt #the time cotnrls when the next fruit grows
            if bush.timer >= bush.growth_time:
                bush.timer = 0
                bush.growth_time = random.randint(bush.min_growth_time, bush.max_growth_time) #make a new qouta, for the timer to reach
                bush.fruits += 1
    

def generateName():
    name = "Bin" + random.choice(state.BIN_NAMES)
    return name

class Bin:
    def __init__(self, position):
        #Identity Variables
        self.name = generateName()
        self.age = 0

        #Movement Variables
        self.position = position
        self.direction = (0,0)
        self.min_boring_timer = state.MIN_BORING_TIMER
        self.max_boring_timer = state.MAX_BORING_TIMER
        self.boring_timer = random.uniform(self.min_boring_timer, self.max_boring_timer)

        #Reproduction Variables
        self.pregnant = False
        self.reproductive_maturity = state.REPRODUCTIVE_MATURITY    #How old you must be to reproduce
        self.gestation_period = state.GESTATION_PERIOD  #How long will the pregnancy take
        self.refractory_period = state.REFRACTORY_PERIOD #How long until you can reproduce again
        self.fertility = round((self.gestation_period + 0.0008 * (self.gestation_period - 120)**3)/500 + 2.76) #how many childer will you have, based on the gestation
        self.speed_penalty_percentage = state.SPEED_PENALTY_PERCENTAGE
        self.gestation_timer = 0
        self.refractory_timer = state.REFRACTORY_PERIOD


        #Energy Varaibles
        self.energy = state.STARTING_ENERGY
        self.raw_energy = 0
        self.metabolism = state.STARTING_METABOLISM

        #General Traits
        self.speed = state.STARTING_SPEED
        self.awareness = state.STARTING_AWARENESS

    def reproduce(self):

        energy_for_pregnancy = self.gestation_period * 0.0006 + 100 #How much energy you use per child, based on gestaton period
        if self.age >= self.reproductive_maturity and self.refractory_timer >= self.refractory_period and self.energy >= energy_for_pregnancy and self.pregnant == False:   #Every conditiion - Age; Refractory; Energy; not already pregnant
                self.pregnant = True
                self.speed *= (100 - self.speed_penalty_percentage)/100 #Changes speed to slower, due to pregnancy
                self.gestation_timer = 0

        if self.pregnant:
            self.gestation_timer += state.dt
            if self.gestation_timer >= self.gestation_period: #When the bin should be born
                offspring_array = []

                for i in range (self.fertility):        #Changes Bins stats(in future will have mutations and etc)
                    offspring_array.append(Bin(self.position))
                    offspring_array[i].energy = energy_for_pregnancy/self.fertility

                self.pregnant = False
                self.refractory_timer = 0
                self.speed /= (100 - self.speed_penalty_percentage)/100 #Reputs the speed to normal

                for bin in offspring_array: #Adds offsprings to the world
                    bins_array.append(bin)

                self.energy -= energy_for_pregnancy
        else:
            self.refractory_timer += state.dt
                

    def digest(self):       #Funstion to detemrine the difesting energy of createures, the higher the metabolism he fatse rcretuers get usable energy, but the less efficient it is
        if self.raw_energy > 0:
            tranforming_energy = self.metabolism * state.dt
            if tranforming_energy > self.raw_energy:   #Makes it so that raw energy can never go below zero
                tranforming_energy = self.raw_energy

            self.energy += tranforming_energy * 1/(self.metabolism*0.03 + 1) #The bigger the metabolism, the less efficiently is the digestion
            self.raw_energy -= tranforming_energy

    def move(self, bushes):
        #(x-h)^2+(y-k)^2 < r^2
        last_direction_magnitude = self.awareness
        closest_bush_vector = None
        fruited_bush = None

        stomach_capacity = self.metabolism * 3
        if(self.raw_energy <= stomach_capacity):
            for bush in bushes:     #It checks every bush to find the closest withing range
                if(bush.fruits > 0):
                    if (bush.position[0] - self.position[0])**2 + (bush.position[1] - self.position[1])**2 < self.awareness**2: #Checks, using the circle equation if the bush is within awareness
                        direction_vector = (bush.position[0] - self.position[0], bush.position[1] - self.position[1]) #vector pointing at bush
                        direction_magnitude = math.sqrt(direction_vector[0]**2 + direction_vector[1]**2)
                        if abs(last_direction_magnitude) > abs(direction_magnitude):      #checks if its the current closest bush
                            closest_bush_vector = direction_vector              #if it is, then it gives the crown to that bush
                            last_direction_magnitude = direction_magnitude
                            fruited_bush = bush
        
        
        if(closest_bush_vector == None): #if it didnt find bushes, give a random direction(subject to change)
            closest_bush_vector = self.randomDirection()

        
        closest_bush_vector_magnitude = math.sqrt(closest_bush_vector[0]**2 + closest_bush_vector[1]**2)
        if closest_bush_vector_magnitude == 0:      #Prevent Division by zero error
            closest_bush_vector_magnitude += 0.01
        closest_bush_vector = (closest_bush_vector[0]/closest_bush_vector_magnitude, closest_bush_vector[1]/closest_bush_vector_magnitude)      #normalzied direction

        self.direction = closest_bush_vector
        self.position = (self.direction[0] * self.speed + self.position[0], self.direction[1] * self.speed + self.position[1])
        
        self.checkBorders()

        if fruited_bush != None:        #Checks if bin is in "range" to eat fruit
            if ((fruited_bush.position[0]  > self.position[0] - 3) and (fruited_bush.position[0]  < self.position[0] + 3)) and ((fruited_bush.position[1]  > self.position[1] - 3) and (fruited_bush.position[1]  < self.position[1] + 3)):
                fruited_bush.fruits -= 1
                self.raw_energy += state.ENERGY_PER_FRUIT

    def randomDirection(self):                  #If boring timer is 0, then the bin changes it direction for a random peridof of time, unitl it gets bored again
        if (self.position[0] < 10
        or self.position[0] > state.GRID_WIDTH - 10
        or self.position[1] < 10
        or self.position[1] > state.GRID_HEIGTH - 10):
            self.boring_timer = 0

        if self.boring_timer <= 0:
            if self.position[0] < state.GRID_X + 30:        #Logic to make bins nto get stuck on edges
                x = abs(random.randrange(-100,100))
            elif self.position[0] > state.GRID_WIDTH - 30:
                x = -abs(random.randrange(-100,100))
            else:
                x = random.randrange(-100,100)

            if self.position[1] < state.GRID_Y + 30:
                y = abs(random.randrange(-100,100))
            elif self.position[1] > state.GRID_HEIGTH - 30:
                y = -abs(random.randrange(-100,100))
            else:
                y = random.randrange(-100,100)
            
            random_direction = ( x + self.direction[0], y + self.direction[1])
            self.boring_timer = random.uniform(self.min_boring_timer, self.max_boring_timer)
        else:
            self.boring_timer -= state.dt           #while traveling one way, the direction gets small fluctuations because it looks better
            random_direction = (self.direction[0] + random.uniform(-0.1, 0.1), self.direction[1] + random.uniform(-0.1, 0.1))


        return random_direction

    def checkBorders(self):                                         #Makes bin stay in the border, and not pass trougth it
        if self.position[0] <= 0:
            self.position = (0, self.position[1])
        elif self.position[0] >= state.GRID_WIDTH:
            self.position = (state.GRID_WIDTH, self.position[1])
        if self.position[1] <= 0:
            self.position = (self.position[0], 0)
        elif self.position[1] >= state.GRID_HEIGTH:
            self.position = (self.position[0], state.GRID_HEIGTH)




bins_array = []

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
            bins_array.append(Bin((x,y)))
        else:
            y = random.randrange(state.GRID_HEIGTH)
            if b == 1:
                x = 0
            else:
                x = state.GRID_WIDTH
            bins_array.append(Bin((x,y)))
        i += 1


def binTick(bins_array, bush_array):
    dead_bins_array = []
    for bin in bins_array:
        bin.age += state.dt
        bin.digest()


        bin.reproduce()


        bin.move(bush_array)

        offspring_cost = 0
        if bin.pregnant:
            offspring_cost = state.OFFSPRING_COST * bin.fertility

        bin.energy -= ((bin.speed**2) + bin.metabolism/5 + bin.awareness/200 + offspring_cost) * state.dt        

        if bin.energy <= 0 or bin.age >= 500:
            dead_bins_array.append(bin)
    for bin in dead_bins_array:
        bins_array.remove(bin)

