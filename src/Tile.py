# import Game
from itertools import cycle

class Tile:
    hidden_states = cycle(('<', '?' ' ')) # Corresponds to blank tile, flagged tile, questioned tile
    # bomb states are represented as !: bomb, X: incorrectly marked bomb, *: activated bomb

    def __init__(self, revealed_state, hidden_state = ' ', isHidden = True):
        self.revealed_state = revealed_state
        self.hidden_state = hidden_state
        self.isHidden = isHidden

    # TODO: improve implementation so that correct hidden state and correct bomb state are displayed
    def get_displayed_state(self):
        if self.isHidden:
            return self.hidden_state
        else: return self.revealed_state

    def cycle_hidden_state(self):
        self.hidden_state = next(Tile.hidden_states)

    def reveal(self):
        self.isHidden = False

bomb = Tile('!')
print(bomb.get_displayed_state())
print(bomb.revealed_state)
bomb.cycle_hidden_state()
print(bomb.hidden_state)
bomb.cycle_hidden_state()
print(bomb.hidden_state)
