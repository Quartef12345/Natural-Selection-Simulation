#Simulator Variables
dt = 1
x = 1280
y = 720



#Grid constants
GRID_X = 50
GRID_Y = 85
GRID_WIDTH = 760
GRID_HEIGTH = 610
GRID_SIZE = (GRID_X, GRID_Y, GRID_WIDTH, GRID_HEIGTH)

#Render Options
RENDER_NAMES = True
RENDER_ENERGY = False
RENDER_HORMONES = False
RENDER_AWARENESS = False
RENDER_GENES = True

#bush constants
BUSH_RADIUS = 3
FRUITS_RADIUS = 2

#Bush Variables
MIN_GROWTH_TIME = 4
MAX_GROWTH_TIME = 16
MAX_FRUITS = 4
ENERGY_PER_FRUIT = 30

#Bins Variables

BIN_NAMES = [
    "o", "i", "u", "a",
    "it", "ot", "ik", "ok", "uk",
    "up", "op", "ip", "ub", "ob",

    "li", "lo", "lu", "la",
    "mi", "mo", "mu",
    "ni", "no", "nu",
    "pi", "po", "pu",

    "bit", "bot", "bat",
    "dip", "dop", "dap",
    "tik", "tok", "tak",
    "lip", "lop", "lap",

    "boo", "bip", "bib",
    "nub", "nubby", "gub",
    "mip", "mib", "mob",
    "wob", "wib", "web",

    "let", "lit", "lot",
    "ling", "lingo",
    "nublet", "bitlet",

    "oo", "ee", "io", "uo",
    "chi", "ki", "qi",

    "snub", "snip", "snop",
    "blub", "blob", "blip",

    "to", "ta", "tu",
    "go", "ga", "gu"
];
BIN_RADIUS = 2

#Traits
STARTING_SPEED = 1
STARTING_AWARENESS = 100
STARTING_METABOLISM = 20

#Reproduction
REPRODUCTIVE_MATURITY = 60
SPEED_PENALTY_PERCENTAGE = 20
GESTATION_PERIOD = 20
REFRACTORY_PERIOD = 30
OFFSPRING_COST = 2


#Movement
MIN_BORING_TIMER = 3
MAX_BORING_TIMER = 9

#Energy and Genes
STARTING_ENERGY  = 100
MUTATION_CHANCE = 0.3
MIN_MUTATION_VARIANCE = 0.9
MAX_MUTATION_VARIANCE = 1.1

#Simulation Constants
BUSH_AMOUNT = 200
STARTING_BIN_AMOUNT = 7