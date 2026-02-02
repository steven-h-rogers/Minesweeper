# import Game
from itertools import cycle

class Tile:
    hidden_states = cycle(('<', '?' ,' ')) # Corresponds to blank tile, flagged tile, questioned tile
    # bomb states are represented as !: bomb, X: incorrectly marked bomb, *: activated bomb

    def __init__(self, revealed_state,  row, col, hidden_state = ' ', isHidden = True):
        self.revealed_state = revealed_state
        self.hidden_state = hidden_state
        self.displayed_state = hidden_state
        self.isHidden = isHidden
        self.row = row
        self.col = col


    # TODO: improve implementation so that correct hidden state and correct bomb state are displayed
    def change_displayed_state(self):
        if self.isHidden == True:
            self.displayed_state = self.hidden_state
        else: 
            self.displayed_state = self.revealed_state


    def cycle_hidden_state(self):
        if self.isHidden:
            self.hidden_state = next(Tile.hidden_states)
            self.displayed_state = self.hidden_state
            print("hidden state is now: ", self.hidden_state)

    def reveal(self):
        self.isHidden = False
        self.change_displayed_state()
        # print(self.hidden_state, self.revealed_state, self.isHidden)

    def explode(self):
        self.revealed_state = '*'
    
    def incorrectly_marked(self):
        self.revealed_state = 'X'

bomb = Tile('!', 0, 0)
two = Tile('2', 0, 1)

print(bomb.displayed_state)
print(two.displayed_state)

bomb.cycle_hidden_state()
two.cycle_hidden_state()

print(bomb.displayed_state)
print(two.displayed_state)

bomb.change_displayed_state()
two.change_displayed_state()

print(bomb.displayed_state)
print(two.displayed_state)
