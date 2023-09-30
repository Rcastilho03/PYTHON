#Criando um campo de digitação
import tkinter as tk

class Application:
    def __init__(self, master=None):

        self.fonteBtn =("Verdana","9")
        self.fonteTxt =("Arial","12")
        #conteiners são subdivisões da janela criada
        self.container1 = tk.Frame(master)
        self.container1["pady"] = 20 #Espaçamento do conteiner superior
        self.container1.pack()

        self.container2 = tk.Frame(master)
        self.container2["padx"] = 20 #Em volta
        self.container2["pady"] = 20 #Espaçamento superior e inferior
        self.container2.pack()

        self.container3 = tk.Frame(master)
        self.container3["padx"] = 20 #Em volta
        self.container3["pady"] = 20 #Espaçamento superior e inferior
        self.container3.pack()


        self.titulo = tk.Label(self.container1, text="Nome do curso")
        self.titulo["font"] = ("Arial", "16", "bold")
        self.titulo.pack ()

        self.campoCurso = tk.Entry(self.container2)
        self.campoCurso["width"] = 30
        self.campoCurso["font"] = self.fonteTxt
        self.campoCurso.pack(side=tk.LEFT)

        self.btnBusca = tk.Button(self.container2, text="Busca", font=self.fonteBtn, width=10)
        self.btnBusca["command"] = self.busca
        self.btnBusca.pack(side=tk.LEFT)

        self.texto = tk.Label(self.container3,text="Horas:")
        self.texto["font"] = ("Arial", "16", "bold")
        self.texto.pack(side=tk.LEFT)

        self.horas = tk.Label(self.container3,text="Vazio")
        self.horas["font"] = ("Arial", "16", "bold")
        self.horas.pack(side=tk.LEFT)


    def busca(self):
        nome=self.campoCurso.get()
        if nome in curso:
            indice = curso.index(nome)
            self.horas["text"] = horasLista[indice]
        else:
            self.horas["text"] = "Curso não encontrado"


curso=['Python',"PowerBI","JavaFundamentals","MicrosoftAI900","GoogleFoundations"]
horasLista=[80,20,80,40,40]

janela = tk.Tk()
janela.title("Cursos") #Adiciona título a janela
janela.minsize(600,400) #Tamanho mínimo da janela
janela.maxsize(800,600) #Tamanho máximo da janela
Application(janela) #Na classe Application inicializa-se todos os elementos e funcionaliades da janela
janela.mainloop()