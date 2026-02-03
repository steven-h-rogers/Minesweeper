# This class will solely be used for generating the map underneath including bombs, numbered tiles, and blank tiles
# Finally, this map will be converted to a tile map for full use in the game file

import numpy as np
import Constants
import Tile

class MapGenerator:

    def __init__(self, dimensions, num_bombs):
        self.cols, self.rows = dimensions
        self.num_bombs = num_bombs
        self.bomb_probability = self.num_bombs/(self.rows*self.cols)

        self.proximity_map = self.generate_proximity_map()
        self.display_map(self.proximity_map)

    """only method that needs to be called to generate a proximity map"""
    def generate_proximity_map(self):
        bomb_map = self.initialize_bomb_map()
        proximity_map = self.label_adjacent_bombs(bomb_map.tolist())
        return proximity_map

    """generatre a 2d array that is only responsible for placing the bombs"""
    # def initialize_bomb_map(self):
    #     bomb_map = np.random.random((self.rows, self.cols)) < self.bomb_probability #randomly place the bombs based on probability
    #     return bomb_map
    
    def initialize_bomb_map(self):
        flattened_bomb_map = np.zeros(self.rows*self.cols, dtype=bool)
        flattened_bomb_map[:self.num_bombs] = True
        np.random.shuffle(flattened_bomb_map)
        bomb_map = flattened_bomb_map.reshape(self.rows, self.cols)
        return bomb_map

        
    """in place labelling of the 2D bomb map into bombs (!) and adjacent bombs (0-8)"""
    def label_adjacent_bombs(self, bomb_map):
        for i in range(self.rows):
            for j in range(self.cols):
                if bomb_map[i][j] == True:
                    bomb_map[i][j] = '!'
                else:
                    adjacent_bombs = 0
                    for direction in Constants.CHECK_DIRECTIONS.values():
                        col_dir = direction[0]
                        row_dir = direction[1]
                        if i+row_dir < self.rows and i+row_dir>=0 and j+col_dir < self.cols and j+col_dir >=0:
                            if bomb_map[i+row_dir][j+col_dir] == '!' or bomb_map[i+row_dir][j+col_dir] == True:
                                adjacent_bombs += 1
                    bomb_map[i][j] = str(adjacent_bombs)
        return bomb_map
    

    def display_map(self, map):
        for row in map:
            print(row)
        print('\n\n')

    def get_display_map(self):
        return self.proximity_map

generator = MapGenerator((10,10), 10)
