import pygame

class Parede(object):
    def __init__(self, x, y):
        self.largura = 15
        self.altura = 5
        self.corpo = pygame.Rect(x, y, self.largura, self.altura)

    def desenha_parede(self, tela, cor):
        pygame.draw.rect(tela, cor, self.corpo)