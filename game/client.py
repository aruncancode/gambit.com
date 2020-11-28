import uuid

class Player():
    def __init__(self, name, player_id, websocket, colour):
        self.name = name
        self.websocket = websocket
        self.colour = colour
        self.player_id = player_id
        self.pool = []
    
    def add_game(self, game_id):
        self.game_id = id
    
    def leave_game(self):
        self.game_id = None

class CurrentGame():
    def __init__(self, type, game_id):
        self.type = type
        self.game_id = game_id
        self.players = []
        self.pool = 0
        self.pgn = []
    
    def add_player(self, player_object):
        self.players.append(player_object)
        self.pool +=1
    
    def get_opponent(self, colour):
        return [e.websocket for e in self.players if e.colour != colour][-1]
    
    def end(self, winner, reason):
        print(winner, "wins by", reason)
    
    def move(self, move):
        self.pgn.append(move)