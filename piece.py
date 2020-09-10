l = "abcdefgh"

class Piece:

    def __init__(self, location, colour):
        self.y = 8- int(location[1])
        self.x = l.index(location[0])
        self.location = location
        self.colour = colour
        self.pMoves = []
        self.alive = True


    def updateMoves(self, board):
        self.pMoves = self.possibleMoves(board)

    def updateLocation(self, location):
        self.y = location[1]
        self.x = location[0]
    
    def Kill(self):
        self.alive = False


class Pawn(Piece):

    def __init__(self, location, colour):
        super().__init__(location, colour)
        self.queen = False

    def possibleMoves(self, board):
        y = 8- int(self.location[1])
        x = l.index(self.location[0])
        moves = []



        if not self.queen:
            if self.colour == "w":

                #check for promotion
                if y == 0:
                    self.queen = True

                #check for pawns on second rank
                if y == 6 and board[y-1][x] == 0:
                    if board[y-2][x] ==0:
                        moves.append((l[x]+str(8-(y-1))))
                        moves.append((l[x]+str(8-(y-2))))
                    else:
                        moves.append((l[x]+str(8-(y-1))))
                
                #check for pawns moving forward - not on second rank
                if y != 6 and board[y-1][x] == 0:
                    moves.append((l[x]+str(8-(y-1))))
                
                #diagonal (captures) (left)
                if board[y-1][x-1] !=0 and board[y-1][x-1].colour != self.colour:
                        moves.append((l[x-1]+str(8-(y-1))))
                
                #diagonal (captures) (right)
                if board[y-1][x+1] !=0 and board[y-1][x+1].colour != self.colour:
                        moves.append((l[x+1]+str(8-(y-1))))

            
            if self.colour == "b":

                #check for promotion
                if y == 7:
                    self.queen = True
                
                #check for pawns on seventh rank
                if y==1 and board[y+1][x] == 0:
                    if board[y+2][x] ==0:
                        moves.append((l[x]+str(8-(y+1))))
                        moves.append((l[x]+str(8-(y+2))))
                    else:
                        moves.append((l[x]+str(8-(y+1))))
                        
                #check for pawns moving forward
                if y != 1 and board[y+1][x] == 0:
                    moves.append((l[x]+str(8-(y+1))))
                
                #diagonal (captures) (left)
                if board[y+1][x-1] !=0 and board[y+1][x-1].colour != self.colour:
                        moves.append((l[x-1]+str(8-(y+1))))
                
                #diagonal (captures) (right)
                if board[y+1][x+1] !=0 and board[y+1][x+1].colour != self.colour:
                        moves.append((l[x+1]+str(8-(y+1))))


            


        return moves

class King(Piece):

    def __init__(self, location, colour):
        super().__init__(location, colour)

    def possibleMoves(self, board):
        self.y = 8- int(location[1])
        self.x = l.index(location[0])
        moves = []
        return moves

class Queen(Piece):

    def __init__(self, location, colour):
        super().__init__(location, colour)

    def possibleMoves(self, board):
        self.y = 8- int(location[1])
        self.x = l.index(location[0])
        moves = []
        return moves

class Bishop(Piece):

    def __init__(self, location, colour):
        super().__init__(location, colour)

    def possibleMoves(self, board):
        self.y = 8- int(location[1])
        self.x = l.index(location[0])
        moves = []
        return moves

class Knight(Piece):

    def __init__(self, location, colour):
        super().__init__(location, colour)

    def possibleMoves(self, board):
        self.y = 8- int(location[1])
        self.x = l.index(location[0])
        moves = []
        return moves

class Rook(Piece):

    def __init__(self, location, colour):
        super().__init__(location, colour)

    def possibleMoves(self, board):
        self.y = 8- int(location[1])
        self.x = l.index(location[0])
        moves = []
        return moves