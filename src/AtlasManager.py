import pygame
class AtlasManager:

    def __init__(self):
        self.GAME_ASSETS = {}
        self.ATLAS = None

        # Dimensions, order, and sizes are hardcoded into the spritesheet
        self.ATLAS_ROWS = 2
        self.ATLAS_COLS = 8
        self.TILES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '!', 'X', '*', ' ', '<', '?'] # All possible tiles
        self.TILE_SIZE = 32

    def load_tiles_to_memory(self):
        tile_index = 0
        for i in range(self.ATLAS_ROWS):
            for j in range(self.ATLAS_COLS):
                if tile_index < 15:
                    curr_symbol = self.TILES[tile_index]
                    curr_symbol_coord_data = (j*self.TILE_SIZE, i*self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
                    curr_symbol_rect = pygame.Rect(curr_symbol_coord_data)
                    self.GAME_ASSETS[curr_symbol] = self.ATLAS.subsurface(curr_symbol_rect)
                    tile_index += 1

    def load_atlas(self):
        self.ATLAS = pygame.image.load('graphics/minesweeper_spritesheet.png').convert_alpha()

    def get_Game_Assets(self):
        return self.GAME_ASSETS
    
atlas_manager = AtlasManager()
    

