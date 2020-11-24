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

    def analyse(self, pgn, board=None):
        if board == None:
            board=self.board
        position = self.pgn_parser(pgn)
        parsed_moves = []
        for moves in position:
            a = moves[0]
            b = moves[-1]
            a_test = self.move(a[-2:], "w", a)
            b_test = self.move(b[-2:], "b", b)
            if a_test[0] == 0:
                return [0]
            if b_test[0] == 0:
                return [0]
            parsed_moves.append([a, a_test[-1]])
            parsed_moves.append([b, b_test[-1]])
        if position[-1][-1] == "OG":
            parsed_moves.pop(-1)
        return [1, parsed_moves]

    def move(self, location, colour, move, board):
        parsed_moves = []
        l = "abcdefgh"
        op_colour = "w" if "w" != colour else "b"
        if move == "OG":
            return [1]
        possible_moves = flatten(board.allMoves(colour))

        for e in range(len(possible_moves)):
            if move == possible_moves[e]:
                break
            if e == len(possible_moves)-1:
                return [0]

        for ids in board.allMoves(colour):
            if move in board.allMoves(colour)[ids]:
                king_location = board.locate("KING" + colour.upper())
                if move == "O-O":
                    rook_location = board.locate("ROOK" + colour.upper() + "2")
                    board.move(
                        king_location,
                        l[(int(l.index(king_location[0])) + 2)] + king_location[1],
                    )
                    parsed_moves.append(ids)
                    board.move(
                        rook_location,
                        l[(int(l.index(rook_location[0])) - 2)] + rook_location[1],
                    )
                    parsed_moves.append("ROOK" + colour.upper() + "2")
                elif move == "O-O-O":
                    rook_location = board.locate("ROOK" + colour.upper() + "1")
                    board.move(
                        king_location,
                        l[(int(l.index(king_location[0])) - 2)] + king_location[1]
                    )
                    parsed_moves.append(ids)
                    board.move(rook_location, l[(int(l.index(rook_location[0])) + 3)] + rook_location[1])
                    parsed_moves.append("ROOK" + colour.upper() + "1")
                else:
                    board.move(board.locate(ids), location)
                    if "KING" in ids:
                        board.get_piece(ids).hasMoved = True
                    parsed_moves = ids
            # else:
            #     print(move)
            #     return False

        # board.show()
        # print(move)
        print(move , board.allMoves(op_colour))
        if board.inCheck(colour, board.allMoves(op_colour)) == False:
            if board.inCheck(op_colour, board.allMoves(colour)) == True:
                if len(self.kingMoves(pgn[:-1], op_colour, flatten(board.allMoves(op_colour)))) == 0:
                    return [2, parsed_moves]
            return [1, parsed_moves]
        else:
            return [0]
        # elif len(location[1]) > 1:
        #     self.board.move(location, piece)
        # else:
        #     self.board.move(location, piece)

    def kingMoves(self, pgn, colour, possible_moves):
        # colour refers to the colour of the player we're checking for checkmate
        # possible moves refer to the moves of the player with the same colour
        board2 = Board()
        king_moves = []

        for move in possible_moves:
            self.analyse(pgn, board=board2)
            if self.board.inCheck(colour, self.board.allMoves(op_colour)):
                self.reset()
                possible_moves.remove(move)
            else:
                king_moves.append(move)
            


    def get(self,id):
        return self.board.get_piece(id)


def flatten(dict):
    a = []
    for key in dict:
        for move in dict[key]:
            a.append(move)
    return a
