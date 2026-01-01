import Game

class Tile:
    
    def __init__(self, displayed_state, hidden_state = ' ', isHidden = True):

        self.ALWAYS_NECESSARY_TILES = Game.ALWAYS_NECESSARY_TILES
        self.displayed_state = displayed_state
        self.displayed_state_img = None # need better software design/object definitions before moving forward
        self.displayed_img = None # There may be different images displayed than what is actually the state of the tile
        self.hidden_state = hidden_state
        self.hidden_state_img = None # user can cycle through ? < ' ' etc so this shouldn't be one fixed value



        self.isHidden = isHidden
