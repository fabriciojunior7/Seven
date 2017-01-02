import pygame, sys

def fim(tentativas):
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

    # Joystick
    tem_joy = False
    if (pygame.joystick.get_count() > 0):
        tem_joy = True
        joy = pygame.joystick.Joystick(0)
        joy.init()

    pygame.font.init()
    font = pygame.font.get_default_font()
    font_pontuacao = pygame.font.SysFont(font, 80)
    font_titulo = pygame.font.SysFont(font, 45)
    mouse_inicia = False
    mouse_sair = False

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            #Mouse
            if(event.type == pygame.MOUSEBUTTONDOWN):
                return(tentativas)
            #Precionados
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE):
                    return(tentativas)
            # Joystick
            if (event.type == pygame.JOYBUTTONDOWN):
                if (joy.get_button(9) == True or joy.get_button(8) == True):
                    return (tentativas)

        #Rodar
        relogio.tick(frames)
        #Desenha
        tela.fill(preto)
        pontuacao = font_pontuacao.render("%i" % tentativas, 1, branco)
        #pontuacao = font_pontuacao.render("28", 1, branco)
        titulo = font_titulo.render("TENTATIVAS", 1, branco)
        tela.blit(titulo, (105, 120))
        tela.blit(pontuacao, (172, 190))
        pygame.display.update()