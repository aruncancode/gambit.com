from piece import King
from piece import Queen
from piece import Rook
from piece import Bishop
from piece import Knight
from piece import Pawn

l = "abcdefgh"


class Board:
    def __init__(self):
        self.board = [[0 for x in range(8)] for _ in range(8)]

        self.board[0][0] = Rook("a8", "b")
        self.board[0][1] = Knight("b8", "b")
        self.board[0][2] = Bishop("c8", "b")
        self.board[0][3] = Queen("d8", "b")
        self.board[0][4] = King("e8", "b")
        self.board[0][5] = Bishop("f8", "b")
        self.board[0][6] = Knight("g8", "b")
        self.board[0][7] = Rook("h8", "b")

        self.board[1][0] = Pawn("a7", "b")
        self.board[1][1] = Pawn("b7", "b")
        self.board[1][2] = Pawn("c7", "b")
        self.board[1][3] = Pawn("d7", "b")
        self.board[1][4] = Pawn("e7", "b")
        self.board[1][5] = Pawn("f7", "b")
        self.board[1][6] = Pawn("g7", "b")
        self.board[1][7] = Pawn("h7", "b")

        self.board[7][0] = Rook("a1", "w")
        self.board[7][1] = Knight("b1", "w")
        self.board[7][2] = Bishop("c1", "w")
        self.board[7][3] = Queen("d1", "w")
        self.board[7][4] = King("e1", "w")
        self.board[7][5] = Bishop("f1", "w")
        self.board[7][6] = Knight("g1", "w")
        self.board[7][7] = Rook("h1", "w")

        self.board[6][0] = Pawn("a2", "w")
        self.board[6][1] = Pawn("b2", "w")
        self.board[6][2] = Pawn("c2", "w")
        self.board[6][3] = Pawn("d2", "w")
        self.board[6][4] = Pawn("e2", "w")
        self.board[6][5] = Pawn("f2", "w")
        self.board[6][6] = Pawn("g2", "w")
        self.board[6][7] = Pawn("h2", "w")

    def move(self, piece, location):
        col, row = location[1][0], location[1][1]
        x = location[0]
        t_row = 8 - int(row)
        t_col = l.index(col)
        for row_i, row in enumerate(self.board):
            for square_i, square in enumerate(row):
                if square == piece:
                    if x == 0:
                        self.board[row_i][square_i] = 0
                        self.board[t_row][t_col] = piece
                        self.board[t_row][t_col].location = l[t_col] + str(
                            8 - (t_row - 1)
                        )
                    elif x != 0:
                        if x == l[row_i]:
                            self.board[row_i][square_i] = 0
                            self.board[t_row][t_col] = piece
                            self.board[t_row][t_col].location = l[t_col] + str(
                                8 - (t_row - 1)
                            )

    def allMoves(self):
        moves = []
        for i in range(8):
            for e in range(8):
                if self.board[i][e] != 0:
                    moves.append(self.board[i][e].possibleMoves(self.board))
        return moves

    
    

