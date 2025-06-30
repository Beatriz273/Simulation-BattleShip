from .player import Player

class Ship:
    def __init__(self, row, col, size, orientation):
        self.row = row
        self.col = col
        self.size = size
        self.orientation = orientation
        self.indexes = self.compute_indexes()

    def compute_indexes(self):
        start = self.row * 10 + self.col
        if self.orientation == "h":
            return [start + i for i in range(self.size)]
        elif self.orientation == "v":
            return [start + i * 10 for i in range(self.size)]

class Game:
    def __init__(self):

        # Instantiate players
        self.player1 = Player()
        self.player2 = Player()

        # Player 1 turn
        self.player1_turn = True

        self.over = False
        self.result = None

        if self.player1.name == self.player2.name:
            self.player2.name = Player.pick_unique_name(exclude=self.player1.name)

        if self.player1.strategy_name == self.player2.strategy_name:
            self.player2.strategy_name = Player.pick_unique_strategy(exclude=self.player1.strategy_name)

    def make_move(self, position):

        player = self.player1 if self.player1_turn else self.player2
        opponent = self.player2 if self.player1_turn else self.player1
        hit = False

        if position in opponent.indexes:
            player.search[position] = "H"
            hit = True
            for ship in opponent.ships:
                if all(player.search[pos] != "U" for pos in ship.indexes):
                    for pos in ship.indexes:
                        player.search[pos] = "D"
        else:
            player.search[position] = "M"

        if all(player.search[i] != "U" for i in opponent.indexes):
            self.over = True
            self.result = player.name

        if not hit:
            self.player1_turn = not self.player1_turn
