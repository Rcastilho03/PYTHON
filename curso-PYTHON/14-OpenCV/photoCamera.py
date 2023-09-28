#No VSCode
#Utilizando a WEBCam para tirar foto
import cv2

webcam = cv2.VideoCapture(0)
resultado,imagem = webcam.read()

cv2.imshow("Foto",imagem)
cv2.waitKey(0)
print(resultado,imagem)
webcam.release()
cv2.destroyAllWindows()