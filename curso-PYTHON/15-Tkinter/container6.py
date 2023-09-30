#Explorando divisões na janela
import tkinter as tk

class Application:
    def __init__(self, master=None):
      #conteiners são subdivisões da janela criada
      self.container1 = tk.Frame(master,bg="red")
      self.container1["pady"] = 50 #Espaçamento do conteiner superior
      self.container1.pack()
      self.container2 = tk.Frame(master,bg="green")
      self.container2["padx"] = 0 #Em volta
      self.container2["pady"] = 50 #Espaçamento superior e inferior
      self.container2.pack()
      self.container3 = tk.Frame(master,bg="yellow")
      self.container3["padx"] = 0 #Espaçamento do conteiner lateral
      self.container3["pady"] = 50 #Espaçamento superior e inferior
      self.container3.pack()
      self.container4 = tk.Frame(self.container3,bg="blue")
      self.container4["padx"] = 30 #Espaçamento do conteiner lateral
      self.container4.pack(side="left")
      self.container5 = tk.Frame(self.container3,bg="magenta")
      self.container5["padx"] = 30 #Espaçamento do conteiner lateral
      self.container5.pack(side="left")
      self.container6 = tk.Frame(self.container3,bg="orange")
      self.container6["padx"] = 30 #Espaçamento do conteiner lateral
      self.container6.pack(side="left")



      self.titulo = tk.Label(self.container1, text="Conteiner1")
      self.titulo["font"] = ("Arial", "16", "bold")
      self.titulo.pack ()

      self.titulo1 = tk.Label(self.container2, text="Conteiner2")
      self.titulo1["font"] = ("Calibri", "16","italic")
      self.titulo1.pack ()

      self.titulo2 = tk.Label(self.container4, text="Conteiner4")
      self.titulo2["font"] = ("Arial", "16")
      self.titulo2.pack ()

      self.titulo3 = tk.Label(self.container5, text="Conteiner5")
      self.titulo3["font"] = ("Arial", "16")
      self.titulo3.pack ()

      self.titulo4 = tk.Label(self.container6, text="Conteiner6")
      self.titulo4["font"] = ("Arial", "16")
      self.titulo4.pack ()

janela = tk.Tk()
janela.title("Teste conteiners") #Adiciona título a janela
janela.minsize(600,400) #Tamanho mínimo da janela
janela.maxsize(800,600) #Tamanho máximo da janela
Application(janela) #Na classe Application inicializa-se todos os elementos e funcionaliades da janela
janela.mainloop()