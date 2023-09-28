#No VSCode
#Utilizando a WEBCam para streaming de video
import cv2

webcam = cv2.VideoCapture(0)
resultado,imagem = webcam.read()
while resultado:
  resultado,imagem = webcam.read()
  cv2.imshow("Video",imagem)
  key = cv2.waitKey(5)
  if key == 27: # ESC
      break

print(resultado,imagem)
webcam.release()
cv2.destroyAllWindows()