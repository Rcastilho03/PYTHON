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


        self.titulo = tk.Label(self.container1, text="Buscador")
        self.titulo["font"] = ("Arial", "16", "bold")
        self.titulo.pack ()

        self.campoNome = tk.Entry(self.container2)
        self.campoNome["width"] = 30
        self.campoNome["font"] = self.fonteTxt
        self.campoNome.pack(side=tk.LEFT)

        self.btnBusca = tk.Button(self.container2, text="Busca", font=self.fonteBtn, width=10)
        self.btnBusca["command"] = self.busca
        self.btnBusca.pack(side=tk.LEFT)

        self.texto = tk.Label(self.container3,text="Vazio")
        self.texto["font"] = ("Arial", "16", "bold")
        self.texto.pack ()


    def busca(self):
        nome=self.campoNome.get()
        self.texto["text"] = nome



janela = tk.Tk()
janela.title("Captura de dados") #Adiciona título a janela
janela.minsize(600,400) #Tamanho mínimo da janela
janela.maxsize(800,600) #Tamanho máximo da janela
Application(janela) #Na classe Application inicializa-se todos os elementos e funcionaliades da janela
janela.mainloop()