import random as rd
def vsPC():
  global player1
  global playerPC
  global vencedor

  def tabuleiroTeste():
    return """
  +-----+-----+-----+
  |  """+jogadas[0]+"""  |  """+jogadas[1]+"""  |  """+jogadas[2]+"""  |
  +-----+-----+-----+
  |  """+jogadas[3]+"""  |  """+jogadas[4]+"""  |  """+jogadas[5]+"""  |
  +-----+-----+-----+
  |  """+jogadas[6]+"""  |  """+jogadas[7]+"""  |  """+jogadas[8]+"""  |
  +-----+-----+-----+
  """

  def analisaVitoria():
    global vencedor
    acabou = False
    contagem = 0
    vitorias = [(jogadas[0],jogadas[1],jogadas[2]), #Linha de cima
                (jogadas[3],jogadas[4],jogadas[5]), #Linha do meio
                (jogadas[6],jogadas[7],jogadas[8]), #Linha de baixo
                (jogadas[0],jogadas[3],jogadas[6]), #Coluna da esquerda
                (jogadas[1],jogadas[4],jogadas[7]), #Coluna do meio
                (jogadas[2],jogadas[5],jogadas[8]), #Coluna da direita
                (jogadas[0],jogadas[4],jogadas[8]), #Diagonal contrabarra
                (jogadas[2],jogadas[4],jogadas[6])] #Diagonal barra
    for i in vitorias:
      if i[0] == i[1] == i[2]: vencedor = i[0]; return True
    for i in jogadas:
      if i == "X" or i == "O":
        contagem +=1
        if contagem == 9: vencedor = "deu Velha"; return True
    return False
  
  def jogadaDisponivel(simbolo,simPl1):
    resposta = simbolo
    jogadas[int(resposta)-1] = simPl1

  def jogadaPl1(simbolo):
    global player1
    player1 = simbolo
    recomecar = True
    resposta = input("Escolha a sua jogada:\n")
    if resposta in jogadas:
      jogadaDisponivel(resposta,player1)
      print("\nJogadas Disponíveis:\n"+tabuleiroTeste()+"\n")
    else:
      while True:
        resposta = input("Esta jogada não está disponível.\nEscolha uma nova jogada:\n")
        if resposta in jogadas:
          jogadaDisponivel(resposta,player1)
          print("\nJogadas Disponíveis:\n"+tabuleiroTeste()+"\n")
          break

  def jogadaPC(simbolo):
    playerPC = simbolo
    listaFiltro = []
    for i in jogadasPadrao:
      if i in jogadas:
        listaFiltro.append(i)
    #Realizar o sorteio na lista filtro
    sorteado = rd.choice(listaFiltro)
    indice = jogadas.index(sorteado)
    jogadas[indice] = simbolo
    print("\nJogadas Disponíveis:\n"+tabuleiroTeste()+"\n")

  def partida(simPl1,simPl2):
    while True:
      acabou = analisaVitoria()
      if acabou != True:
        #print(jogadas.count(simPl2))
        if jogadas.count(simPl2) == 0:
         jogadas[4] = simPl2
         print("\nJogadas Disponíveis:\n"+tabuleiroTeste()+"\n")
        else:
         nJogada = len(jogadas) - jogadas.count(simPl1) - jogadas.count(simPl2)
         if nJogada%2 == 0:
          jogadaPl1(simPl1)
         elif nJogada%2 == 1:
          jogadaPC(simPl2)
      else:
        print("Parabéns",vencedor)
        break

    #sua resposta
  print("Bem - Vindo")
  jogadas = ["1","2","3","4","5","6","7","8","9"]
  jogadasPadrao = ["1","2","3","4","5","6","7","8","9"]
  jogando = True
  libera = False
  while True:
    player1 = input("Você quer X ou O?\n")
    if player1 == "X" or player1 == "x" or player1 == "O" or player1 == "o":
      if player1 == "X" or player1 == "x":
        if player1 == "x":
          player1 = "X"
        playerPC = "O"
      if player1 == "O" or player1 == "o":
        if player1 == "o":
          player1 = "O"
        playerPC = "X"
      break
  print("Jogadas Disponíveis:\n"+tabuleiroTeste()+"\n")
  partida(player1,playerPC)
vsPC()