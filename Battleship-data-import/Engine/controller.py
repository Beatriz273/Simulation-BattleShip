from .strategy import Strategies

class PlayerController:
    def __init__(self, game):
        self.game = game
        self.next_move = None

    def player_turn(self):
        current_player = self.game.player1 if self.game.player1_turn else self.game.player2
        strategy_func = getattr(Strategies(), f"{current_player.strategy_name.lower()}_strategy")
        self.next_move = strategy_func(current_player)
