import obstaculos, itens

#Player
coordenada_player = [(192, 375)]

#Paredes
coordenadas_paredes = [(192, 395)
, (142, 345), (242, 345)
, (192, 295)
, (142, 245), (242, 245)
, ((192, 195))
, (142, 145), (242, 145)
, (192, 95)
, (142, 45), (242, 45)]

#Chaves
coordenadas_chaves = [(198, 25)]

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