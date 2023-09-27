#Rodas no VSCode
#precisa instalar a biblioteca (basta digitar comando abaixo no powershell do terminal)
#pip install pyodbc
import pyodbc
from datetime import date
from datetime import datetime

server = 'serverpythondb.database.windows.net'
database = 'pythonDatabase'
username = 'Python'
password = '{P!th0n502}'
driver= '{ODBC Driver 17 for SQL Server}'#->VSCode Windows

hoje = datetime.today()

dia = str(hoje.day)
mes = str(hoje.month)
ano = str(hoje.year)
hora = str(hoje.hour)
minuto =str(hoje.minute)
segundo =str(hoje.second)


print(hoje.hour)
print(hoje.minute)
print(hoje.second)
print(hoje.microsecond)

def leitura():
    with pyodbc.connect('DRIVER='+driver+
                        ';SERVER=tcp:'+server+
                        ';PORT=1433;DATABASE='+database+
                        ';UID='+username+
                        ';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM dbo.Registro")
            row = cursor.fetchone()
            while row:
                print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4])+ " " + str(row[5])+ " " + str(row[6])+ " " + str(row[7])+ " " + str(row[8]))
                #print("Lendo")
                row = cursor.fetchone()

def escrita():

  nome = input("Digite seu nome:\t")
  litros = input("Quantos litros você deseja colocar?\t")
  with pyodbc.connect('DRIVER='+driver+
                        ';SERVER=tcp:'+server+
                        ';PORT=1433;DATABASE='+database+
                        ';UID='+username+
                        ';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO [dbo].[Registro] (Dia,Mes,Ano,Hora,Minuto,Segundo,Litros,Nome) VALUES ("+dia+","+mes+","+ano+","+hora+","+minuto+","+segundo+","+litros+","+"'"+nome+"'")
            conn.commit()




#escrita()
leitura()