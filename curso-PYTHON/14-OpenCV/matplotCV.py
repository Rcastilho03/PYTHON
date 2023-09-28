#Rodar VS CODE
#Plotando com matplot lib
import cv2
import matplotlib.pyplot as plt
imagem = cv2.imread("logo_opencv.png")
cv2.imshow("Imagem",imagem)#VSCode
plt.imshow(imagem)
plt.show()
cv2.waitKey(0)
#Observe bem as cores na plotagem. O que está acontecendo?