import pygame

class Chave(object):
    def __init__(self, x, y):
        self.largura  = 5
        self.altura = 5
        self.x = x
        self.y = y
        self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenha_chave(self, tela, cor):
        pygame.draw.rect(tela, cor, self.corpo)