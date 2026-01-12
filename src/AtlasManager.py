import pygame
class AtlasManager:
    GAME_ASSETS = None

    ATLAS = pygame.image.load('graphics/minesweeper_spritesheet.png').convert_alpha()

    # Dimensions are hardcoded into the spritesheet
    ATLAS_ROWS = 2
    ATLAS_COLS = 8
    ATLAS_COORDS = {} # Stores the symbol and coords data necessary for a blit into memory
    TILES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '!', 'X', '*', ' ', '<', '?'] # All possible tiles



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
