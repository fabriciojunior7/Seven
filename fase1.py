import obstaculos, itens

#Player
coordenada_player = [(10, 365)]

#Paredes
coordenadas_paredes = [(0, 395), (15, 395), (30, 395), (45, 395), (60, 395), (75, 395), (90, 395)
, (130, 360), (145, 360), (160, 360)
, (222, 360), (237, 360), (252, 360)
, (315, 360), (330, 360), (345, 360)
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

    return(saida)