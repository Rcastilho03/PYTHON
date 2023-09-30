#Exercício 10
#Elabore um gráfico de pizza com a população dos estados solicitados no exercício 9
estados = ("Espírito Santo","Paraná","Rio de Janeiro","São Paulo")
populacao = (3.833,11.443,16.054,44.420)
import matplotlib.pyplot as plt
plt.pie(populacao,labels = estados)
plt.title("Estados")
plt.show()