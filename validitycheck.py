class Board:
    def __init__(self):
        self.board = [
            ["rb", "nb", "bb", "qb", "kb", "bb", "nb", "rb"],
            ["ab", "bb", "cb", "db", "eb", "fb", "gb", "hb"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["aw", "bw", "cw", "dw", "ew", "fw", "gw", "hw"],
            ["rw", "nw", "bw", "qw", "kw", "bw", "nw", "rw"],
        ]
        self._something = "abcdefgh"

    def move(self, move, piece):
        col, row = move[0], move[1]
        t_row = 8 - int(row)
        t_col = self._something.index(col)
        for row_i, row in enumerate(self.board):
            for square_i, square in enumerate(row):
                if square == piece:
                    self.board[row_i][square_i] = "  "
                    self.board[t_row][t_col] = piece


class Chess:
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

        location = ""
        piece = ""
        action = None

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
            location = "Castles"
            action = "Castles"

        if move not in ["O-O-O", "O-O"]:
            location = move[-2:]
            # num = str(ord(location[0]) - 96)
            # location = location.replace(location[0], num)

        return piece.lower(), location, action, move

    def analyse(self, pgn):
        position = self.pgn_parser(pgn)
        for e in position:
            a = self.move_parser(e.split()[1])
            b = self.move_parser(e.split()[2])

            # print(a[1])

            # print(a[0], b[0], e)
            self.move(a[0], a[1], a[2], "w", a[-1])
            self.move(b[0], b[1], b[2], "b", b[-1])

    def move(self, piece, location, action, player, move):
        piece = piece + player
        if location == "Castles":
            print(("r" + player))
            self.board.move("f1", ("r" + player))
            self.board.move("g1", ("k" + player))
        else:
            self.board.move(location, piece)

        print(move)
        for row in self.board.board:
            print(row)

        print()

    def inCheck(self):
        ok = 1

        return ok

    def ischeckMate(self):
        ok = 0
        return ok

    def isStalemate(self):
        ok = 0
        return ok

    def validPosition(self):
        ok = 0
        return ok


# work on fixing analysis
# castling
# finish incheck()

