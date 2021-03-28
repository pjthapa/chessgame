from tkinter import *

#create a list of all chess positions
list_of_white_pieces =["White Rook", "White knight", "White Bishop","White Queen","White King","White Pawn"]
list_of_black_pieces =["Black Rook", "Black knight", "Black Bishop","Black Queen","Black King","Black Pawn"]
board_coordinates = {'A1': [0, 0, 'white',"White Rook"], 'A2': [100, 0, 'green', "White Pawn"], 'A3': [200, 0, 'white', ""], 'A4': [300, 0, 'green', ""],
                     'A5': [400, 0, 'white', ""], 'A6': [500, 0, 'green', ""], 'A7': [600, 0, 'white', "Black Pawn"], 'A8': [700, 0, 'green', "Black Rook"],
                     'B8': [700, 100, 'white', "Black Knight"], 'B7': [600, 100, 'green', "Black Pawm"], 'B6': [500, 100, 'white', ""],
                     'B5': [400, 100, 'green',""], 'B4': [300, 100, 'white', ""], 'B3': [200, 100, 'green', ""],
                     'B2': [100, 100, 'white',"White Pawn"], 'B1': [0, 100, 'green',"White knight"], 'C1': [0, 200, 'white',"White Bishop"],
                     'C2': [100, 200, 'green',"White Pawn"], 'C3': [200, 200, 'white', ""], 'C4': [300, 200, 'green', ""],
                     'C5': [400, 200, 'white', ""], 'C6': [500, 200, 'green', ""], 'C7': [600, 200, 'white', "Black Pawn"],
                     'C8': [700, 200, 'green', "Black Bishop"], 'D8': [700, 300, 'white', "Black King"], 'D7': [600, 300, 'green', "Black Pawn"],
                     'D6': [500, 300, 'white', ""], 'D5': [400, 300, 'green', ""], 'D4': [300, 300, 'white', ""],
                     'D3': [200, 300, 'green', ""], 'D2': [100, 300, 'white',"White Pawn"], 'D1': [0, 300, 'green',"White King"],
                     'E1': [0, 400, 'white',"White Queen"], 'E2': [100, 400, 'green',"White Pawn"], 'E3': [200, 400, 'white', ""],
                     'E4': [300, 400, 'green', ""], 'E5': [400, 400, 'white', ""], 'E6': [500, 400, 'green', ""],
                     'E7': [600, 400, 'white', "Black Pawn"], 'E8': [700, 400, 'green', "Black Queen"], 'F8': [700, 500, 'white', "Black Bishop"],
                     'F7': [600, 500, 'green', "Black Pawn"], 'F6': [500, 500, 'white', ""], 'F5': [400, 500, 'green', ""],
                     'F4': [300, 500, 'white', ""], 'F3': [200, 500, 'green', ""], 'F2': [100, 500, 'white', "White Pawn"],
                     'F1': [0, 500, 'green',"White Bishop"], 'G1': [0, 600, 'white',"White knight"], 'G2': [100, 600, 'green',"White Pawn"],
                     'G3': [200, 600, 'white', ""], 'G4': [300, 600, 'green',""], 'G5': [400, 600, 'white', ""],
                     'G6': [500, 600, 'green', ""], 'G7': [600, 600, 'white', "Black Pawn"], 'G8': [700, 600, 'green',"Black Kinght"],
                     'H8': [700, 700, 'white',"Black Rook"], 'H7': [600, 700, 'green',"Black Pawn"], 'H6': [500, 700, 'white', ""],
                     'H5': [400, 700, 'green', ""], 'H4': [300, 700, 'white', ""], 'H3': [200, 700, 'green', ""],
                     'H2': [100, 700, 'white',"White Pawn"], 'H1': [0, 700, 'green',"White Rook"]}

if __name__ =="__main__":
    #initialize ches board
    chess_board = Tk()

    #give the program a title
    chess_board.title("Chess Board")

    #give it a background color
    chess_board.configure(background="grey")

    #create dimension of the GUI
    chess_board.geometry("800x800")


    #create the buttons

    for key in board_coordinates:
        button = Button(chess_board, text=board_coordinates.get(key)[3] , bg=board_coordinates.get(key)[2])
        button.place(x=board_coordinates.get(key)[1], y=board_coordinates.get(key)[0], height=100, width=100)
        #changing cartesian position of button in a snake manner



    chess_board.mainloop()


