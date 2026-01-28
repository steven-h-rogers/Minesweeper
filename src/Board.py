from Tile import Tile
class Board:

    def __init__(self, proximity_map):
        self.proximity_map = proximity_map
        self.rows = len(proximity_map)
        self.cols = len(proximity_map[0])
        self.board = self.convert_prox_to_board()

    def convert_prox_to_board(self):
        board = self.proximity_map
        for i in range(self.rows):
            for j in range(self.cols):
                   board[i][j] = Tile(self.proximity_map[i][j])
        return board

        