import pandas as pd

dt = pd.read_excel("./vendas.xlsx")
dicionario = dt.to_dict()
dicionario["preço unitário"][3] = 500
dt2 = pd.DataFrame(dicionario)

print(dt2)