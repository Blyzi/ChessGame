#  piece_11.py
#  

class Piece:
    def __init__(self,piece):
        self.mvt_possible=None
        self.eat_possible=mvt_possible
        self.mvt_limit=None

class Roi(Piece):
    def __init__(self,piece):
        super().__init__(self,piece)
        self.mvt_possible=[1,10,11,-1,-10,-11,-9,9]
        self.mvt_limit=1
       
class Reine(Roi):
    def __init__(self,piece):
        super().__init__(self,piece)
        self.mvt_limit=None

class Tour(Piece):
    def __init__(self,piece):
        super().__init__(self,piece)
        self.mvt_possible=[1,10,-1,-10]

class Fou(Piece):
    def __init__(self,piece):
        super().__init__(self,piece)
        self.mvt_possible=[11,-11,-9,9]
        
class Cavalier(Piece):
    def __init__(self,piece):
        super().__init__(self,piece)
        self.mvt_possible=[-21,-19,-12,-8,21,19,12,8]

#A faire        
class Pion(Piece):
    def __init__(self,piece):
        super().__init__(self,piece)
        self.mvt_possible=[1]
    
    def color_and_place():
        pass
