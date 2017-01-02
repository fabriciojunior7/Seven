import obstaculos, itens

#Player
coordenada_player = [(385, 330)]

#Paredes
coordenadas_paredes = [(0, 55)
, (85, 55)
, (135, 105)
, (185, 155)
, (235, 205)
, (285, 255)
, (335, 305)
, (385, 355)]

#Chaves
coordenadas_chaves = [(5, 45)]


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