import obstaculos, itens

#Player
coordenada_player = [(0, 45)]

#Paredes
coordenadas_paredes = [(0, 75)
, (100, 145)
, (200, 215)
, (300, 285)
, (385, 355)]

#Chaves
coordenadas_chaves = [(390, 345)]


def forma_fase():
    paredes = []
    chaves = []

    saida = []

    saida.append(coordenada_player)

    for coordenadas in coordenadas_paredes:
        paredes.append(obstaculos.Parede(coordenadas[0], coordenadas[1]))
    saida.append(paredes)

    for coordenadas in coordenadas_chaves:
        chaves.append((itens.Chave(coordenadas[0], coordenadas[1])))
    saida.append(chaves)

    return (saida)