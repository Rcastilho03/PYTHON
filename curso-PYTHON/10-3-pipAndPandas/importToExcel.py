#Importando um dataframe do Excel
#pip install openpyxl
import pandas as pd

dt = pd.read_excel("./cursos2.xlsx")
print(dt)