# from game import Game
from game import *


# pgn = [["d4", "e5"], ["e3", "Bb4"], ["c3", "f6"] ,["Nf3", "f5"], ["Ne5", "Bc3"], ["Nc3", "f4"]]
# pgn = ['f4', 'd5', 'Nc3', 'c6', 'd3', 'Nd7']
pgn = ['Nf3', 'd5', 'd4', 'Nc6', 'Bf4', 'e5', 'de5', 'd4', 'Nd4', 'Qd4', 'Qd4', 'Nd4', 'Nc3', 'Nc2', 'Kd2', 'Na1', 'Kc1', 'Bf5', 'Kd1', 'Nc2', 'h3', 'Rd8', 'Kc1', 'Ba3', 'ba3', 'Nf6', 'e6', 'fe6', 'Be5', 'Ne4', 'Bg7']
game = Game()
# print(game.pgn_parser(pgn))
print(game.analyse(pgn))
