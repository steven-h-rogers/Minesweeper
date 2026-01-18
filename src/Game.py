import pygame
import Tile
import random
import numpy as np
from AtlasManager import atlas_manager
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

    TILE_SIZE = 32 # Each tile in the sheet is 32x32
    TILES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '!', 'X', '*', ' ', '<', '?'] # All possible tiles

    def __init__(self, dimensions, num_bombs):
        self.dimensions = dimensions
        self.cols, self.rows = self.dimensions

        self.num_bombs = num_bombs
        self.bomb_probability = num_bombs/(self.rows*self.cols)

        self.bomb_map = self.initialize_bomb_map(self.rows, self.cols, self.bomb_probability)
        self.atlas = atlas_manager
        self.atlas.load_atlas()
        self.atlas.load_tiles_to_memory()
        print(atlas_manager.get_Game_Assets)

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
                else: #TODO: maybe make this function a bit more single responsibility compatible and have the checking of tiles live in it's own function to improve readability
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
    

    def display_dict(self, dict_to_print):
        for k,v in dict_to_print.items():
            print(k,v,sep=': ')
    


            
