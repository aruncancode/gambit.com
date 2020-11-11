# from game import Game
from game import *


# pgn = [["d4", "e5"], ["e3", "Bb4"], ["c3", "f6"] ,["Nf3", "f5"], ["Ne5", "Bc3"], ["Nc3", "f4"]]
# pgn = ['f4', 'd5', 'Nc3', 'c6', 'd3', 'Nd7']
pgn = ['e4', 'Bd6']
game = Game()
# print(game.pgn_parser(pgn))
print(game.analyse(pgn))
