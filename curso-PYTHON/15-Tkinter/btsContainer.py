#Criando botões em um conteiner
import tkinter as tk

class Application:
    def __init__(self, master=None):
        self.fonteBtn =("Verdana","9")
        #conteiners são subdivisões da janela criada
        self.container1 = tk.Frame(master)
        self.container1["pady"] = 20 #Espaçamento do conteiner superior
        self.container1.pack()
        self.container2 = tk.Frame(master)
        self.container2["padx"] = 200 #Em volta
        self.container2["pady"] = 20 #Espaçamento superior e inferior
        self.container2.pack()

        self.titulo = tk.Label(self.container1, text="Conteiner - Título")
        self.titulo["font"] = ("Arial", "16", "bold")
        self.titulo.pack ()

        self.btnEsquerda = tk.Button(self.container2, text="Esquerda", font=self.fonteBtn, width=10)
        self.btnEsquerda["command"] = self.esquerda
        self.btnEsquerda.pack(side=tk.LEFT)

        self.btnCentro = tk.Button(self.container2, text="Sair", font=self.fonteBtn, width=10)
        self.btnCentro["command"] = self.container1.quit
        self.btnCentro.pack(side=tk.LEFT)

        self.btnDireita = tk.Button(self.container2, text="Direita", font=self.fonteBtn, width=10)
        self.btnDireita["command"] = self.direita
        self.btnDireita.pack(side=tk.LEFT)

    def esquerda(self):
        self.titulo["text"] = "Esquerda"

    def direita(self):
        self.titulo["text"] = "Direita"


janela = tk.Tk()
janela.title("Teste conteiners") #Adiciona título a janela
janela.minsize(600,400) #Tamanho mínimo da janela
janela.maxsize(800,600) #Tamanho máximo da janela
Application(janela) #Na classe Application inicializa-se todos os elementos e funcionaliades da janela
janela.mainloop()