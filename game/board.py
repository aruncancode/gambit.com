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

        self.board[0][0] = Rook("a8", "b", "ROOKB1")
        self.board[0][1] = Knight("b8", "b", "KNIGHTB1")
        self.board[0][2] = Bishop("c8", "b", "BISHOPB1")
        self.board[0][3] = Queen("d8", "b", "QUEENB")
        self.board[0][4] = King("e8", "b", "KINGB")
        self.board[0][5] = Bishop("f8", "b", "BISHOPB2")
        self.board[0][6] = Knight("g8", "b", "KNIGHTB2")
        self.board[0][7] = Rook("h8", "b", "ROOKB2")

        self.board[1][0] = Pawn("a7", "b", "PAWNBA")
        self.board[1][1] = Pawn("b7", "b", "PAWNBB")
        self.board[1][2] = Pawn("c7", "b", "PAWNBC")
        self.board[1][3] = Pawn("d7", "b", "PAWNBD")
        self.board[1][4] = Pawn("e7", "b", "PAWNBE")
        self.board[1][5] = Pawn("f7", "b", "PAWNBF")
        self.board[1][6] = Pawn("g7", "b", "PAWNBG")
        self.board[1][7] = Pawn("h7", "b", "PAWNBH")

        self.board[7][0] = Rook("a1", "w", "ROOKW1")
        self.board[7][1] = Knight("b1", "w", "KNIGHTW1")
        self.board[7][2] = Bishop("c1", "w", "BISHOPW1")
        self.board[7][3] = Queen("d1", "w", "QUEENW")
        self.board[7][4] = King("e1", "w", "KINGW")
        self.board[7][5] = Bishop("f1", "w", "BISHOPW2")
        self.board[7][6] = Knight("g1", "w", "KNIGHTW2")
        self.board[7][7] = Rook("h1", "w", "ROOKW2")

        self.board[6][0] = Pawn("a2", "w", "PAWNWA")
        self.board[6][1] = Pawn("b2", "w", "PAWNWB")
        self.board[6][2] = Pawn("c2", "w", "PAWNWC")
        self.board[6][3] = Pawn("d2", "w", "PAWNWD")
        self.board[6][4] = Pawn("e2", "w", "PAWNWE")
        self.board[6][5] = Pawn("f2", "w", "PAWNWF")
        self.board[6][6] = Pawn("g2", "w", "PAWNWG")
        self.board[6][7] = Pawn("h2", "w", "PAWNWH")



    def move(self,initial_location, final_location):
        # print(initial_location, final_location)

        #killing the piece that is being captured if so
        # if self.board[8-int(final_location[1])][l.index(final_location[0])] !=0:
        #     self.board[8-int(final_location[1])][l.index(final_location[0])]

        #setting final location of piece to contain the piece object
        self.board[8-int(final_location[1])][l.index(final_location[0])]=self.board[8-int(initial_location[1])][l.index(initial_location[0])]
        self.board[8-int(final_location[1])][l.index(final_location[0])].updateLocation(final_location)


        #setting inital location of piece to empty
        self.board[8-int(initial_location[1])][l.index(initial_location[0])] = 0
        return 


    def locate(self, id):
        for row_i, row in enumerate(self.board):
            for square_i, square in enumerate(row):
               if square != 0 and square.id == id:
                   return l[square_i]+str(8-row_i) 


    def allMoves(self, colour):
        board = self.board
        moves = {"b" : {}, "w" : {}}
        for i in range(8):
            for e in range(8):
                if board[i][e] != 0:
                    moves[board[i][e].colour][board[i][e].id] = (board[i][e].possibleMoves(board))
        
        # castles
        for i in range(8):
            for e in range(8):
                if board[i][e] !=0 and board[i][e].id == "KING" + colour.upper() and board[i][e].hasMoved == False:
                    if board[i][e+1] ==0 and board[i][e+2] ==0:
                        moves[colour]["KING"+colour.upper()].append("O-O")
                        break

        return moves[colour] if colour != None else moves

    def show(self):
        a =[[square.id if square !=0 else 0 for square in row] for row in self.board]
        for e in a:
            print(e)
            # print("\n")