
import piece_11

#class
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

    def find_coord_of_piece(self,selected_piece):
        if not (selected_piece==""):
            for i in self.plateau_init:
                for j in i:
                    if selected_piece==j:
                        a=i.index(j)
                        b=self.plateau_init.index(i)
            coord=self.plateau_coor[b][a]
            return [selected_piece,coord]

    def check_piece(self,go_to_position):
        n=str(go_to_position)
        i=int(n[0])-1
        p=self.plateau_coor[i].index(go_to_position)
        gotopiece=self.plateau_init[i][p]
        if gotopiece =="":
                return [False,""]
        else:
                return [True,gotopiece]

    def check_eat_possibility(self,go_to_position,piece_to_move):
        if self.check_piece(go_to_position)[0]:
                color1=piece_to_move[1]
                color2=self.check_piece(go_to_position)[1][1]
                if color1 ==color2:
                    eat_possibility=False
                else:
                    eat_possibility=True
        else:
            eat_possibility=False
        return eat_possibility

    def eat_piece(self,go_to_position):
        if self.check_piece(go_to_position)[0]:
            pass
 
    def move_piece(self,list_to_move):
        piece=list_to_move[0]
        go_to_position=list_to_move[1]
        
        
    
plateau = Plateau()
print(plateau.find_coord_of_piece(""))


