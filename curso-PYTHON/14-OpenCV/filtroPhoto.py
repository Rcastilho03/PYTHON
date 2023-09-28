#Rodar no VSCode
#Filtrando os canais RGB de uma imagem a partir da webcam
import numpy as np
import cv2
filtro = [3,0.5,0]

webcam = cv2.VideoCapture(0)
resultado,imagem = webcam.read()

#Obtendo cada pixel da imagem
#imagem = cv2.imread("logo_opencv.png")
imagemFiltro = imagem.copy()
for l in range (len(imagemFiltro)):
  for c in range (len(imagemFiltro[l])):
    imagemFiltro[l][c] = list(np.multiply(imagemFiltro[l][c],filtro))
cv2.imshow("Imagem Filtro",imagemFiltro)#VSCode
cv2.waitKey(0)
webcam.release()
cv2.destroyAllWindows()