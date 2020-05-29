#  piece_11.py
#  
from tkinter import *

class Piece:
    def __init__(self, piece, coor, screen):
        self.mvt_possible = None
        self.eat_possible = self.mvt_possible
        self.mvt_limit = None
        self.coor = None
        self.img = PhotoImage(file="img/"+piece+".png")
        screen.create_image(coor[0]*75, coor[1]*75, image=self.img)

class Roi(Piece):
    def __init__(self, piece, coor, screen):
        super().__init__(piece, coor, screen)
        self.mvt_possible=[1,10,11,-1,-10,-11,-9,9]
        self.mvt_limit=1

class Reine(Roi):
    def __init__(self, piece, coor, screen):
        super().__init__(self, piece, coor, screen)
        self.mvt_limit=None

class Tour(Piece):
    def __init__(self, piece, coor, screen):
        super().__init__(piece, coor, screen)
        self.mvt_possible=[1,10,-1,-10]

class Fou(Piece):
    def __init__(self, piece, coor, screen):
        super().__init__( piece, coor, screen)
        self.mvt_possible=[11,-11,-9,9]
        
class Cavalier(Piece):
    def __init__(self, piece, coor, screen):
        super().__init__( piece, coor, screen)
        self.mvt_possible=[-21,-19,-12,-8,21,19,12,8]

class Pion(Piece):
    def __init__(self, piece, coor, screen):
        super().__init__( piece, coor, screen)
        self.mvt_possible=color_and_place(self)
        self.piece=piece
        
    def color_and_place(self):  #orientation déplacement selon la couleur
        if self.piece[1]=="N":
            mvt=10
        elif self.piece[1]=="B":
            mvt=-10
        return [mvt]

