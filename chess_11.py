from tkinter import *
import piece_11

class Plateau:

    def __init__(self):
        self.player_turn = "White"
        self.plateau_coor = [list(range(11, 19)), list(range(21, 29)), list(range(31, 39)), list(range(41, 49)),
                        list(range(51, 59)), list(range(61, 69)), list(range(71, 79)), list(range(81, 89))]

        self.plateau_init = [
                        ["TN1", "CN1", "FN1", "EN1", "RN1", "FN2", "CN2", "TN2"],
                        ["PN1", "PN2", "PN3", "PN4", "PN5", "PN6", "PN7", "PN8"],
                        ["", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", ""],
                        ["PB1", "PB2", "PB3", "PB4", "PB5", "PB6", "PB7", "PB8"],
                        ["TB1", "CB1", "FB1", "RB1", "EB1", "FB2", "CB2", "TB2"]
                        ]
        self.piece_eaten:[[B],[N]]

    def find_coord_of_piece(self, selected_piece):
        if not (selected_piece == ""):
            for i in self.plateau_init:
                for j in i:
                    if selected_piece == j:
                        a = i.index(j)
                        b = self.plateau_init.index(i)
            coord = self.plateau_coor[b][a]
            return [selected_piece, coord]

    def two_case_pion_mvt(self,selected_piece): #test
        coord=self.find_coord_of_piece( selected_piece)
        two=False
        color=selected_piece[1]
        if color=="N":
            for i in range (21,29):
                if i==coord:
                    two=True
        if color=="B":
            for i in range (71,79):
                if i==coord:
                    two=True
        if two:
            a=piece_11.Pion(selected_piece)#test
            a.mvt=[1,2]#test

    def check_piece(self, go_to_position):  #vérifie si une piece se trouve dans la case de destination
        n = str(go_to_position)
        i = int(n[0]) - 1
        p = self.plateau_coor[i].index(go_to_position)
        gotopiece = self.plateau_init[i][p]
        if gotopiece == "":
            return [False, ""]
        else:
            return [True, gotopiece]

    def check_eat_possibility(self, go_to_position, piece_to_move):
        if self.check_piece(go_to_position)[0]:
            color1 = piece_to_move[1]
            color2 = self.check_piece(go_to_position)[1][1]
            if color1 == color2:
                eat_possibility = False
            else:
                eat_possibility = True
        else:
            eat_possibility = False
        return eat_possibility

    def eat_piece(self, go_to_position,piece_to_move):
        if self.check_piece(go_to_position)[0] and self.check_eat_possibility(go_to_position,piece_to_move):
            pass
        else:
            print("Erreur, pas de piece à manger")

    def move_piece(self, list_to_move):
        piece = list_to_move[0]
        go_to_position = list_to_move[1]

    def display(self):
        
        fen = Tk()
        
        self.screen = Canvas(fen, width=1000, height=600, bg="#efefef")
        self.screen.grid(row=0, column=0)

        for i in range(1, 9):
            for j in range(1,9, 2):
                if(i%2 == 0):
                    self.screen.create_rectangle((i-1)*75, (j-1)*75, i*75, j*75, fill="gray", outline="black")
                    self.screen.create_rectangle((i - 1) * 75, (j - 1) * 75 + 75, i * 75, j * 75 + 75, fill="white", outline="black")
                else:
                    self.screen.create_rectangle((i - 1) * 75, (j - 1) * 75, i * 75, j * 75, fill="white", outline="black")
                    self.screen.create_rectangle((i-1)*75, (j-1)*75+75, i*75, j*75+75, fill="gray", outline="black")

        self.screen.create_rectangle(700, 0, 1000, 600, fill="#83A38C")


        self.player_turn = StringVar()
        self.player_turn.set("Turn : White")

        turn = Label(fen, textvariable=self.player_turn, bg="#83A38C")
        self.screen.create_window(850, 50, window=turn)

        fen.minsize(1000, 600)

        fen.title("Chess Game")


        fen.mainloop()

plateau = Plateau()
print(plateau.find_coord_of_piece(""))
plateau.display()

