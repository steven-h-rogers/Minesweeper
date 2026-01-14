import pygame
class AtlasManager:
    GAME_ASSETS = None
    #This line will cause an issue as pygame has not yet been initialized. Need to use a constructor instead
    ATLAS = pygame.image.load('graphics/minesweeper_spritesheet.png').convert_alpha()

    # Dimensions, order, and sizes are hardcoded into the spritesheet
    ATLAS_ROWS = 2
    ATLAS_COLS = 8
    TILES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '!', 'X', '*', ' ', '<', '?'] # All possible tiles
    TILE_SIZE = 32



    def load_tiles_to_memory():
        tile_index = 0
        for i in range(AtlasManager.ATLAS_ROWS):
            for j in range(AtlasManager.ATLAS_COLS):
                if tile_index < 15:
                    curr_symbol = AtlasManager.TILES[tile_index]
                    curr_symbol_coord_data = (j*AtlasManager.TILE_SIZE, i*AtlasManager.TILE_SIZE, AtlasManager.TILE_SIZE, AtlasManager.TILE_SIZE)
                    curr_symbol_rect = pygame.Rect(curr_symbol_coord_data)
                    AtlasManager.GAME_ASSETS[curr_symbol] = pygame.Surface.subsurface(curr_symbol_rect)
                    tile_index += 1

    def get_Game_Assets():
        return AtlasManager.GAME_ASSETS

    load_tiles_to_memory()
