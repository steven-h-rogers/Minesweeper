import pygame
class AtlasManager:

    def __init__(self):
        self.GAME_ASSETS = {}
        self.ATLAS = None
        self.initialized = False

        self.loaded_atlas = False
        self.loaded_tiles = False

        # Dimensions, order, and sizes are hardcoded into the spritesheet
        self.ATLAS_ROWS = 2
        self.ATLAS_COLS = 8
        self.TILES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '!', 'X', '*', ' ', '<', '?'] # All possible tiles
        self.TILE_SIZE = 32

    # only call this after pygame has been initialized 
    def initialize(self):
        if self.initialized == False:
            self.load_atlas()
            self.load_tiles_to_memory()
            self.initialized = True
        else: print("Atlas Manager already initialized")


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
        if self.loaded_atlas == False:
            self.loaded_atlas = True
            self.ATLAS = pygame.image.load('graphics/minesweeper_spritesheet.png').convert_alpha()

    def get_Game_Assets(self):
        if self.loaded_tiles == False:
            self.loaded_tiles = True
            return self.GAME_ASSETS
    
atlas_manager = AtlasManager()
    

