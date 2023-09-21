import matplotlib.pyplot as plt
#Exercício 9
#gráfico de barra população atual por estado
#1 para os estados apresentados a seguir, pesquise a população atual
#2 gere uma lista condendo a população de cada estado coordenadamente a tupla
#3 Plotar gráfico de barras com as devidas formatações
estados = ("Espírito Santo","Paraná","Rio de Janeiro","São Paulo")
populacao =[3.833,11.443,16.054,44.420]

plt.bar(estados,populacao,color="yellow")
plt.title("Estados Brasileiros(População)")
plt.xlabel("Estados") 
plt.ylabel("População(milhões)") 
plt.grid(True)
plt.show()