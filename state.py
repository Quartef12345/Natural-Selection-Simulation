#Constants
dt = 1

#Grid constants
GRID_X = 50
GRID_Y = 85
GRID_WIDTH = 760
GRID_HEIGTH = 610
GRID_SIZE = (GRID_X, GRID_Y, GRID_WIDTH, GRID_HEIGTH)


#bush constants
BUSH_RADIUS = 6
FRUITS_RADIUS = 3

MIN_GROWTH_TIME = 9
MAX_GROWTH_TIME = 24
MAX_FRUITS = 4

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
BIN_RADIUS = 6

STARTING_SPEED = 2
STARTING_AWARENESS = 60
MIN_BORING_TIMER = 1
MAX_BORING_TIMER = 3


STARTING_ENERGY  = 100
MUTATION_CHANCE = 0.01
MUTATION_INTENSITY = 2
REPRODUCTION_THRESHOLD = 500

#Simulation Constants
BUSH_AMOUNT = 20
STARTING_BIN_AMOUNT = 1000