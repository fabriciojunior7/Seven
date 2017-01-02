import obstaculos, itens

#Player
coordenada_player = [(385, 0)]

#Paredes
coordenadas_paredes = [(0, 395), (15, 395)
]

#Chaves
coordenadas_chaves = [(0, 0)]

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

    return(saida)