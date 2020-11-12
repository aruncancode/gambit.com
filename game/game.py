from board import *
from piece import *


class Game:
    def __init__(self):
        self.board = Board()
        return

    def reset(self):
        self.__init__()

    # def pgn_parser(self, pgn):
    #     moves = []
    #     ret = {"w": [], "b": [], "result": ""}
    #     e = 2
    #     pgn = " ".join(pgn.splitlines())

    #     while e:
    #         a = pgn.split(str(e) + ".")[0]
    #         if len(a) > 0:
    #             moves.append(a)
    #             ret["w"].append(a.split()[1])
    #             ret["b"].append(a.split()[2])
    #             ret["result"] = a.split()[-1]
    #             pgn = pgn.replace(a, "")
    #             e += 1
    #         else:
    #             e = 0
    #             moves[-1] = " ".join(moves[-1].split()[:-1])
    #             if ret["b"][-1] in ["0-1", "0.5-0.5", "1-0"]:
    #                 ret["b"].pop(-1)
    #     return moves

    # def move_parser(self, move):

    #     location = []
    #     piece = ""
    #     action = None
    #     full_move = move
    #     if "x" in move:
    #         action = "Capture"
    #     if "+" in move:
    #         action = "Check"
    #         move = move.replace("+", "")
    #     if "#" in move:
    #         action = "Checkmate"
    #         move = move.replace("#", "")

    #     if move[0] in [chr(e) for e in range(97, 105)]:
    #         piece = move[0]
    #     elif move[0] in ["N", "B", "Q", "K", "R"]:
    #         piece = move[0]
    #     elif move in ["O-O-O", "O-O"]:
    #         piece = move
    #         location = ["", move]
    #         action = "Castles"

    #     if move not in ["O-O-O", "O-O"]:
    #         if len(move) > 3:
    #             location = [move[1], move[-2:]]
    #         else:
    #             location = ["", move[-2:]]

    #     return piece, location, action, move

    def pgn_parser(self, pgn):
        out = []
        cur = []
        if len(pgn) == 1:
            return [[pgn[-1], "OG"]]
        for i in range(0, len(pgn)):
            cur.append(pgn[i])
            if i % 2 == 1:
                out.append(cur)
                cur = []
            if i == len(pgn)-1 and len(pgn)%2==1:
                cur = [pgn[i], "OG"]
                out.append(cur)
        return out

    def analyse(self, pgn):
        position = self.pgn_parser(pgn)
        parsed_moves = []
        for moves in position:
            a = moves[0]
            b = moves[-1]
            a_test = self.move(a[-2:], "w", a)
            b_test = self.move(b[-2:], "b", b)
            # self.board.show()
            if a_test[0] == False:
                return [False]
            if b_test[0] == False:
                return [False]
            # self.board.show()
            parsed_moves.append([a, a_test[-1]])
            parsed_moves.append([b, b_test[-1]])
        if position[-1][-1] == "OG":
            parsed_moves.pop(-1)
        return [True, parsed_moves]

    def move(self, location, colour, move):
        parsed_moves = ""
        l = "abcdefgh"
        op_colour = "w" if "w" != colour else "b"
        if move == "OG":
            return [True]
        possible_moves = flatten(self.board.allMoves(colour))
        print(move, possible_moves)

        for e in range(len(possible_moves)):
            if move == possible_moves[e]:
                break
            if e == len(possible_moves)-1:
                return [False]

        for ids in self.board.allMoves(colour):
            if move in self.board.allMoves(colour)[ids]:
                king_location = self.board.locate("KING" + colour.upper())
                if move == "O-O":
                    rook_location = self.board.locate("ROOK" + colour.upper() + "2")
                    self.board.move(
                        king_location,
                        l[(int(l.index(king_location[0])) + 2)] + king_location[1],
                    )
                    self.board.move(
                        rook_location,
                        l[(int(l.index(rook_location[0])) - 2)] + rook_location[1],
                    )
                elif move == "O-O-O":
                    rook_location = self.board.locate("ROOK" + colour.upper() + "1")
                    self.board.move(
                        king_location,
                        l[(int(l.index(king_location[0])) - 2)] + king_location[1],
                    )
                    self.board.move(
                        rook_location,
                        l[(int(l.index(rook_location[0])) + 3)] + rook_location[1],
                    )
                else:
                    self.board.move(self.board.locate(ids), location)
                    parsed_moves = ids
            # else:
            #     print(move)
            #     return False

        # self.board.show()
        # print(move)
        if self.board.inCheck(colour, self.board.allMoves(op_colour)) == False:
            return [1, parsed_moves]
        else:
            return [0]
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
