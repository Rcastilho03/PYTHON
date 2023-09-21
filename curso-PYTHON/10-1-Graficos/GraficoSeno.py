#Exercício 8
#1 Para a lista criada a seguir arredonde os resultados com duas casas
#no momento da criação da lista
#2 Elabore uma lista que armazene os resultados do seno
#de cada valor da lista de radianos criada
#3 Plotar o gráfico de dispersão com titulo, nomes nos eixos e grid
import math
import matplotlib.pyplot as plt
listaRadianos =[round(0.1*math.pi*i,2) for i in range(21)]

resultSeno = [math.sin(i) for i in listaRadianos]
plt.plot(listaRadianos,resultSeno)
plt.title("Grafico do Seno")
plt.xlabel("Pi rad")
plt.ylabel("Seno")
plt.show()