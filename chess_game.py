class game_engine():
    def __init__(self, selected_piece, starting_position, ending_position= None):
        self.selected_piece = selected_piece
        self.starting_position = starting_position
        self.ending_position = ending_position
    def legal_move(self):
        if self.selected_piece == "White Pawn":
            print(self.selected_piece, self.ending_position, self.starting_position)
            print(self.value(self.ending_position) == self.value(self.starting_position) + 1)
            return self.value(self.ending_position) == self.value(self.starting_position) + 1
    def value(self, position):
        if str(position) == "A2":
            return 1
        elif str(position) == "A3":
            return 2
        else:
            return 3
