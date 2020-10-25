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

        return piece, location, action, move

    def analyse(self, pgn):
        position = self.pgn_parser(pgn)
        for e in position:
            a = self.move_parser(e.split()[1])
            b = self.move_parser(e.split()[2])
            # print(a, b)
            if self.move(a[0], a[1], a[2], "w", a[-1]) == False:
                return False
            if self.move(b[0], b[1], b[2], "b", b[-1]) == False:
                return False
        return True

    def move(self, piece, location, action, colour, move):
        l = "abcdefgh"
        op_colour = "w" if "w" != colour else "b"

        # print(len(self.board.allMoves("b")))
        # print(self.board.allMoves("b"))
        # print(move)
        # print(flatten(self.board.allMoves(colour)))
        # print(self.board.locate("KINGW"))
        if move == "OG":
            return

        if move not in flatten(self.board.allMoves(colour)):
            return False

        for ids in self.board.allMoves(colour):
            if move in self.board.allMoves(colour)[ids]:
                king_location = self.board.locate("KING" + colour.upper())
                if move == "O-O":
                    rook_location = self.board.locate("ROOK" + colour.upper() + "2")
                    self.board.move(king_location, l[(int(l.index(king_location[0])) + 2)] + king_location[1])
                    self.board.move(rook_location, l[(int(l.index(rook_location[0])) -2)] + rook_location[1])
                elif move == "O-O-O":
                    rook_location = self.board.locate("ROOK" + colour.upper() + "1")
                    self.board.move(king_location, l[(int(l.index(king_location[0])) - 2)] + king_location[1])
                    self.board.move(rook_location, l[(int(l.index(rook_location[0])) +3)] + rook_location[1])
                else:
                    self.board.move(self.board.locate(ids), location[1])
            # else:
            #     print(move)
            #     return False
        
        
        self.board.show()
        # print(move)
        if self.board.inCheck(colour, self.board.allMoves(op_colour)) == False:
            return (True)
        else:
            return (False)
        # elif len(location[1]) > 1:
        #     self.board.move(location, piece)
        # else:
        #     self.board.move(location, piece)




        

    # def inCheck(self, colour):
    #     opponent_colour = "b" if colour == "w" else "w"
    #     king_location = self.board.locate("KING" + colour.upper())
    #     opponent_moves = self.board.allMoves(opponent_colour)
    #     for pieces in opponent_moves:
    #         for move in opponent_moves[pieces]:
    #             if king_location in move:
    #                 return True
    #     return False

        
    # def ischeckMate(self):
    #     ok = 0
    #     return ok

    # def isStalemate(self):
    #     ok = 0
    #     return ok

    # def validPosition(self):
    #     ok = 0
    #     return ok

def flatten(dict):
    a = []
    for key in dict:
        for move in dict[key]:
            a.append(move)
    return a