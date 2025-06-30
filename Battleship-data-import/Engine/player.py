import random
import json
from .strategy import Strategies

NAMES = [ "Alex", "Jordan", "Taylor", "Morgan", "Riley",
    "Casey", "Skyler", "Drew", "Quinn", "Jamie"]

class Loader:
    @staticmethod
    def load_board_data(board_strategy_file="board_strategie.json"):
        try:
            with open(board_strategy_file, "r") as file:
                board_data = json.load(file)
                return board_data.get('board_strategie', [])
        except Exception as e:
            print(f"Erro ao carregar estratégias de tabuleiro: {e}")
            return []

class Player:
    board_strategies = Loader.load_board_data()

    def __init__(self, name=None):

        # Choose player name
        self.name = name or self.pick_unique_name()

        self.ships = []
        self.search = ["U"] * 100
        self.indexes = []

        # Choose game strategy
        self.strategy_name = self.pick_unique_strategy()

        # Choose game board
        self.place_ships(random.choice(Player.board_strategies))

    @staticmethod
    def pick_unique_name(exclude=None):
        options = [n for n in NAMES if n != exclude]
        return random.choice(options)
    
    @staticmethod
    def pick_unique_strategy(exclude=None):
        strategies = Strategies().available_strategies
        options = [s for s in strategies if s != exclude]
        return random.choice(options)

    def place_ships(self, strategy):
        from .game import Ship
        for ship_data in strategy:
            ship = Ship(**ship_data)
            self.ships.append(ship)
            self.indexes.extend(ship.indexes)
