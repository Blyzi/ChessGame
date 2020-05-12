

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

    @classmethod
    def create_plateau(cls):
        l=[]
        for i in range(len(cls.plateau_init)):
            l.append([])
            for j in range(len(cls.plateau_init)):
                l[i].append([])
        for i in range(len(cls.plateau_init)):
            for j in range(len(cls.plateau_init)):
                l[i][j].append(cls.plateau_coor[i][j])
                l[i][j].append(cls.plateau_init[i][j])
        return l

plate=Plateau.create_plateau()
print(plate)
plateau = Plateau()
print(plateau.plateau_coor)
print(plateau.plateau_init)
