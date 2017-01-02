import pygame, sys

def menu(pontuacoes):

    pygame.init()
    pygame.joystick.init()
    largura = 400
    altura = 400
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Seven - Inicio")
    relogio = pygame.time.Clock()
    frames = 60

    #Cores
    branco = (255, 255, 255)
    verde = (0, 255, 0)
    vermelho = (255, 0, 0)
    azul = (0, 0, 255)
    preto = (0, 0, 0)

    #Joystick
    tem_joy = False
    if(pygame.joystick.get_count() > 0):
        tem_joy = True
        joy = pygame.joystick.Joystick(0)
        joy.init()

    #Superficies
    quadro_inicio = pygame.Surface((110, 30))
    quadro_sair = pygame.Surface((45, 15))

    #Fontes
    pygame.font.init()
    font = pygame.font.get_default_font()
    font_inicio = pygame.font.SysFont(font, 45)
    font_sair = pygame.font.SysFont(font, 25)
    font_titulo = pygame.font.SysFont(font, 20)
    font_pontuacao = pygame.font.SysFont(font, 15)
    font_desenvolvedor = pygame.font.SysFont(font, 13)
    font_data = pygame.font.SysFont(font, 13)
    mouse_inicia = False
    mouse_sair = False

    #Tabela
    posicoes = []
    for i in range(len(pontuacoes)):
        posicoes.append(i)

    while(len(pontuacoes) > 20):
        pontuacoes.pop(0)
        posicoes.pop(0)

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            #Mouse
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(pygame.mouse.get_pressed()[0] == True and mouse_inicia == True):
                    return(0)
                elif (pygame.mouse.get_pressed()[0] == True and mouse_sair == True):
                    pygame.quit()
                    sys.exit()
            #Precionados
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                    return(0)
            #Joystick
            if(event.type == pygame.JOYBUTTONDOWN):
                if(joy.get_button(9) == True or joy.get_button(8) == True):
                    return(0)

        #Checar
        if((pygame.mouse.get_pos()[0] > 145 and pygame.mouse.get_pos()[0] < 255) and (pygame.mouse.get_pos()[1] > 185 and pygame.mouse.get_pos()[1] < 215)):
            mouse_inicia = True
        else:
            mouse_inicia = False

        if ((pygame.mouse.get_pos()[0] > 177 and pygame.mouse.get_pos()[0] < 222) and (pygame.mouse.get_pos()[1] > 300 and pygame.mouse.get_pos()[1] < 315)):
            mouse_sair = True
        else:
            mouse_sair = False

        #Rodar
        relogio.tick(frames)
        #Desenha
        tela.fill(preto)
        quadro_inicio.fill(branco)
        quadro_sair.fill(branco)
        inicio = font_inicio.render("START", 1, preto)
        sair = font_sair.render("SAIR", 1, preto)
        titulo = font_titulo.render("Ultimas", 1, branco)
        titulo2 = font_titulo.render("Partidas", 1, branco)
        desenvolvedor = font_desenvolvedor.render("- Fabricio Junior -", 1, branco)
        data = font_data.render("2016", 1, branco)
        coordenadas_pontuacao = []
        coordenada1 = (16, 35)
        i = 0
        for p in pontuacoes:
            i += 1
            coordenadas_pontuacao.append((coordenada1[0], coordenada1[1] + (i*17)))
        ii = 0
        for p in pontuacoes:
            pontuacao = font_pontuacao.render("%i - ( %i )" % ((posicoes[ii]+1), p), 1, branco)
            tela.blit(pontuacao, coordenadas_pontuacao[i-1])
            i -= 1
            ii += 1
        if(len(pontuacoes) > 0):
            tela.blit(titulo, (13, 5))
            tela.blit(titulo2, (10, 20))
        tela.blit(quadro_inicio, (145, 185))
        tela.blit(quadro_sair, (177, 300))
        tela.blit(inicio, (150, 188))
        tela.blit(sair, (179, 300))
        tela.blit(desenvolvedor, (322, 380))
        tela.blit(data, (352, 391))
        pygame.display.update()
