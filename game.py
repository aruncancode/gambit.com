from board import *
from piece import *


class Game:
    def __init__(self):
        self.board = Board()
        return

    def pgn_parser(self, pgn):
        moves = []
        ret = {"w": [], "b": [], "result": ""}
        e = 2
        pgn = " ".join(pgn.splitlines())

        while e:
            a = pgn.split(str(e) + ".")[0]
            if len(a) > 0:
                moves.append(a)
                ret["w"].append(a.split()[1])
                ret["b"].append(a.split()[2])
                ret["result"] = a.split()[-1]
                pgn = pgn.replace(a, "")
                e += 1
            else:
                e = 0
                moves[-1] = " ".join(moves[-1].split()[:-1])
                if ret["b"][-1] in ["0-1", "0.5-0.5", "1-0"]:
                    ret["b"].pop(-1)
        return moves

    def move_parser(self, move):

        location = []
        piece = ""
        action = None
        full_move = move

        if "x" in move:
            action = "Capture"
            move = move.replace("x", "")
        if "+" in move:
            action = "Check"
            move = move.replace("+", "")
        if "#" in move:
            action = "Checkmate"
            move = move.replace("#", "")

        if move[0] in [chr(e) for e in range(97, 105)]:
            piece = move[0]
        elif move[0] in ["N", "B", "Q", "K", "R"]:
            piece = move[0]
        elif move in ["O-O-O", "O-O"]:
            piece = move
            location = ["", move]
            action = "Castles"

        if move not in ["O-O-O", "O-O"]:
            if len(move) > 3:
                location = [move[1], move[-2:]]
            else:
                location = ["", move[-2:]]

        return piece, location, action, full_move

    def analyse(self, pgn):
        position = self.pgn_parser(pgn)
        for e in position:
            a = self.move_parser(e.split()[1])
            b = self.move_parser(e.split()[2])
            # print(a, b)

            self.move(a[0], a[1], a[2], "w", a[-1])
            self.move(b[0], b[1], b[2], "b", b[-1])

    def move(self, piece, location, action, player, move):
        # print(len(self.board.allMoves("b")))
        print(self.board.allMoves("b"))

        print(move)

        for moves in self.board.allMoves(player):
            if move in moves[1:]:                
                self.board.move(self.board.locate(moves[0]), location[1])
        
        # self.board.show()




        # elif len(location[1]) > 1:
        #     self.board.move(location, piece)
        # else:
        #     self.board.move(location, piece)






    # def possibleMoves(self):
    #     ret = []
    #     return ret

    # def inCheck(self):
    #     ok = 1
    #     return ok

    # def ischeckMate(self):
    #     ok = 0
    #     return ok

    # def isStalemate(self):
    #     ok = 0
    #     return ok

    # def validPosition(self):
    #     ok = 0
    #     return ok

