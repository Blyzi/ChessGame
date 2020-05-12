

class Plateau:

    def __init__(self):
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

    def check_piece(self,go_to_position):
        n=str(go_to_position)
        i=int(n[0])-1
        p=self.plateau_coor[i].index(go_to_position)
        gotopiece=self.plateau_init[i][p]
        if gotopiece =="":
                print("pas de piece sur la case")
        else:
                print(gotopiece, "sur la case")
		
plateau = Plateau()
print(plateau.plateau_coor)
print(plateau.plateau_init)
plateau.check_piece(35)
