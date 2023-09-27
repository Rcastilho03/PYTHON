#Rodas no VSCode
#precisa instalar a biblioteca (basta digitar comando abaixo no powershell do terminal)
#pip install pyodbc
import pyodbc

server = 'serverpythondb.database.windows.net'
database = 'pythonDatabase'
username = 'Python'
password = '{P!th0n502}'
driver= '{ODBC Driver 17 for SQL Server}'#->VSCode Windows

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
    with pyodbc.connect('DRIVER='+driver+
                        ';SERVER=tcp:'+server+
                        ';PORT=1433;DATABASE='+database+
                        ';UID='+username+
                        ';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO [dbo].[Registro] (Dia,Mes,Ano,Hora,Minuto,Segundo,Litros,Nome) VALUES (1,8,2023,1,5,30,10,'Wagner')")
            conn.commit()







#escrita()
leitura()