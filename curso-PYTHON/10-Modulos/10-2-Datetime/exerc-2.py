#Exercício 2
#Analise o link de formatação de string dado acima e tente chegar na formatação
#que resulta em:
# 19 de September de 2023 - Tuesday
from datetime import date
d = date(2023, 9, 19)
print(d.strftime('%d de %B de %Y - %A'))