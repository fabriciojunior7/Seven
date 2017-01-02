import pygame, sys
import player, obstaculos, fases, itens, menu, fim

global level_atual
level_atual = 0
pontuacoes = []

def main():
    #Globais
    pygame.init()
    pygame.joystick.init()
    largura = 400
    altura = 400
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Seven - %i" % level_atual)
    relogio = pygame.time.Clock()
    frames = 60
    gravidade = 0.5
    global tentativas
    tentativas = 0

    #Textos
    pygame.font.init()
    font = pygame.font.get_default_font()
    font_status = pygame.font.SysFont(font, 20)

    #Joysticks
    tem_joy = False
    if(pygame.joystick.get_count() > 0):
        tem_joy = True
        joy = pygame.joystick.Joystick(0)
        joy.init()

    #Cores
    branco = (255, 255, 255)
    verde = (0 , 255, 0)
    vermelho = (255, 0, 0)
    azul = (0, 0, 255)
    preto = (0, 0, 0)
    amarelo = (255, 255, 0)

    def tela_atual(level):

        if(level_atual == 0):
            menu.menu(pontuacoes)
            global level_atual
            level_atual = 1
            main()
        elif(level_atual == 8):
            pontuacoes.append(fim.fim(tentativas))
            global level_atual
            level_atual = 0
            main()

        def restart_level():
            tela_atual(level)
        def proxima_fase():
            global level_atual
            level_atual += 1
            pygame.display.set_caption("Seven - %i" % level_atual)
            tela_atual(level_atual)

        # Player
        player_pos = fases.Fase(level).player
        p1 = player.P1(player_pos[0][0], player_pos[0][1])
        velocidade_andar = 2

        #Fase
        paredes = fases.Fase(level).paredes

        #Itens
        chaves = fases.Fase(level).chaves

        while(True):
            #Fechar game
            if(p1.corpo.y > altura):
                global tentativas
                tentativas += 1
                restart_level()
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                #Pressionados
                if(event.type == pygame.KEYDOWN):
                    #Restart
                    if(event.key == pygame.K_ESCAPE):
                        global level_atual
                        level_atual = 0
                        main()

                    if(event.key == pygame.K_a or event.key == pygame.K_LEFT):
                        p1.ad[0] = True
                    if(event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                        p1.ad[1] = True
                    if(event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE):
                        p1.pular(gravidade)
                        p1.em_queda = True
                #Soltos
                if(event.type == pygame.KEYUP):
                    if(event.key == pygame.K_a or event.key == pygame.K_LEFT):
                        p1.ad[0] = False
                    if(event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                        p1.ad[1] = False

                #Joystick
                if(event.type == pygame.JOYBUTTONDOWN):
                    #RESTART
                    if(joy.get_button(8) == True or joy.get_button(9) == True):
                        global level_atual
                        level_atual = 0
                        main()
                    #Butoes
                    if(joy.get_button(0) == True or joy.get_button(1) == True or joy.get_button(2) == True or joy.get_button(3) == True):
                        p1.pular(gravidade)
                        p1.em_queda = True
                if(event.type == pygame.JOYAXISMOTION):
                    # Eixos
                    if (joy.get_axis(0) <= -0.9):
                        p1.ad[0] = True
                    if (joy.get_axis(0) >= 0.9):
                        p1.ad[1] = True
                    if (joy.get_axis(0) > -0.9 and joy.get_axis(0) <= 0):
                        p1.ad[0] = False
                    if (joy.get_axis(0) < 0.9 and joy.get_axis(0) >= -0.1):
                        p1.ad[1] = False

            #Colisao
            for parede in paredes:
                if(p1.corpo.colliderect(parede.corpo)):
                    if(p1.queda >= 0):
                        p1.colidiu(parede.corpo.y + 1)
                        p1.colidindo = True
                        break
                else: p1.colidindo = False
            #Passar Fase
            for chave in chaves:
                if(p1.corpo.colliderect(chave.corpo)):
                    proxima_fase()

            if(p1.colidindo == True): p1.em_queda == False
            elif(p1.colidindo == False): p1.em_queda == True

            if(p1.em_queda == True):
                p1.cair(gravidade)

            #Checar
            p1.mover(velocidade_andar)
            p1.fim_tela(largura)

            #Rodar
            relogio.tick(frames)
            #Desenha
            tela.fill(preto)
            status = font_status.render("%i" % tentativas, 1, branco)
            for parede in paredes:
                parede.desenha_parede(tela, branco)
            for chave in chaves:
                chave.desenha_chave(tela, vermelho)

            p1.desenha_player(tela, verde)
            tela.blit(status, (0, 0))
            pygame.display.update()

    tela_atual(level_atual)

main()