
pontos_do_jogador = 100 #pontos que o jogador tera e que serao subtraidos ao decorrer do jogo 

numero_sorteado = 31 #é o numero que o usuario tem q acertar

numero_usuario = " " #vai guardar a resposta do usuario 

dificuldade = input("escolha uma dificuldade: facil, normal ou dificil: ")#guardar  a dificuldade desejada pelo jogador

#configura o jogo para as dificuldades facil normal e dificil
if(dificuldade == "facil"):
    print("você tem 30 tentativas")
    tentativas = 30
    pontos_subtraidos_jogador = 10

elif(dificuldade == "normal"):
    print("você tem 15 tentativas")
    tentativas = 15
    pontos_subtraidos_jogador = 20


elif(dificuldade == "dificil"):
    print("você tem 5 tentativas")
    tentativas = 5
    pontos_subtraidos_jogador = 50  
    pontos_do_jogador = 250

numero_usuario = int( input("escolha um numero de 1 a 100: ") ) #pega o numero para o sorteio


#verifica se o usuario acertou ou não, faz o calculo da pontuação e tentativas restantes.
# este loop ira funcionar até o usuario acertar o numero ou as tentativas acabarem
while(tentativas >= 0):

    #se o usuario acertar o numero
    if(numero_sorteado == numero_usuario):
        print("")
        print(f"você acertou, sua pontuação total é de {pontos_do_jogador}")
        break

    #como o usurario não acertou o numero, algumas punições serao aplicadas
    tentativas -= 1
    pontos_do_jogador -= pontos_subtraidos_jogador
    if(pontos_do_jogador <= 0):# para que o jogador não perca mais que zero pontos
        pontos_do_jogador = 0



    #se o usuario escolher um numero errado
    if(numero_sorteado > numero_usuario):
        
        #informa a para o jogador alguns dados 
        print("")
        print(f"você errou,o numero sorteado é maior que {numero_usuario} , sua pontuação atual é de {pontos_do_jogador}")
        print(f"você tem atualmente {tentativas} tentativas para acertar")

    #se o usuario escolher um numero maior que o numero sorteado
    elif(numero_sorteado < numero_usuario):

        #informa a para o jogador alguns dados 
        print("")
        print(f"você errou,o numero sorteado é menor que {numero_usuario} , sua pontuação atual é de {pontos_do_jogador}")
        print(f"você tem atualmente {tentativas} tentativas para acertar")
        

    #menssagem de erro caso o jogador nao colabore
    else:
        print("comando invalido!")
        break
    
    numero_usuario = int( input("escolha um numero de 1 a 100: ") )#faz a pergunta novamente para o user