import fase1, fase2, fase3, fase4, fase5, fase6, fase7

class Fase(object):
    def __init__(self, fase):
        if(fase == 1):
            self.player = fase1.forma_fase()[0]
            self.paredes = fase1.forma_fase()[1]
            self.chaves = fase1.forma_fase()[2]
        elif(fase == 2):
            self.player = fase2.forma_fase()[0]
            self.paredes = fase2.forma_fase()[1]
            self.chaves = fase2.forma_fase()[2]
        elif(fase == 3):
            self.player = fase3.forma_fase()[0]
            self.paredes = fase3.forma_fase()[1]
            self.chaves = fase3.forma_fase()[2]
        elif(fase == 4):
            self.player = fase4.forma_fase()[0]
            self.paredes = fase4.forma_fase()[1]
            self.chaves = fase4.forma_fase()[2]
        elif(fase == 5):
            self.player = fase5.forma_fase()[0]
            self.paredes = fase5.forma_fase()[1]
            self.chaves = fase5.forma_fase()[2]
        elif(fase == 6):
            self.player = fase6.forma_fase()[0]
            self.paredes = fase6.forma_fase()[1]
            self.chaves = fase6.forma_fase()[2]
        elif(fase == 7):
            self.player = fase7.forma_fase()[0]
            self.paredes = fase7.forma_fase()[1]
            self.chaves = fase7 .forma_fase()[2]
