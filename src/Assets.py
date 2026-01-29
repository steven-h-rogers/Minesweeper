import pygame
import Tile
import random
import numpy as np
from AtlasManager import atlas_manager
import Constants
from MapGenerator import MapGenerator
"""win condition is once all bombs are flagged and all non bombs are revealed
rows = y axis
cols = x axis
bombs on bomb_map are represented with !
everything else on bomb_map is amount of adjacent bombs at that point
"""

class Assets:

    def __init__(self):
        self.atlas = atlas_manager
        self.atlas.initialize()



   