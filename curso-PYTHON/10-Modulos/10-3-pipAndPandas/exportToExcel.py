#Exportando um dataframe para o Excel
#pip install openpyxl
import pandas as pd
cursos = {
    "curso":["Python","PowerBI","JavaFundamentals","MicrosoftAI900","GoogleFoundations"],
    "horas":[80,20,80,40,40]
    }
#print(cursos)

dt = pd.DataFrame(cursos)
dt.sort_values("horas")
dt.to_excel("./cursos2.xlsx",index = False)
print(dt.sort_values("horas",ascending=False))