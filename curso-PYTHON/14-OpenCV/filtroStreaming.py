#Rodar no VSCode
#Filtrando os canais RGB de uma imagem a partir da webcam
#Filtro dinâmico
#Exercício criar trackBar para cores verde e vermelho,
#realizar a leitura e normalizar para 0 a 1 e aplicar ao filtro
import numpy as np
import cv2
filtro = [1,1,1]

def redim(imagem):
    altura = imagem.shape[0]
    largura = imagem.shape[1]
    fator = 0.5
    dim = (int(largura*fator),int(altura*fator))
    return cv2.resize(imagem,dim,interpolation=cv2.INTER_AREA)


def onChange(val):
   return

webcam = cv2.VideoCapture(0)
resultado,imagem = webcam.read()
#Criando a janela de ajuste do filtro
filtroWindow = "Filtro"
cv2.namedWindow(filtroWindow)
cv2.resizeWindow("Filtro", 400,200)

#Criando a barra de ajuste azul
cv2.createTrackbar("Azul", filtroWindow, 0, 100,onChange) #Cria a barra para tom azul
cv2.setTrackbarPos("Azul", filtroWindow,100) #Configura posição inicial do ajuste para 100%

while resultado:
    resultado,imagem = webcam.read()
    imagem = redim(imagem)
    #Lê ajuste do tom azul no trackbar 2 ajusta para número entre 0 e 1
    azul = cv2.getTrackbarPos("Azul", filtroWindow)
    azul = azul/100

    #Configura filtro da imagem
    filtro = [azul,1,1]
    #Obtendo cada pixel da imagem
    #imagem = cv2.imread("logo_opencv.png")
    for l in range (len(imagem)):
        for c in range (len(imagem[l])):
            imagem[l][c] = list(np.multiply(imagem[l][c],filtro))
    cv2.imshow("Video Filtro",imagem)#VSCode
    key = cv2.waitKey(5)
    if key == 27: # ESC
        break
webcam.release()
cv2.destroyAllWindows()