position_into_tuple ={'A1': (1, 1), 'A2': (1, 2), 'A3': (1, 3), 'A4': (1, 4), 'A5': (1, 5), 'A6': (1, 6), 'A7': (1, 7), 'A8': (1, 8), 'B1': (2, 1), 'B2': (2, 2), 'B3': (2, 3), 'B4': (2, 4), 'B5': (2, 5), 'B6': (2, 6), 'B7': (2, 7), 'B8': (2, 8), 'C1': (3, 1), 'C2': (3, 2), 'C3': (3, 3), 'C4': (3, 4), 'C5': (3, 5), 'C6': (3, 6), 'C7': (3, 7), 'C8': (3, 8), 'D1': (4, 1), 'D2': (4, 2), 'D3': (4, 3), 'D4': (4, 4), 'D5': (4, 5), 'D6': (4, 6), 'D7': (4, 7), 'D8': (4, 8), 'E1': (5, 1), 'E2': (5, 2), 'E3': (5, 3), 'E4': (5, 4), 'E5': (5, 5), 'E6': (5, 6), 'E7': (5, 7), 'E8': (5, 8), 'F1': (6, 1), 'F2': (6, 2), 'F3': (6, 3), 'F4': (6, 4), 'F5': (6, 5), 'F6': (6, 6), 'F7': (6, 7), 'F8': (6, 8), 'G1': (7, 1), 'G2': (7, 2), 'G3': (7, 3), 'G4': (7, 4), 'G5': (7, 5), 'G6': (7, 6), 'G7': (7, 7), 'G8': (7, 8), 'H1': (8, 1), 'H2': (8, 2), 'H3': (8, 3), 'H4': (8, 4), 'H5': (8, 5), 'H6': (8, 6), 'H7': (8, 7), 'H8': (8, 8)}

class game_engine():
    def __init__(self, selected_piece, starting_position, ending_position= None):
        self.selected_piece = selected_piece
        self.starting_position = starting_position
        self.ending_position = ending_position
    def legal_move(self):
        if self.selected_piece == "White Pawn":
            # print(self.selected_piece, self.ending_position, self.starting_position)
            return self.pawn_move_check(self.ending_position) == self.pawn_move_check(self.starting_position) + 1
        if self.selected_piece =="Black Pawn":
            return self.pawn_move_check((self.ending_position)) == self.pawn_move_check(self.starting_position) - 1
        if self.selected_piece == "White Rook" or self.selected_piece =="Black Rook":
            return self.rook_move_check(self.starting_position, self.ending_position)
        if self.selected_piece == "White Bishop" or self.selected_piece == "Black Bishop":
            return self.bishop_move_check(self.starting_position, self.ending_position)
        if self.selected_piece =="White Queen" or self.selected_piece =="Black Queen":
            return self.queen_move_check(self.starting_position, self.ending_position)
    def pawn_move_check(self, position):
        return position_into_tuple.get(position)[1]
    def rook_move_check(self, starting_position, ending_position):
        if position_into_tuple.get(starting_position)[0] == position_into_tuple.get(ending_position)[0] or position_into_tuple.get(starting_position)[1] == position_into_tuple.get(ending_position)[1]:
            return True
        else:
            return False
    def bishop_move_check(self, starting_position, ending_position):
        return abs(position_into_tuple.get(starting_position)[0] - position_into_tuple.get(ending_position)[0]) == abs(position_into_tuple.get(starting_position)[1] - position_into_tuple.get(ending_position)[1])
    def queen_move_check(self, starting_position, ending_position):
        if position_into_tuple.get(starting_position)[0] == position_into_tuple.get(ending_position)[0] or position_into_tuple.get(starting_position)[1] == position_into_tuple.get(ending_position)[1]:
            return True
        elif abs(position_into_tuple.get(starting_position)[0] - position_into_tuple.get(ending_position)[0]) == abs(position_into_tuple.get(starting_position)[1] - position_into_tuple.get(ending_position)[1]):
            return True
        else:
            return False







