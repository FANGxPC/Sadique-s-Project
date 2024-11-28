import json

class GameStats:
    def __init__(self,ai_game):
        self.settings=ai_game.sett
        self.reset_stats()
        self.game_active=False

        self.high_score=0
        with open('high.json','r') as file:
            self.high_score=json.load(file)
        self.level=1
    def reset_stats(self):
        self.ships_left=self.settings.ship_limit
        self.score=0
        