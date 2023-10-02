# Foi uma honra vacilar com você
# Criando um campo de digitação
import tkinter as tk
from tkinter import messagebox

class Application:
    def __init__(self, master=None):

        self.fonteBtn =("Verdana","9")
        self.fonteTxt =("Arial","12")
        self.pady = "28"
        self.padx = "10"
        #conteiners são subdivisões da janela criada
        self.ct1 = tk.Frame(master)
        self.ct1["pady"] = self.pady #Espaçamento do conteiner superior
        self.ct1.pack()

        self.ct2 = tk.Frame(master)
        self.ct2["pady"] = self.pady #Espaçamento do conteiner superior
        self.ct2.pack()

        self.ct6 = tk.Frame(master)
        self.ct6["pady"] = self.pady #Espaçamento do conteiner superior
        self.ct6.pack()

        self.ct11 = tk.Frame(master)
        self.ct11["pady"] = self.pady #Espaçamento do conteiner superior
        self.ct11.pack()

        self.ct14 = tk.Frame(master)
        self.ct14["pady"] = self.pady #Espaçamento do conteiner superior
        self.ct14.pack()

#Containers inside ct2
        self.ct3 = tk.Frame(self.ct2)
        self.ct3["pady"] = self.padx #Espaçamento do conteiner superior
        self.ct3.pack(side = "left")

        self.ct4 = tk.Frame(self.ct2)
        self.ct4["pady"] = self.padx #Espaçamento do conteiner superior
        self.ct4.pack(side = "left")

        self.ct5 = tk.Frame(self.ct2)
        self.ct5["pady"] = self.padx #Espaçamento do conteiner superior
        self.ct5.pack(side = "left")

#Containers inside ct6
        self.ct7 = tk.Frame(self.ct6)
        self.ct7["pady"] = self.padx #Espaçamento do conteiner superior
        self.ct7.pack(side = "left")

        self.ct8 = tk.Frame(self.ct6)
        self.ct8["pady"] = self.padx #Espaçamento do conteiner superior
        self.ct8.pack(side = "left")

        self.ct9 = tk.Frame(self.ct6)
        self.ct9["pady"] = self.padx #Espaçamento do conteiner superior
        self.ct9.pack(side = "left")

        self.ct10 = tk.Frame(self.ct6)
        self.ct10["pady"] = self.padx #Espaçamento do conteiner superior
        self.ct10.pack(side = "left")

#Containers inside ct11
        self.ct12 = tk.Frame(self.ct11)
        self.ct12["pady"] = self.padx #Espaçamento do conteiner superior
        self.ct12.pack(side = "left")

        self.ct13 = tk.Frame(self.ct11)
        self.ct13["pady"] = self.padx #Espaçamento do conteiner superior
        self.ct13.pack(side = "left")



        self.titulo = tk.Label(self.ct1, text="Pesquisa Seleção")
        self.titulo["font"] = ("Arial", "16", "bold")
        self.titulo.pack ()

        self.titulo1 = tk.Label(self.ct3, text="Jogadores")
        self.titulo1["font"] = ("Arial", "16", "bold")
        self.titulo1.pack ()


        self.jogador = tk.Entry(self.ct4)
        self.jogador["width"] = 30
        self.jogador["font"] = self.fonteTxt
        self.jogador.pack()
        

        self.btnBusca = tk.Button(self.ct5, text="Busca", font=self.fonteBtn, width=10)
        self.btnBusca["command"] = self.busca
        self.btnBusca.pack(side=tk.LEFT)




        self.titulo2 = tk.Label(self.ct7, text="Clube:")
        self.titulo2["font"] = ("Arial", "16", "bold")
        self.titulo2.pack ()
        
        self.clube = tk.Label(self.ct8, text="?????")
        self.clube["font"] = ("Arial", "10")
        self.clube.pack ()

        self.titulo3 = tk.Label(self.ct9, text="País:")
        self.titulo3["font"] = ("Arial", "16", "bold")
        self.titulo3.pack ()
        
        self.pais = tk.Label(self.ct10, text="?????")
        self.pais["font"] = ("Arial", "10")
        self.pais.pack ()




        self.titulo4 = tk.Label(self.ct12, text="Salário:")
        self.titulo4["font"] = ("Arial", "16", "bold")
        self.titulo4.pack ()
        
        self.salario = tk.Label(self.ct13, text="?????")
        self.salario["font"] = ("Arial", "10")
        self.salario.pack ()



        self.btnSair = tk.Button(self.ct14, text="SAIR", font=self.fonteBtn, width=10)
        self.btnSair["command"] = master.quit
        self.btnSair.pack()


#
        
#
        #self.texto = tk.Label(self.container3,text="Horas:")
        #self.texto["font"] = ("Arial", "16", "bold")
        #self.texto.pack(side=tk.LEFT)
#
        #self.horas = tk.Label(self.container3,text="Vazio")
        #self.horas["font"] = ("Arial", "16", "bold")
        #self.horas.pack(side=tk.LEFT)


    def busca(self):
        player=self.jogador.get()
        print(player)
        if player in nome:
            indice = nome.index(player)
            self.clube["text"] = clubes[indice]
            self.pais["text"] = países[indice]
            self.salario["text"] = str(salarios[indice])+" Milhões"

        else:
            self.clube["text"] = "????????"
            self.pais["text"] = "????????"
            self.salario["text"] = "????????"
            messagebox.showwarning(title="Atenção",message="Jogador não encontrado")


nome = ["Alex Telles","Alexsandro",	"Alisson",	"Bruno Guimarães",	"Casemiro",	"Daniel Alves",	"Danilo","Danilo","Eder Militão","Ederson","Fabinho","Fred","Gabriel Martinelli",	"Guilherme Arana",	"Lucas Paquetá",	"Marquinhos",	"Neymar",	"Philippe Coutinho",	"Raphinha",	"Richarlison",	"Rodrygo",	"Thiago Silva",	"Vinícius Junior",	"Weverton"]
clubes=["Manchester",	"Juventus",	"Liverpool",	"Newcastle",	"Real Madrid",	"Barcelona",	"Palmeiras",	"Juventus",	"Real Madrid",	"Manchester",	"Liverpool",	"Manchester",	"Arsenal",	"Atlético-MG"	,"Lyon",	"PSG"	,"PSG",	"Aston Villa",	"Leeds United",	"Everton",	"Real Madrid",	"Chelsea",	"Real Madrid",	"Palmeiras"]
países = ["Inglaterra","Itália","Inglaterra","Inglaterra","Espanha","Espanha","Brasil","Itália","Espanha","Inglaterra","Inglaterra","Inglaterra","Inglaterra","Brasil","França","França","França","Inglaterra","Inglaterra","Inglaterra","Espanha","Inglaterra","Espanha","Brasil"]
salarios= [2.7,	2.4,	5.1,	2.5,	5.1,	0.98,	0.5,	2.2,	4.2,	4.3,	4.1,	3.4,	0.95,	0.45,	4.5	,7.1,	22,	9.5,	4.1,	2.5,	3.5,	2.8,	5.5,	0.3]


janela = tk.Tk()
janela.title("Cursos") #Adiciona título a janela
janela.minsize(600,400) #Tamanho mínimo da janela
janela.maxsize(800,600) #Tamanho máximo da janela
Application(janela) #Na classe Application inicializa-se todos os elementos e funcionaliades da janela
janela.mainloop()