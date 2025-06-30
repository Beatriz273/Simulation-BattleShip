import random

class Strategies:
    def __init__(self):
        self.available_strategies = ["Random", "Adjacente", "Lateral"]

    def random_strategy(self, player):
        choices = [i for i, val in enumerate(player.search) if val == "U"]
        return random.choice(choices) if choices else None

    def adjacente_strategy(self, player):
        hits = [i for i, val in enumerate(player.search) if val == "H"]
        candidates = []
        for hit in hits:
            for offset in [-1, 1, -10, 10]:
                neighbor = hit + offset
                if 0 <= neighbor < 100 and player.search[neighbor] == "U":
                    candidates.append(neighbor)
        return random.choice(candidates) if candidates else self.random_strategy(player)

    def lateral_strategy(self, player):
        lateral = [i for i in range(100)
                   if (i // 10 in [0, 9] or i % 10 in [0, 9]) and player.search[i] == "U"]
        return random.choice(lateral) if lateral else self.random_strategy(player)
