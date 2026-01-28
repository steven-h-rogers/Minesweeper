import pygame
import Tile
import random
import numpy as np
from AtlasManager import atlas_manager
import Constants
from MapGenerator import MapGenerator
from Board import Board
"""win condition is once all bombs are flagged and all non bombs are revealed
rows = y axis
cols = x axis
bombs on bomb_map are represented with !
everything else on bomb_map is amount of adjacent bombs at that point
"""

class Game:

    def __init__(self, dimensions, num_bombs, screen):
        self.dimensions = dimensions
        self.cols, self.rows = self.dimensions
        self.num_bombs = num_bombs

        self.screen = screen

        self.atlas = atlas_manager
        self.atlas.initialize()

        self.map_gen = MapGenerator(dimensions, num_bombs)
        self.board = Board(self.map_gen.get_display_map())

        self.render_board(self.board)

   
    def render_tile(self, board, col, row):
        selected_tile = board.board[col][row]
        tile_surface = self.atlas.GAME_ASSETS[selected_tile.hidden_state]
        self.screen.blit(tile_surface, (col*Constants.TILE_SIZE, row*Constants.TILE_SIZE))

    def render_board(self, board):
        for i in range(board.rows):
            for j in range(board.cols):
                self.render_tile(board, j, i)

    


            
