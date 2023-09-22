#método strftime() -> permite formatar o objeto para o padrão desejado
from datetime import date

d = date(2023, 9, 19)
print(d)
print(d.strftime('%d/%m/%Y'))

d1=d.strftime('%d-%m-%Y')
print(d1)