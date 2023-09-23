import pandas as pd
cursos = {
    "curso":["Python","PowerBI","JavaFundamentals","MicrosoftAI900","GoogleFoundations"],
    "horas":[80,20,80,40,40]
    }
#print(cursos)

dt = pd.DataFrame(cursos)
print(dt)
dt