#Criando divisões na janela
import tkinter as tk

class Application:
    def __init__(self, master=None):
      #conteiners são subdivisões da janela criada
      self.container1 = tk.Frame(master)
      self.container1["pady"] = 50 #Espaçamento do conteiner superior
      self.container1.pack()
      self.container2 = tk.Frame(master)
      self.container2["padx"] = 0 #Em volta
      self.container2["pady"] = 50 #Espaçamento superior e inferior
      self.container2.pack()
      self.container3 = tk.Frame(master)
      self.container3["padx"] = 0 #Espaçamento do conteiner lateral
      self.container3["pady"] = 50 #Espaçamento superior e inferior
      self.container3.pack()

      self.titulo = tk.Label(self.container1, text="Conteiner1")
      self.titulo["font"] = ("Arial", "16", "bold")
      self.titulo.pack ()

      self.titulo = tk.Label(self.container2, text="Conteiner2")
      self.titulo["font"] = ("Calibri", "16","italic")
      self.titulo.pack ()

      self.titulo = tk.Label(self.container3, text="Conteiner2")
      self.titulo["font"] = ("Arial", "16")
      self.titulo.pack ()

janela = tk.Tk()
janela.title("Teste conteiners") #Adiciona título a janela
janela.minsize(600,400) #Tamanho mínimo da janela
janela.maxsize(800,600) #Tamanho máximo da janela
Application(janela) #Na classe Application inicializa-se todos os elementos e funcionaliades da janela
janela.mainloop()