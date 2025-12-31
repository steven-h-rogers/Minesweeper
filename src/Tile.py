class Tile:
    TILE_WIDTH = 32
    TILE_HEIGHT = 32

    STATE_ATLAS = {
                   '!' : 'bomb',
                   '<' : 'flag',
                   '?': 'questionable',
                   '0': 'none',
                   '1': ''}
    

    def __init__(self, displayed_state, hidden_state = 'plain', isHidden = True):
        self.displayed_state = displayed_state
        self.hidden_state = hidden_state
        self.isHidden = isHidden