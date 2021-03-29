from tkinter import *

#create a list of all chess positions position as key and coordinates, background color and initial piece as vlaue
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
selection = ""
first_selected_button = None
first_selected_button = ""


if __name__ =="__main__":
    #initialize ches board
    chess_board = Tk()

    #give the program a title
    chess_board.title("Chess Board")

    #give it a background color
    chess_board.configure(background="grey")

    #create dimension of the GUI
    chess_board.geometry("800x800")


    def click(button, button_str, piece):
        global selection
        global first_selected_button
        global first_selected_button_string

        #check if click is on empty space or not
        if selection == "" and piece != "":

            #update selected piece
            selection = piece
            # print("selected"+ selection)

            #save the selected position and associated variable
            first_selected_button = button
            first_selected_button_string = button_str
            # print(board_coordinates[button_str][3])
        else:
            #update button text and dictionary to selected
            button['text'] = str(selection)
            board_coordinates[button_str][3] = str(selection)

            #update old button and dictionary to nothing
            board_coordinates[first_selected_button_string][3] = ""
            first_selected_button['text'] = ""

            #reset selection and first click
            selection = ""
            first_selected_button = None


    #create the buttons
    A1 = Button(chess_board, text=board_coordinates.get('A1')[3], bg=board_coordinates.get('A1')[2],command = lambda: click(A1, 'A1', board_coordinates.get('A1')[3]))
    A1.place(x=board_coordinates.get('A1')[1], y=board_coordinates.get('A1')[0], height=100, width=100)
    A2 = Button(chess_board, text=board_coordinates.get('A2')[3], bg=board_coordinates.get('A2')[2],command = lambda: click(A2, 'A2', board_coordinates.get('A2')[3]))
    A2.place(x=board_coordinates.get('A2')[1], y=board_coordinates.get('A2')[0], height=100, width=100)
    A3 = Button(chess_board, text=board_coordinates.get('A3')[3], bg=board_coordinates.get('A3')[2],command = lambda: click(A3, 'A3', board_coordinates.get('A3')[3]))
    A3.place(x=board_coordinates.get('A3')[1], y=board_coordinates.get('A3')[0], height=100, width=100)
    A4 = Button(chess_board, text=board_coordinates.get('A4')[3], bg=board_coordinates.get('A4')[2],command = lambda: click(A4, 'A4', board_coordinates.get('A4')[3]))
    A4.place(x=board_coordinates.get('A4')[1], y=board_coordinates.get('A4')[0], height=100, width=100)
    A5 = Button(chess_board, text=board_coordinates.get('A5')[3], bg=board_coordinates.get('A5')[2],command = lambda: click(A5, 'A5', board_coordinates.get('A5')[3]))
    A5.place(x=board_coordinates.get('A5')[1], y=board_coordinates.get('A5')[0], height=100, width=100)
    A6 = Button(chess_board, text=board_coordinates.get('A6')[3], bg=board_coordinates.get('A6')[2],
                command = lambda: click(A6, 'A6', board_coordinates.get('A6')[3]))
    A6.place(x=board_coordinates.get('A6')[1], y=board_coordinates.get('A6')[0], height=100, width=100)
    A7 = Button(chess_board, text=board_coordinates.get('A7')[3], bg=board_coordinates.get('A7')[2],
                command = lambda: click(A7, 'A7', board_coordinates.get('A7')[3]))
    A7.place(x=board_coordinates.get('A7')[1], y=board_coordinates.get('A7')[0], height=100, width=100)
    A8 = Button(chess_board, text=board_coordinates.get('A8')[3], bg=board_coordinates.get('A8')[2]
                ,command = lambda: click(A8, 'A8', board_coordinates.get('A8')[3]))
    A8.place(x=board_coordinates.get('A8')[1], y=board_coordinates.get('A8')[0], height=100, width=100)
    B8 = Button(chess_board, text=board_coordinates.get('B8')[3], bg=board_coordinates.get('B8')[2]
                ,command = lambda: click(B8, 'B8', board_coordinates.get('B8')[3]))
    B8.place(x=board_coordinates.get('B8')[1], y=board_coordinates.get('B8')[0], height=100, width=100)
    B7 = Button(chess_board, text=board_coordinates.get('B7')[3], bg=board_coordinates.get('B7')[2]
                ,command = lambda: click(B7, 'B7', board_coordinates.get('B7')[3]))
    B7.place(x=board_coordinates.get('B7')[1], y=board_coordinates.get('B7')[0], height=100, width=100)
    B6 = Button(chess_board, text=board_coordinates.get('B6')[3], bg=board_coordinates.get('B6')[2]
                ,command = lambda: click(B6, 'B6', board_coordinates.get('B6')[3]))
    B6.place(x=board_coordinates.get('B6')[1], y=board_coordinates.get('B6')[0], height=100, width=100)
    B5 = Button(chess_board, text=board_coordinates.get('B5')[3], bg=board_coordinates.get('B5')[2]
                ,command = lambda: click(B5, 'B5', board_coordinates.get('B5')[3]))
    B5.place(x=board_coordinates.get('B5')[1], y=board_coordinates.get('B5')[0], height=100, width=100)
    B4 = Button(chess_board, text=board_coordinates.get('B4')[3], bg=board_coordinates.get('B4')[2]
                ,command = lambda: click(B4, 'B4', board_coordinates.get('B4')[3]))
    B4.place(x=board_coordinates.get('B4')[1], y=board_coordinates.get('B4')[0], height=100, width=100)
    B3 = Button(chess_board, text=board_coordinates.get('B3')[3], bg=board_coordinates.get('B3')[2]
                ,command = lambda: click(B3, 'B3', board_coordinates.get('B3')[3]))
    B3.place(x=board_coordinates.get('B3')[1], y=board_coordinates.get('B3')[0], height=100, width=100)
    B2 = Button(chess_board, text=board_coordinates.get('B2')[3], bg=board_coordinates.get('B2')[2]
                ,command = lambda: click(B2, 'B2', board_coordinates.get('B2')[3]))
    B2.place(x=board_coordinates.get('B2')[1], y=board_coordinates.get('B2')[0], height=100, width=100)
    B1 = Button(chess_board, text=board_coordinates.get('B1')[3], bg=board_coordinates.get('B1')[2]
                ,command = lambda: click(B1, 'B1', board_coordinates.get('B1')[3]))
    B1.place(x=board_coordinates.get('B1')[1], y=board_coordinates.get('B1')[0], height=100, width=100)
    C1 = Button(chess_board, text=board_coordinates.get('C1')[3], bg=board_coordinates.get('C1')[2],
                command = lambda: click(C1, 'C1', board_coordinates.get('C1')[3]))
    C1.place(x=board_coordinates.get('C1')[1], y=board_coordinates.get('C1')[0], height=100, width=100)
    C2 = Button(chess_board, text=board_coordinates.get('C2')[3], bg=board_coordinates.get('C2')[2],
                command = lambda: click(C2, 'C2', board_coordinates.get('C2')[3]))
    C2.place(x=board_coordinates.get('C2')[1], y=board_coordinates.get('C2')[0], height=100, width=100)
    C3 = Button(chess_board, text=board_coordinates.get('C3')[3], bg=board_coordinates.get('C3')[2],
                command = lambda: click(C3, 'C3', board_coordinates.get('C3')[3]))
    C3.place(x=board_coordinates.get('C3')[1], y=board_coordinates.get('C3')[0], height=100, width=100)
    C4 = Button(chess_board, text=board_coordinates.get('C4')[3], bg=board_coordinates.get('C4')[2],
                command = lambda: click(C4, 'C4', board_coordinates.get('C4')[3]))
    C4.place(x=board_coordinates.get('C4')[1], y=board_coordinates.get('C4')[0], height=100, width=100)
    C5 = Button(chess_board, text=board_coordinates.get('C5')[3], bg=board_coordinates.get('C5')[2],
                command = lambda: click(C5, 'C5', board_coordinates.get('C5')[3]))
    C5.place(x=board_coordinates.get('C5')[1], y=board_coordinates.get('C5')[0], height=100, width=100)
    C6 = Button(chess_board, text=board_coordinates.get('C6')[3], bg=board_coordinates.get('C6')[2],
                command = lambda: click(C6, 'C6', board_coordinates.get('C6')[3]))
    C6.place(x=board_coordinates.get('C6')[1], y=board_coordinates.get('C6')[0], height=100, width=100)
    C7 = Button(chess_board, text=board_coordinates.get('C7')[3], bg=board_coordinates.get('C7')[2],
                command = lambda: click(C7, 'C7', board_coordinates.get('C7')[3]))
    C7.place(x=board_coordinates.get('C7')[1], y=board_coordinates.get('C7')[0], height=100, width=100)
    C8 = Button(chess_board, text=board_coordinates.get('C8')[3], bg=board_coordinates.get('C8')[2],
                command = lambda: click(C8, 'C8', board_coordinates.get('C8')[3]))
    C8.place(x=board_coordinates.get('C8')[1], y=board_coordinates.get('C8')[0], height=100, width=100)
    D8 = Button(chess_board, text=board_coordinates.get('D8')[3], bg=board_coordinates.get('D8')[2],
                command = lambda: click(D8, 'D8', board_coordinates.get('D8')[3]))
    D8.place(x=board_coordinates.get('D8')[1], y=board_coordinates.get('D8')[0], height=100, width=100)
    D7 = Button(chess_board, text=board_coordinates.get('D7')[3], bg=board_coordinates.get('D7')[2],
                command = lambda: click(D7, 'D7', board_coordinates.get('D7')[3]))
    D7.place(x=board_coordinates.get('D7')[1], y=board_coordinates.get('D7')[0], height=100, width=100)
    D6 = Button(chess_board, text=board_coordinates.get('D6')[3], bg=board_coordinates.get('D6')[2],
                command = lambda: click(D6, 'D6', board_coordinates.get('D6')[3]))
    D6.place(x=board_coordinates.get('D6')[1], y=board_coordinates.get('D6')[0], height=100, width=100)
    D5 = Button(chess_board, text=board_coordinates.get('D5')[3], bg=board_coordinates.get('D5')[2],
                command = lambda: click(D5, 'D5', board_coordinates.get('D5')[3]))
    D5.place(x=board_coordinates.get('D5')[1], y=board_coordinates.get('D5')[0], height=100, width=100)
    D4 = Button(chess_board, text=board_coordinates.get('D4')[3], bg=board_coordinates.get('D4')[2],
                command = lambda: click(D4, 'D4', board_coordinates.get('D4')[3]))
    D4.place(x=board_coordinates.get('D4')[1], y=board_coordinates.get('D4')[0], height=100, width=100)
    D3 = Button(chess_board, text=board_coordinates.get('D3')[3], bg=board_coordinates.get('D3')[2],
                command = lambda: click(D3, 'D3', board_coordinates.get('D3')[3]))
    D3.place(x=board_coordinates.get('D3')[1], y=board_coordinates.get('D3')[0], height=100, width=100)
    D2 = Button(chess_board, text=board_coordinates.get('D2')[3], bg=board_coordinates.get('D2')[2],
                command = lambda: click(D2, 'D2', board_coordinates.get('D2')[3]))
    D2.place(x=board_coordinates.get('D2')[1], y=board_coordinates.get('D2')[0], height=100, width=100)
    D1 = Button(chess_board, text=board_coordinates.get('D1')[3], bg=board_coordinates.get('D1')[2],
                command = lambda: click(D1, 'D1', board_coordinates.get('D1')[3]))
    D1.place(x=board_coordinates.get('D1')[1], y=board_coordinates.get('D1')[0], height=100, width=100)
    E1 = Button(chess_board, text=board_coordinates.get('E1')[3], bg=board_coordinates.get('E1')[2],
                command = lambda: click(E1, 'E1', board_coordinates.get('E1')[3]))
    E1.place(x=board_coordinates.get('E1')[1], y=board_coordinates.get('E1')[0], height=100, width=100)
    E2 = Button(chess_board, text=board_coordinates.get('E2')[3], bg=board_coordinates.get('E2')[2],
                command = lambda: click(E2, 'E2', board_coordinates.get('E2')[3]))
    E2.place(x=board_coordinates.get('E2')[1], y=board_coordinates.get('E2')[0], height=100, width=100)
    E3 = Button(chess_board, text=board_coordinates.get('E3')[3], bg=board_coordinates.get('E3')[2],
                command = lambda: click(E3, 'E3', board_coordinates.get('E3')[3]))
    E3.place(x=board_coordinates.get('E3')[1], y=board_coordinates.get('E3')[0], height=100, width=100)
    E4 = Button(chess_board, text=board_coordinates.get('E4')[3], bg=board_coordinates.get('E4')[2],
                command = lambda: click(E4, 'E4', board_coordinates.get('E4')[3]))
    E4.place(x=board_coordinates.get('E4')[1], y=board_coordinates.get('E4')[0], height=100, width=100)
    E5 = Button(chess_board, text=board_coordinates.get('E5')[3], bg=board_coordinates.get('E5')[2],
                command = lambda: click(E5, 'E5', board_coordinates.get('E5')[3]))
    E5.place(x=board_coordinates.get('E5')[1], y=board_coordinates.get('E5')[0], height=100, width=100)
    E6 = Button(chess_board, text=board_coordinates.get('E6')[3], bg=board_coordinates.get('E6')[2],
                command = lambda: click(E6, 'E6', board_coordinates.get('E6')[3]))
    E6.place(x=board_coordinates.get('E6')[1], y=board_coordinates.get('E6')[0], height=100, width=100)
    E7 = Button(chess_board, text=board_coordinates.get('E7')[3], bg=board_coordinates.get('E7')[2],
                command = lambda: click(E7, 'E7', board_coordinates.get('E7')[3]))
    E7.place(x=board_coordinates.get('E7')[1], y=board_coordinates.get('E7')[0], height=100, width=100)
    E8 = Button(chess_board, text=board_coordinates.get('E8')[3], bg=board_coordinates.get('E8')[2],
                command = lambda: click(E8, 'E8', board_coordinates.get('E8')[3]))
    E8.place(x=board_coordinates.get('E8')[1], y=board_coordinates.get('E8')[0], height=100, width=100)
    F8 = Button(chess_board, text=board_coordinates.get('F8')[3], bg=board_coordinates.get('F8')[2],
                command = lambda: click(F8, 'F8', board_coordinates.get('F8')[3]))
    F8.place(x=board_coordinates.get('F8')[1], y=board_coordinates.get('F8')[0], height=100, width=100)
    F7 = Button(chess_board, text=board_coordinates.get('F7')[3], bg=board_coordinates.get('F7')[2],
                command = lambda: click(F7, 'F7', board_coordinates.get('F7')[3]))
    F7.place(x=board_coordinates.get('F7')[1], y=board_coordinates.get('F7')[0], height=100, width=100)
    F6 = Button(chess_board, text=board_coordinates.get('F6')[3], bg=board_coordinates.get('F6')[2],
                command = lambda: click(F6, 'F6', board_coordinates.get('F6')[3]))
    F6.place(x=board_coordinates.get('F6')[1], y=board_coordinates.get('F6')[0], height=100, width=100)
    F5 = Button(chess_board, text=board_coordinates.get('F5')[3], bg=board_coordinates.get('F5')[2],
                command = lambda: click(F5, 'F5', board_coordinates.get('F5')[3]))
    F5.place(x=board_coordinates.get('F5')[1], y=board_coordinates.get('F5')[0], height=100, width=100)
    F4 = Button(chess_board, text=board_coordinates.get('F4')[3], bg=board_coordinates.get('F4')[2],
                command = lambda: click(F4, 'F4', board_coordinates.get('F4')[3]))
    F4.place(x=board_coordinates.get('F4')[1], y=board_coordinates.get('F4')[0], height=100, width=100)
    F3 = Button(chess_board, text=board_coordinates.get('F3')[3], bg=board_coordinates.get('F3')[2],
                command = lambda: click(F3, 'F3', board_coordinates.get('F3')[3]))
    F3.place(x=board_coordinates.get('F3')[1], y=board_coordinates.get('F3')[0], height=100, width=100)
    F2 = Button(chess_board, text=board_coordinates.get('F2')[3], bg=board_coordinates.get('F2')[2],
                command = lambda: click(F2, 'F2', board_coordinates.get('F2')[3]))
    F2.place(x=board_coordinates.get('F2')[1], y=board_coordinates.get('F2')[0], height=100, width=100)
    F1 = Button(chess_board, text=board_coordinates.get('F1')[3], bg=board_coordinates.get('F1')[2],
                command = lambda: click(F1, 'F1', board_coordinates.get('F1')[3]))
    F1.place(x=board_coordinates.get('F1')[1], y=board_coordinates.get('F1')[0], height=100, width=100)
    G1 = Button(chess_board, text=board_coordinates.get('G1')[3], bg=board_coordinates.get('G1')[2],
                command = lambda: click(G1, 'G1', board_coordinates.get('G1')[3]))
    G1.place(x=board_coordinates.get('G1')[1], y=board_coordinates.get('G1')[0], height=100, width=100)
    G2 = Button(chess_board, text=board_coordinates.get('G2')[3], bg=board_coordinates.get('G2')[2],
                command = lambda: click(G2, 'G2', board_coordinates.get('G2')[3]))
    G2.place(x=board_coordinates.get('G2')[1], y=board_coordinates.get('G2')[0], height=100, width=100)
    G3 = Button(chess_board, text=board_coordinates.get('G3')[3], bg=board_coordinates.get('G3')[2],
                command = lambda: click(G3, 'G3', board_coordinates.get('G3')[3]))
    G3.place(x=board_coordinates.get('G3')[1], y=board_coordinates.get('G3')[0], height=100, width=100)
    G4 = Button(chess_board, text=board_coordinates.get('G4')[3], bg=board_coordinates.get('G4')[2],
                command = lambda: click(G4, 'G4', board_coordinates.get('G4')[3]))
    G4.place(x=board_coordinates.get('G4')[1], y=board_coordinates.get('G4')[0], height=100, width=100)
    G5 = Button(chess_board, text=board_coordinates.get('G5')[3], bg=board_coordinates.get('G5')[2],
                command = lambda: click(G5, 'G5', board_coordinates.get('G5')[3]))
    G5.place(x=board_coordinates.get('G5')[1], y=board_coordinates.get('G5')[0], height=100, width=100)
    G6 = Button(chess_board, text=board_coordinates.get('G6')[3], bg=board_coordinates.get('G6')[2],
                command = lambda: click(G6, 'G6', board_coordinates.get('G6')[3]))
    G6.place(x=board_coordinates.get('G6')[1], y=board_coordinates.get('G6')[0], height=100, width=100)
    G7 = Button(chess_board, text=board_coordinates.get('G7')[3], bg=board_coordinates.get('G7')[2],
                command = lambda: click(G7, 'G7', board_coordinates.get('G7')[3]))
    G7.place(x=board_coordinates.get('G7')[1], y=board_coordinates.get('G7')[0], height=100, width=100)
    G8 = Button(chess_board, text=board_coordinates.get('G8')[3], bg=board_coordinates.get('G8')[2],
                command = lambda: click(G8, 'G8', board_coordinates.get('G8')[3]))
    G8.place(x=board_coordinates.get('G8')[1], y=board_coordinates.get('G8')[0], height=100, width=100)
    H8 = Button(chess_board, text=board_coordinates.get('H8')[3], bg=board_coordinates.get('H8')[2],
                command = lambda: click(H8, 'H8', board_coordinates.get('H8')[3]))
    H8.place(x=board_coordinates.get('H8')[1], y=board_coordinates.get('H8')[0], height=100, width=100)
    H7 = Button(chess_board, text=board_coordinates.get('H7')[3], bg=board_coordinates.get('H7')[2],
                command = lambda: click(H7, 'H7', board_coordinates.get('H7')[3]))
    H7.place(x=board_coordinates.get('H7')[1], y=board_coordinates.get('H7')[0], height=100, width=100)
    H6 = Button(chess_board, text=board_coordinates.get('H6')[3], bg=board_coordinates.get('H6')[2],
                command = lambda: click(H6, 'H6', board_coordinates.get('H6')[3]))
    H6.place(x=board_coordinates.get('H6')[1], y=board_coordinates.get('H6')[0], height=100, width=100)
    H5 = Button(chess_board, text=board_coordinates.get('H5')[3], bg=board_coordinates.get('H5')[2],
                command = lambda: click(H5, 'H5', board_coordinates.get('H5')[3]))
    H5.place(x=board_coordinates.get('H5')[1], y=board_coordinates.get('H5')[0], height=100, width=100)
    H4 = Button(chess_board, text=board_coordinates.get('H4')[3], bg=board_coordinates.get('H4')[2],
                command = lambda: click(H4, 'H4', board_coordinates.get('H4')[3]))
    H4.place(x=board_coordinates.get('H4')[1], y=board_coordinates.get('H4')[0], height=100, width=100)
    H3 = Button(chess_board, text=board_coordinates.get('H3')[3], bg=board_coordinates.get('H3')[2],
                command = lambda: click(H3, 'H3', board_coordinates.get('H3')[3]))
    H3.place(x=board_coordinates.get('H3')[1], y=board_coordinates.get('H3')[0], height=100, width=100)
    H2 = Button(chess_board, text=board_coordinates.get('H2')[3], bg=board_coordinates.get('H2')[2],
                command = lambda: click(H2, 'H2', board_coordinates.get('H2')[3]))
    H2.place(x=board_coordinates.get('H2')[1], y=board_coordinates.get('H2')[0], height=100, width=100)
    H1 = Button(chess_board, text=board_coordinates.get('H1')[3], bg=board_coordinates.get('H1')[2],
                command = lambda: click(H1, 'H1', board_coordinates.get('H1')[3]))
    H1.place(x=board_coordinates.get('H1')[1], y=board_coordinates.get('H1')[0], height=100, width=100)

    chess_board.mainloop()


