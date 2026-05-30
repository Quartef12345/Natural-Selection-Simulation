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
RENDER_AWARENESS = False
RENDER_ENERGY = True
RENDER_RAW_ENERGY = True
RENDER_NAMES = True
RENDER_AGE = True

#bush constants
BUSH_RADIUS = 3
FRUITS_RADIUS = 2

MIN_GROWTH_TIME = 9
MAX_GROWTH_TIME = 27
MAX_FRUITS = 4
ENERGY_PER_FRUIT = 30

#Bins Constants

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

STARTING_SPEED = 0.2
STARTING_AWARENESS = 100
STARTING_METABOLISM = 10

MIN_BORING_TIMER = 3
MAX_BORING_TIMER = 9


STARTING_ENERGY  = 100
MUTATION_CHANCE = 0.01
MUTATION_INTENSITY = 2
REPRODUCTION_THRESHOLD = 550
REPRODUCTION_PENALTY = 300

#Simulation Constants
BUSH_AMOUNT = 500
STARTING_BIN_AMOUNT = 5