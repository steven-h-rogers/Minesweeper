import pygame
import Tile
import random
import numpy as np

"""win condition is once all bombs are flagged and all non bombs are revealed
rows = y axis
cols = x axis
bombs on bomb_map are represented with !
everything else on bomb_map is amount of adjacent bombs at that point
"""


class Game:

    # Directions dict to check adjacent cells
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
    ATLAS_COORDS = {} # Stores the symbol and coords data necessary for a blit into memory

    TILE_SIZE = 32 # Each tile in the sheet is 32x32
    TILES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '!', 'X', '*', ' ', '<', '?'] # All possible tiles
    ALWAYS_NECESSARY_TILES = ['!', ' ', '<', '?', 'X', '*'] # Tiles that will be needed/can be displayed if the user wishes uses them

    def __init__(self, dimensions, num_bombs):
        """TODO: In the future, this class should be split into two classes so that 
        image doesn't have to be loaded upon every new game. Have a seperate class 
        that loads all of the things that will always be needed into memory once 
        and then another one that handles all of the things that are unique to the 
        actual game instance"""
        self.ATLAS = pygame.image.load('graphics/minesweeper_spritesheet.png').convert_alpha() # Load Spritesheet on the class level

        self.dimensions = dimensions
        self.cols, self.rows = self.dimensions

        self.num_bombs = num_bombs
        self.bomb_probability = num_bombs/(self.rows*self.cols)

        self.bomb_map = self.initialize_bomb_map(self.rows, self.cols, self.bomb_probability)
        self.curr_game_tiles = self.get_unique_tiles(self.bomb_map)
        self.curr_game_tiles.update(Game.ALWAYS_NECESSARY_TILES)
        self.initialize_atlas_coords_dict()

        self.display_dict(Game.ATLAS_COORDS)
        # self.curr_game_tile_dict = self.load_game_tiles_to_memory()


    """generatre a 2d array that is only responsible for placing the bombs"""
    def initialize_bomb_map(self, rows, cols, bomb_probability):
        bomb_map = np.random.random((rows, cols)) < bomb_probability #randomly place the bombs based on probability
        return self.generate_proximity_map(bomb_map.tolist())
        
    """from the initial bomb distribution map, convert bombs to ! and all other tiles 
    to adjacent bomb map"""
    def generate_proximity_map(self, bomb_map):
        rows = len(bomb_map)
        cols = len(bomb_map[0])
        for i in range(rows):
            for j in range(cols):
                if bomb_map[i][j] == True:
                    bomb_map[i][j] = '!'
                else:
                    adjacent_bombs = 0
                    for direction in Game.CHECK_DIRECTIONS.values():
                        col_dir = direction[0]
                        row_dir = direction[1]
                        if i+row_dir < rows and i+row_dir>=0 and j+col_dir < cols and j+col_dir >=0:
                            if bomb_map[i+row_dir][j+col_dir] == '!' or bomb_map[i+row_dir][j+col_dir] == True:
                                adjacent_bombs += 1
                    bomb_map[i][j] = str(adjacent_bombs)
        return bomb_map
    

    def display_bomb_map(self, bomb_map):
        for row in bomb_map:
            print(row)

    def get_unique_tiles(self, bomb_map):
        unique_tiles = set()
        for row in bomb_map:
            unique_tiles.update(row)
        unique_tiles.discard('!')
        return unique_tiles
    

    def initialize_atlas_coords_dict(self):
        tile_index = 0
        for i in range(self.ATLAS_ROWS):
            for j in range(self.ATLAS_COLS):
                if tile_index < 15:
                    curr_symbol = self.TILES[tile_index]
                    curr_symbol_coord_data = (j*self.TILE_SIZE, i*self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
                    curr_symbol_rect = pygame.Rect(curr_symbol_coord_data)
                    self.ATLAS_COORDS[curr_symbol] = curr_symbol_rect
                    tile_index += 1


    def display_dict(self, dict_to_print):
        for k,v in dict_to_print.items():
            print(k,v,sep=': ')
    

    def load_game_tiles_to_memory(self):
        curr_game_surfaces = {}
        for symbol in self.curr_game_tiles:
           curr_game_surfaces[symbol] = self.ATLAS.subsurface(Game.ATLAS_COORDS[symbol])
        return curr_game_surfaces
            
