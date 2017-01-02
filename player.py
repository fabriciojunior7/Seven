import pygame

class P1(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 15
        self.altura = 15
        self.forca_pulo = 7
        self.queda = 0
        self.corpo = pygame.Rect(x, y, self.largura, self.largura)
        self.ad = [False, False]
        self.em_queda = True
        self.colidindo = False

    def mover(self, velocidade):
        if(self.ad[0] == True):
            self.corpo.move_ip(-velocidade, 0)
        if (self.ad[1] == True):
            self.corpo.move_ip(velocidade, 0)

    def pular(self, gravidade):
        if(self.colidindo == True):
            self.queda = -self.forca_pulo

    def cair(self, gravidade):
        self.corpo.move_ip(0, self.queda)
        self.queda += gravidade

    def colidiu(self, y):
        self.corpo.y = y - self.altura
        self.queda = 0

    def fim_tela(self, tela_x_max):
        if(self.corpo.x + self.largura > tela_x_max):
            self.corpo.x = tela_x_max - self.largura
        elif(self.corpo.x < 0):
            self.corpo.x = 0

    def desenha_player(self, tela, cor):
        pygame.draw.rect(tela, cor, self.corpo)