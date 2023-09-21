#Projeto
global ultimaJogada

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
def mudaSimbolo(simbolo):
  global ultimaJogada
  ultimaJogada = simbolo
  if ultimaJogada == "X" or ultimaJogada == "x":
   ultimaJogada = "O"
  elif ultimaJogada == "O" or ultimaJogada == "o":
    ultimaJogada = "X"

def jogadaDisponivel(simbolo):
  resposta = simbolo
  jogadas[int(resposta)-1] = ultimaJogada

  mudaSimbolo(ultimaJogada)

def analisaVitoria():
  acabou = False
  vitorias = [(jogadas[0],jogadas[1],jogadas[2]), #Linha de cima
              (jogadas[3],jogadas[4],jogadas[5]), #Linha do meio
              (jogadas[6],jogadas[7],jogadas[8]), #Linha de baixo
              (jogadas[0],jogadas[3],jogadas[6]), #Coluna da esquerda
              (jogadas[1],jogadas[4],jogadas[7]), #Coluna do meio
              (jogadas[2],jogadas[5],jogadas[8]), #Coluna da direita
              (jogadas[0],jogadas[4],jogadas[8]), #Diagonal contrabarra
              (jogadas[2],jogadas[4],jogadas[6])] #Diagonal barra
  for i in vitorias:
    if i[0] == i[1] == i[2]: return True
  return False

def recomeco():
  valor = input("""Você deseja continuar jogando?\nSe Sim digite Sim, se não digite Não.""")
  condicao = True if valor == "Sim" or valor == "SIM" or valor == "sim" else False
  if condicao:
    for i in range(len(jogadas)-1):
      jogadas[i] = str(i+1)
      print("Jogadas Disponíveis:\n"+tabuleiroTeste()+"\n")
  return condicao

def partida(simbolo):
  global ultimaJogada
  ultimaJogada = simbolo
  recomecar = True
  while recomecar:
    for i in range(len(jogadas)+1):
      acabou = analisaVitoria()
      if acabou != True:
        if i < 9:
          resposta = input("Escolha a sua jogada:\n")
          if resposta in jogadas:
            jogadaDisponivel(resposta)
            print("\nJogadas Disponíveis:\n"+tabuleiroTeste()+"\n")
          else:
            x = True
            while x:
              resposta = input("Esta jogada não está disponível.\nEscolha uma nova jogada:\n")
              if resposta in jogadas:
                jogadaDisponivel(resposta)
                print("\nJogadas Disponíveis:\n"+tabuleiroTeste()+"\n")
                x = False
      else:
        mudaSimbolo(ultimaJogada)
        print("Parabéns",ultimaJogada)
        break
    deuVelha = analisaVitoria()
    if deuVelha == False:
      print("Deu Velha!")
    recomecar = recomeco()
#sua resposta
print("Bem - Vindo")
jogadas = ["1","2","3","4","5","6","7","8","9"]
jogando = True
libera = False
while not libera:
  ultimaJogada = input("Você quer X ou O?\n")
  if ultimaJogada == "X" or ultimaJogada == "x" or ultimaJogada == "O" or ultimaJogada == "o":
    if ultimaJogada == "x":
      ultimaJogada = "X"
    if ultimaJogada == "o":
      ultimaJogada = "O"
    libera = True
print("Jogadas Disponíveis:\n"+tabuleiroTeste()+"\n")
partida(ultimaJogada)