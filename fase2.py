import obstaculos, itens

#Player
coordenada_player = [(10, 150)]

#Paredes
coordenadas_paredes = [(0, 200), (15, 200), (30, 200)
, (100, 200)
, (170, 200) ,(185, 200), (200, 200)
, (270, 200)
, (340, 200), (355, 200), (370, 200)
, (385, 395)]

#Chaves
coordenadas_chaves = [(390, 385)]


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