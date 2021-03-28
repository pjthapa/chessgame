from tkinter import *

#create a list of all chess positions
list_of_chess_position= ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B8', 'B7', 'B6', 'B5', 'B4', 'B3', 'B2', 'B1', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D8', 'D7', 'D6', 'D5', 'D4', 'D3', 'D2', 'D1', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'F8', 'F7', 'F6', 'F5', 'F4', 'F3', 'F2', 'F1', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H8', 'H7', 'H6', 'H5', 'H4', 'H3', 'H2', 'H1']
list_of_pieces =["Rook", "knight", "Bishop","Queen","King","Pawn"]
#function to generate color:
last_color = "green"
def color_decider():
    global last_color
    if last_color == "green":
        last_color = "white"
        return last_color
    else:
        last_color = "green"
        return last_color

if __name__ =="__main__":
    #initialize ches board
    chess_board = Tk()

    #give the program a title
    chess_board.title("Chess Board")

    #give it a background color
    chess_board.configure(background="grey")

    #create dimension of the GUI
    chess_board.geometry("800x800")

    #create the position variables for each button
    x_position = 0
    y_position = 0
    y_increase = 100
    y_change_count = 0

    #create the buttons
    for position in list_of_chess_position:
        color = color_decider()
        print(position)
        button = Button(chess_board, text=position, bg=color)
        button.place(x=x_position, y=y_position, height=100, width=100)
        # print([position, y_position, y_change_count, x_position, y_increase])
        #changing cartesian position of button in a snake manner
        y_position += y_increase
        y_change_count += 1
        if y_change_count == 8:
            y_position -= y_increase
            x_position += 100
            y_change_count = 0
            y_increase = -y_increase


    chess_board.mainloop()


