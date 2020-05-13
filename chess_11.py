from tkinter import *

class Plateau:

    def __init__(self):
        self.player_turn = "White"
        self.plateau_coor = [list(range(10, 18)), list(range(20, 28)), list(range(30, 38)), list(range(40, 48)),
                        list(range(50, 58)), list(range(60, 68)), list(range(70, 78)), list(range(80, 88))]

        self.plateau_init = [
                        ["TN1", "CN1", "FN1", "EN1", "RN1", "FN2", "CN2", "TR2"],
                        ["PN1", "PN2", "PN3", "PN4", "PN5", "PN6", "PN7", "PN8"],
                        ["", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", ""],
                        ["PB1", "PB2", "PB3", "PB4", "PB5", "PB6", "PB7", "PB8"],
                        ["TB1", "CB1", "FB1", "RB1", "EB1", "FB2", "CB2", "TB2"]
                        ]




    def display(self):

        fen = Tk()

        plateau = Canvas(fen, width=696, height=696, bg="white")
        plateau.grid(row=1, column=0, padx=50)

        for i in range(1, 9):
            for j in range(1,9, 2):
                if(i%2 == 0):
                    print((i-1)*87, (j-1)*87, i*87, j*87)
                    plateau.create_rectangle((i-1)*87, (j-1)*87, i*87, j*87, fill="gray")

                    #plateau.create_rectangle(, fill="white")
                else:
                    plateau.create_rectangle((i-1)*87, (j-1)*87+87, i*87, j*87+87, fill="gray")

                    #plateau.create_rectangle(, fill="white")
                    #plateau.create_rectangle(, fill="gray")

        menu = Canvas(fen, bg="white", width=484, height=720)
        menu.grid(row=0, column=1, rowspan=3)


        fen.minsize(1280, 720)
        fen.maxsize(1280,720)

        fen.title("Chess Game")

        fen.configure(bg="#efefef")

        #for i in range(0, 20):
         #   fen.grid_columnconfigure(i, weight=1)
          #  fen.grid_rowconfigure(i, weight=1)

        fen.mainloop()


plateau = Plateau()
plateau.display()
