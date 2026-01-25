"""This is a class that will store global constants"""

CHECK_DIRECTIONS = {
    'left': (-1, 0),
    'up_left': (-1, -1),
    'up': (0, -1),
    'up_right': (1, -1),
    'right': (1,0),
    'down_right': (1, 1),
    'down': (0, 1),
    'down_left': (-1, 1)
}

# Dimensions are baked into the spritesheet
ATLAS_ROWS = 2
ATLAS_COLS = 8
NUM_SPRITES = 15 # One empty space in the sheet

TILE_SIZE = 32 # Each tile in the sheet is 32x32
TILES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '!', 'X', '*', ' ', '<', '?'] # All possible tiles