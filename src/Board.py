from Tile import Tile
import Constants
from Assets import Assets
from collections import deque
import re
class Board:

    def __init__(self, proximity_map, num_bombs, screen):
        self.screen = screen
        self.num_bombs = num_bombs
        self.proximity_map = proximity_map
        self.rows = len(proximity_map)
        self.cols = len(proximity_map[0])
        self.board = self.convert_prox_to_board() # This stores the list as a 2d array of tiles

        self.assets = Assets()
        self.atlas = self.assets.atlas
        self.atlas.initialize()

        

    def convert_prox_to_board(self):
        board = self.proximity_map
        for i in range(self.rows):
            for j in range(self.cols):
                board[i][j] = Tile(self.proximity_map[i][j], i, j)
        return board
    
    def render_tile(self, col, row):
        selected_tile = self.board[col][row]
        tile_surface = self.atlas.GAME_ASSETS[selected_tile.displayed_state]
        self.screen.blit(tile_surface, (col*Constants.TILE_SIZE, row*Constants.TILE_SIZE))

    def render_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.render_tile(col, row)

    
    def reveal_single_tile(self, row, col):
        self.board[row][col].reveal()

    def handle_l_click(self, row, col):
        root = self.board[row][col]
        if root.revealed_state != '!':
            if re.search(r"[1-8]", root.revealed_state) and root.isHidden:
                self.reveal_single_tile(row, col)
            if re.search(r"[1-8]", root.revealed_state) and root.isHidden is False:
                if self.reveal_if_bombs_marked(root.row, root.col) == 'INCORRECTLY MARKED':
                    self.reveal_entire_board()
                    return 'GAME OVER'
            elif root.revealed_state == '0':
                print("clicked empty tile")
                self.reveal_empty_adjacents(root)
        else:
            root.explode()
            self.reveal_entire_board()
            return 'GAME OVER'
    
    def handle_r_click(self, row, col):
        root = self.board[row][col]
        if root.isHidden == True:
            root.cycle_hidden_state()

    def reveal_entire_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                curr_tile = self.board[row][col]
                if curr_tile.revealed_state != '!' and curr_tile.displayed_state == '<':
                    curr_tile.incorrectly_marked()
                curr_tile.reveal()

    # modified flood fill
    def reveal_empty_adjacents(self, root):
        queue = deque([root])
        visited = set()

        while queue:
            curr_tile = queue.pop()
            row, col = curr_tile.row, curr_tile.col
            self.reveal_single_tile(row, col)

            if re.search(r"[1-8]", curr_tile.revealed_state) == None:
                for direction in Constants.CHECK_DIRECTIONS.values():
                    col_dir = direction[0]
                    row_dir = direction[1]
                    if row+row_dir < self.rows and row+row_dir>=0 and col+col_dir < self.cols and col+col_dir >=0:
                        adjacent_tile = self.board[row+row_dir][col+col_dir]
                        if adjacent_tile not in visited and adjacent_tile not in queue and adjacent_tile.isHidden and adjacent_tile.revealed_state != '!':
                            queue.append(adjacent_tile)
                    visited.add(curr_tile)
    
    

    def reveal_if_bombs_marked(self, row, col):
        root = self.board[row][col]
        flagged_adjacent_bombs = 0
        adjacent_safe_tiles = [] #keep adjacent safe tiles on hand in case all bombs are flagged so they can be revealed
        row, col = root.row, root.col
        
        for direction in Constants.CHECK_DIRECTIONS.values():
            col_dir = direction[0]
            row_dir = direction[1]
            if row+row_dir < self.rows and row+row_dir>=0 and col+col_dir < self.cols and col+col_dir >=0:
                adjacent_tile = self.board[row+row_dir][col+col_dir]
                if adjacent_tile.revealed_state == '!' and adjacent_tile.displayed_state == '<':
                    flagged_adjacent_bombs += 1
                elif adjacent_tile.revealed_state != '!' and adjacent_tile.displayed_state == '<':
                    adjacent_tile.incorrectly_marked()
                    return 'INCORRECTLY MARKED'
                else:
                    adjacent_safe_tiles.append(adjacent_tile)
            if re.search(r'[1-8]', root.displayed_state) != None and int(root.displayed_state) == flagged_adjacent_bombs:
                for tile in adjacent_safe_tiles:
                    if tile.revealed_state == '0':
                        self.reveal_empty_adjacents(tile)
                    else:
                        self.reveal_single_tile(tile.row, tile.col)




    # TODO: future optimization is to count these figures live as instance variables that are tracked within handle_l_click and handle_r_click so that an O(m*n) function doesn't have to be called after every update
    def check_for_win(self):
        print('checking for win')
        num_safe_tiles = ((self.rows)*(self.cols))-self.num_bombs

        num_revealed_safe_tiles = 0
        num_flagged_bomb_tiles = 0

        for row in range(self.rows):
            for col in range(self.cols):
                curr_tile = self.board[row][col]
                if curr_tile.revealed_state == '!' and curr_tile.displayed_state == "<":
                        num_flagged_bomb_tiles += 1
                else:
                    if curr_tile.isHidden == False:
                        num_revealed_safe_tiles += 1
        if num_revealed_safe_tiles == num_safe_tiles and num_flagged_bomb_tiles == self.num_bombs:
            return "YOU WON"
                

        