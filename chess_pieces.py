""" This file creates the pieces. Currently I have only begun to develop the pawn
and rook pieces. If I can get these pieces working, it should be pretty easy to get
the rest of the pieces working except the king which will need lots of special care.
"""

# Create a general class for pieces
class Piece(object):
    moved_yet = False  
    def __init__(self):
        pass    

#movement_type = a list of booleans, whether or not a piece can move:
# 1. horizontal 2. vertical 3. diagonal 4. knight

class Pawn(Piece):
    type_piece = "pawn"
    movement_type = [False, True, True, False]
    #spaces_can_move = 2
    def __init__(self, color, column, row):
        self.color = color
        self.column = column
        self.row = row
        self.occupied_space = board[row][column]
    #Need to add en passant and pawn promotion abilities

class Rook(Piece):
    type_piece = "rook"    
    movement_type = [True, True, False, False]
    spaces_can_move = 7
    def __init__(self, color, column, row):
        self.color = color
        self.column = column
        self.row = row
        self.occupied_space = board[row][column]
        board[column][row].occupying_piece = self

#Creates all the starting white pieces
def create_white_pieces():
    white_pieces = []
    A2Pawn = Pawn("white", 0, 1)
    white_pieces.append(A2Pawn)
    B2Pawn = Pawn("white", 1, 1)
    white_pieces.append(B2Pawn)
    C2Pawn = Pawn("white", 2, 1)
    white_pieces.append(C2Pawn)
    D2Pawn = Pawn("white", 3, 1)
    white_pieces.append(D2Pawn)
    E2Pawn = Pawn("white", 4, 1)
    white_pieces.append(E2Pawn)
    F2Pawn = Pawn("white", 5, 1)
    white_pieces.append(F2Pawn)
    G2Pawn = Pawn("white", 6, 1)
    white_pieces.append(G2Pawn)
    H2Pawn = Pawn("white", 7, 1)
    white_pieces.append(H2Pawn)
    WQRook = Rook("white", 0, 0)
    white_pieces.append(WQRook)
    WQKnight = Knight("white", 2, 0)
    white_pieces.append(WQKnight)
    WQBishop = Bishop("white", 1, 0)
    white_pieces.append(WQBishop)
    WQueen = Queen("white", 3, 0)
    white_pieces.append(WQueen)
    WKing = King("white", 4, 0)
    white_pieces.append(WKing)
    WKBishop = Bishop("white", 6, 0)
    white_pieces.append(WKBishop)
    WKKnight = Knight("white", 5, 0)
    white_pieces.append(WKKnight)
    WKRook = Rook("white", 7, 0)
    white_pieces.append(WKRook)    
    return white_pieces

###I need to update the board to show the position of all the pieces

#Creates all the starting black pieces
def create_black_pieces():
    black_pieces = []
    A7Pawn = Pawn("black", 0, 6)
    black_pieces.append(A7Pawn)
    B7Pawn = Pawn("black", 1, 6)
    black_pieces.append(B7Pawn)
    C7Pawn = Pawn("black", 2, 6)
    black_pieces.append(C7Pawn)
    D7Pawn = Pawn("black", 3, 6)
    black_pieces.append(D7Pawn)
    E7Pawn = Pawn("black", 4, 6)
    black_pieces.append(E7Pawn)
    F7Pawn = Pawn("black", 5, 6)
    black_pieces.append(F7Pawn)
    G7Pawn = Pawn("black", 6, 6)
    black_pieces.append(G7Pawn)
    H7Pawn = Pawn("black", 7, 6)
    black_pieces.append(H7Pawn)
    BQRook = Rook("black", 0, 7)
    black_pieces.append(BQRook)
    BQKnight = Knight("black", 1, 7)
    black_pieces.append(BQKnight)
    BQBishop = Bishop("black", 2, 7)
    black_pieces.append(BQBishop)
    BQueen = Queen("black", 3, 7)
    black_pieces.append(BQueen)
    BKing = King("black", 4, 7)
    black_pieces.append(BKing)
    BKBishop = Bishop("black", 5, 7)
    black_pieces.append(BKBishop)
    BKKnight = Knight("black", 6, 7)
    black_pieces.append(BKKnight)
    BKRook = Rook("black", 7, 7)
    black_pieces.append(BKRook)
    return black_pieces




