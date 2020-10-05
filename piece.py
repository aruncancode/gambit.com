from board import *
l = "abcdefgh"

def allMoves(board, colour):
    moves = []
    for i in range(8):
        for e in range(8):
            if board[i][e] != 0:
                if board[i][e].colour == colour:
                    moves.append(board[i][e].possibleMoves(board))
    return moves

class Piece:
    def __init__(self, location, colour, id):
        self.y = 8 - int(location[1])
        self.x = l.index(location[0])
        self.location = location
        self.colour = colour
        self.pMoves = []
        self.alive = True
        self.id = id

    def updateLocation(self, location):
        self.location = location

    def Kill(self):
        self.alive = False


class Pawn(Piece):
    def __init__(self, location, colour, id):
        super().__init__(location, colour, id)
        self.queen = False
        self.type = "Pawn"
        self.name = self.location[0]


    def possibleMoves(self, board):
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        moves = []

        if not self.queen:
            if self.colour == "w":

                # check for promotion
                if y == 0:
                    self.queen = True

                # check for pawns on second rank
                if y == 6 and board[y - 1][x] == 0:
                    if board[y - 2][x] == 0:
                        moves.append((l[x] + str(8 - (y - 1))))
                        moves.append((l[x] + str(8 - (y - 2))))
                    else:
                        moves.append((l[x] + str(8 - (y - 1))))

                # check for pawns moving forward - not on second rank
                if y != 6 and board[y - 1][x] == 0:
                    moves.append((l[x] + str(8 - (y - 1))))

                # diagonal (captures) (left)
                if (
                    board[y - 1][x - 1] != 0
                    and board[y - 1][x - 1].colour != self.colour
                ):
                    moves.append( (l[x] +"x" +l[x - 1] + str(8 - (y - 1))))

                # diagonal (captures) (right)
                if (
                    x != 7
                    and board[y - 1][x + 1] != 0
                    and board[y - 1][x + 1].colour != self.colour
                ):
                    moves.append((l[x] +"x" +l[x + 1] + str(8 - (y - 1))))

            if self.colour == "b":
                # check for promotion
                if y == 7:
                    self.queen = True

                # check for pawns on seventh rank
                if y == 1 and board[y + 1][x] == 0:
                    if board[y + 2][x] == 0:
                        moves.append((l[x] + str(8 - (y + 1))))
                        moves.append((l[x] + str(8 - (y + 2))))
                    else:
                        moves.append((l[x] + str(8 - (y + 1))))

                # check for pawns moving forward
                if y != 1 and board[y + 1][x] == 0:
                    moves.append((l[x] + str(8 - (y + 1))))

                # diagonal (captures) (left)
                if (
                    x != 0
                    and board[y + 1][x - 1] != 0
                    and board[y + 1][x - 1].colour != self.colour
                ):
                    moves.append((l[x] +"x" +l[x - 1] + str(8 - (y + 1))))

                # diagonal (captures) (right)
                if (
                    x != 7
                    and board[y + 1][x + 1] != 0
                    and board[y + 1][x + 1].colour != self.colour
                ):
                    moves.append((l[x] +"x" +l[x + 1] + str(8 - (y + 1))))

        return moves


class King(Piece):
    def __init__(self, location, colour, id):
        super().__init__(location, colour, id)
        self.type = "King"
        self.name = "K"
        self.hasMoved = False

    def possibleMoves(self, board):
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        moves = []
        # Up
        if y != 0 and board[y - 1][x] == 0:
            moves.append((l[x] + str(8 - (y - 1))))
        # Down
        if y != 7 and board[y + 1][x] == 0:
            moves.append((l[x] + str(8 - (y + 1))))
        # Left
        if x != 0 and board[y][x - 1] == 0:
            moves.append((l[x - 1] + str(8 - (y))))
        # Right
        if x != 7 and board[y][x + 1] == 0:
            moves.append((l[x + 1] + str(8 - (y))))
        # TopLeft
        if y != 0 and x != 0 and board[y - 1][x - 1] == 0:
            moves.append((l[x - 1] + str(8 - (y - 1))))
        # TopRight
        if y != 0 and x != 7 and board[y - 1][x + 1] == 0:
            moves.append((l[x + 1] + str(8 - (y - 1))))
        # BottomLeft
        if y != 7 and x != 0 and board[y + 1][x - 1] == 0:
            moves.append((l[x - 1] + str(8 - (y + 1))))
        # BottomRight
        if y != 7 and x != 7 and board[y + 1][x + 1] == 0:
            moves.append((l[x + 1] + str(8 - (y + 1))))

        return moves




class Queen(Piece):
    def __init__(self, location, colour, id):
        super().__init__(location, colour, id)
        self.type = "Queen"
        self.name = "Q"



    def possibleMoves(self, board):
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        moves = []
        # Up
        while y != 0:
            if board[y - 1][x] == 0:
                moves.append("Q" + (l[x] + str(8 - (y - 1))))
            elif board[y - 1][x].colour != self.colour:
                moves.append("Qx" + (l[x] + str(8 - (y - 1))))
                break
            else:
                break
            y -= 1
        # Down
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        while y != 7:
            if board[y + 1][x] == 0:
                moves.append(("Q" + l[x] + str(8 - (y + 1))))
            elif board[y + 1][x] !=0 and board[y + 1][x].colour != self.colour:
                moves.append(("Qx" + l[x] + str(8 - (y + 1))))
                break
            else:
                break
            y += 1
        # #Left
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        while x != 0:
            if board[y][x - 1] == 0:
                moves.append(("Q" + l[x - 1] + str(8 - (y))))
            elif board[y][x - 1].colour != self.colour:
                moves.append( ("Qx" +l[x - 1] + str(8 - (y))))
                break
            else:
                break
            x -= 1
        # #Right
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        while x != 7:
            if board[y][x + 1] == 0:
                moves.append(("Q" + l[x + 1] + str(8 - (y))))
            elif board[y][x + 1].colour != self.colour:
                moves.append(("Qx" + l[x + 1] + str(8 - (y))))
                break
            else:
                break
            x += 1

        # Top Right
        while x != 7 and y != 0:
            if board[y - 1][x + 1] == 0:
                moves.append(("Q" + l[x + 1] + str(8 - (y - 1))))
            elif board[y - 1][x + 1].colour != self.colour:
                moves.append(("Qx" + l[x + 1] + str(8 - (y - 1))))
                break
            else:
                break
            x += 1
            y -= 1

        # Bottom Left
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        while y != 7 and x != 0:
            if board[y + 1][x - 1] == 0:
                moves.append(("Q" + l[x - 1] + str(8 - (y + 1))))
            elif board[y + 1][x - 1].colour != self.colour:
                moves.append(("Qx" + l[x - 1] + str(8 - (y + 1))))
            else:
                break
            x -= 1
            y += 1

        # Top Left
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        while y != 0 and x != 0:
            if board[y - 1][x - 1] == 0:
                moves.append(("Q" +l[x - 1] + str(8 - (y - 1))))
            elif board[y - 1][x - 1]:
                moves.append(("Qx" +l[x - 1] + str(8 - (y - 1))))
            else:
                break
            x -= 1
            y -= 1

        # Bottom Right
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        while y != 7 and x != 7:
            if board[y + 1][x + 1] == 0:
                moves.append(("Q" + l[x + 1] + str(8 - (y + 1))))
            elif board[y + 1][x + 1].colour != self.colour:
                moves.append(("Qx" + l[x + 1] + str(8 - (y + 1))))
            else:
                break
            x += 1
            y += 1

        return moves


class Bishop(Piece):
    def __init__(self, location, colour, id):
        super().__init__(location, colour, id)
        self.type = "Bishop"
        self.name = "B"

    def possibleMoves(self, board):
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        moves = []
        # Top Right
        while x != 7 and y != 0:
            if board[y - 1][x + 1] == 0:
                moves.append(("B" + l[x + 1] + str(8 - (y - 1))))
            elif board[y - 1][x + 1].colour != self.colour:
                moves.append(("Bx" + l[x + 1] + str(8 - (y - 1))))
                break
            else:
                break
            x += 1
            y -= 1
        # Bottom Left
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        while y != 7 and x != 0:
            if board[y + 1][x - 1] == 0:
                moves.append(("B" + l[x - 1] + str(8 - (y + 1))))
            elif board[y + 1][x - 1].colour != self.colour:
                moves.append(("Bx" + l[x - 1] + str(8 - (y + 1))))
            else:
                break
            x -= 1
            y += 1
        # Top Left
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        while y != 0 and x != 0:
            if board[y - 1][x - 1] == 0:
                moves.append(("B" +l[x - 1] + str(8 - (y - 1))))
            elif board[y - 1][x - 1]:
                moves.append(("Bx" +l[x - 1] + str(8 - (y - 1))))
            else:
                break
            x -= 1
            y -= 1
        # Bottom Right
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        while y != 7 and x != 7:
            if board[y + 1][x + 1] == 0:
                moves.append(("B" + l[x + 1] + str(8 - (y + 1))))
            elif board[y + 1][x + 1].colour != self.colour:
                moves.append(("Bx" + l[x + 1] + str(8 - (y + 1))))
            else:
                break
            x += 1
            y += 1

        return moves


class Knight(Piece):
    def __init__(self, location, colour, id):
        super().__init__(location, colour, id)
        self.type = "Knight"
        self.name = "K"


    def possibleMoves(self, board):
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        moves = []

        # TopLeft1
        if y != 0 and y != 1 and x != 7:
            if board[y - 2][x + 1] == 0:
                moves.append("N" + (l[x + 1] + str(8 - (y - 2))))
            elif board[y - 2][x + 1].colour != self.colour:
                moves.append("Nx" + (l[x + 1] + str(8 - (y - 2))))
                
        # TopLeft2
        if y != 0 and x != 6 and x != 7:
            if board[y - 1][x + 2] == 0:
                moves.append("N" +(l[x + 2] + str(8 - (y - 1))))
            elif board[y - 1][x + 2].colour != self.colour:
                moves.append("Nx" +(l[x + 2] + str(8 - (y - 1))))
                
        # TopRight1
        if y != 0 and y != 1 and x != 0:
            if board[y - 2][x - 1] == 0:
                moves.append("N" +(l[x - 1] + str(8 - (y - 2))))
            elif board[y - 2][x - 1].colour != self.colour:
                moves.append("Nx" +(l[x - 1] + str(8 - (y - 2))))

        # TopRight2
        if y != 0 and x != 0 and x != 1:
            if board[y - 1][x - 2] == 0:
                moves.append("N" +(l[x - 2] + str(8 - (y - 1))))
            elif board[y - 1][x - 2].colour != self.colour:
                moves.append("Nx" +(l[x - 2] + str(8 - (y - 1))))

        # BottomLeft1
        if y != 6 and y != 7 and x != 0:
            if board[y + 2][x - 1] == 0:
                moves.append("N" +(l[x - 1] + str(8 - (y + 2))))
            elif board[y + 2][x - 1].colour != self.colour:
                moves.append("Nx" +(l[x - 1] + str(8 - (y + 2))))

        # BottomLeft2
        if y != 7 and x != 0 and x != 1:
            if board[y + 1][x - 2] == 0:
                moves.append("N" +(l[x - 2] + str(8 - (y + 1))))
            elif board[y + 1][x - 2].colour != self.colour:
                moves.append("Nx" +(l[x - 2] + str(8 - (y + 1))))

        # BottomRight1
        if y != 7 and y != 6 and x != 7:
            if  board[y + 2][x + 1] == 0:
                moves.append("N" +(l[x + 1] + str(8 - (y + 2))))
            elif board[y + 2][x + 1].colour != self.colour:
                moves.append("Nx" +(l[x + 1] + str(8 - (y + 2))))
                
        # BottomRight2
        if y != 7 and x != 6 and x != 7:
            if board[y + 1][x + 2] == 0:
                moves.append("N" +(l[x + 2] + str(8 - (y + 1))))
            elif board[y + 1][x + 2].colour != self.colour:
                moves.append("Nx" +(l[x + 2] + str(8 - (y + 1))))

        return moves


class Rook(Piece):
    def __init__(self, location, colour, id):
        super().__init__(location, colour, id)
        self.type = "Rook"
        self.name = "R"


    def possibleMoves(self, board):
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        moves = []

        # Up
        while y != 0:
            if board[y - 1][x] == 0:
                moves.append("R" + (l[x] + str(8 - (y - 1))))
            elif board[y - 1][x].colour != self.colour:
                moves.append("Rx" + (l[x] + str(8 - (y - 1))))
                break
            else:
                break
            y -= 1
        # Down
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        while y != 7:
            if board[y + 1][x] == 0:
                moves.append(("R" + l[x] + str(8 - (y + 1))))
            elif board[y + 1][x] !=0 and board[y + 1][x].colour != self.colour:
                moves.append(("Rx" + l[x] + str(8 - (y + 1))))
                break
            else:
                break
            y += 1
        # #Left
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        while x != 0:
            if board[y][x - 1] == 0:
                moves.append(("R" + l[x - 1] + str(8 - (y))))
            elif board[y][x - 1].colour != self.colour:
                moves.append( ("Rx" +l[x - 1] + str(8 - (y))))
                break
            else:
                break
            x -= 1
        # #Right
        y, x = 8 - int(self.location[1]), l.index(self.location[0])
        while x != 7:
            if board[y][x + 1] == 0:
                moves.append(("R" + l[x + 1] + str(8 - (y))))
            elif board[y][x + 1].colour != self.colour:
                moves.append(("Rx" + l[x + 1] + str(8 - (y))))
                break
            else:
                break
            x += 1

        return moves

