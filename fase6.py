import obstaculos, itens

#Player
coordenada_player = [(10, 375)]

#Paredes
coordenadas_paredes = [(0, 395), (15, 395), (81, 395)
, (162, 395), (177, 395), (192, 395), (207, 395), (222, 395)
, (0, 345), (385, 345)
, (-10, 295), (130, 295), (255, 295) ,(395, 295)
, (0, 245), (385, 245)
, (-10, 195), (395, 195)
, (0, 145), (385, 145)
, (-10, 95), (395, 95)
, (0, 45), (385, 45)
, (385, 395), (370, 395), (304, 395)]

#Chaves
coordenadas_chaves = [(198, 327)]

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