#Aplicação de Tracking de Objeto baseado em filtro de cores

# pip install numpy
# pip install opencv-python

#Exercício: altere a cor do retângulo para amarelo,
#Exercício: defina as posições inicias das barras para um ajuste de algum objeto
#Exercício: adicione um trackBar de 0 a 1 chamado seleção
#Fazer a leitura do trackbar de Seleção
#Se a seleção for 1 deve-se mostrar a imagem colorida (frame), se não deve mostrar
#a imagem da máscara (gray)

import numpy as np
import cv2


ESC_KEY = 27

cap = cv2.VideoCapture(0)

def setLimitsOfTrackbar():
    hue = {}
    hue["min"] = cv2.getTrackbarPos("Min Hue", trackbarWindow)
    hue["max"] = cv2.getTrackbarPos("Max Hue", trackbarWindow)

    if hue["min"] > hue["max"]:
        cv2.setTrackbarPos("Max Hue", trackbarWindow, hue["min"])
        hue["max"] = cv2.getTrackbarPos("Max Hue", trackbarWindow)

    sat = {}
    sat["min"] = cv2.getTrackbarPos("Min Saturation", trackbarWindow)
    sat["max"] = cv2.getTrackbarPos("Max Saturation", trackbarWindow)

    if sat["min"] > sat["max"]:
        cv2.setTrackbarPos("Max Saturation", trackbarWindow, sat["min"])
        sat["max"] = cv2.getTrackbarPos("Max Saturation", trackbarWindow)

    val = {}
    val["min"] = cv2.getTrackbarPos("Min Value", trackbarWindow)
    val["max"] = cv2.getTrackbarPos("Max Value", trackbarWindow)

    if val["min"] > val["max"]:
        cv2.setTrackbarPos("Max Value", trackbarWindow, val["min"])
        val["max"] = cv2.getTrackbarPos("Max Value", trackbarWindow)

    return hue, sat, val

def computeTracking(frame, hue, sat, val):

    #transforma a imagem de BGR para HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #definir os intervalos de cores que vão aparecer na imagem final
    lowerColor = np.array([hue['min'], sat["min"], val["min"]])
    upperColor = np.array([hue['max'], sat["max"], val["max"]])

    #marcador pra saber se o pixel pertence ao intervalo ou não
    mask = cv2.inRange(hsvImage, lowerColor, upperColor)

    #aplica máscara que "deixa passar" pixels pertencentes ao intervalo, como filtro
    result = cv2.bitwise_and(frame, frame, mask = mask)

    #aplica limiarização
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    _,gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    #encontra pontos que circundam regiões conexas (contour)
    contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    #se existir contornos
    if contours:
        #retornando a área do primeiro grupo de pixels brancos
        maxArea = cv2.contourArea(contours[0])
        maxArea2 = 0
        contourMaxAreaId = 0
        contourMaxAreaId2 = 0
        i = 0

        #para cada grupo de pixels branco
        for cnt in contours:
            #procura o grupo com a maior área
            if maxArea < cv2.contourArea(cnt):
                maxArea2=maxArea
                contourMaxAreaId2 =contourMaxAreaId
                maxArea = cv2.contourArea(cnt)
                contourMaxAreaId = i

            elif maxArea2<cv2.contourArea(cnt):
                maxArea2=cv2.contourArea(cnt)
                contourMaxAreaId2=i
            i += 1
            print (i)

        #achei o contorno com maior área em pixels
        cntMaxArea = contours[contourMaxAreaId]
        cntMaxArea2 = contours[contourMaxAreaId2]

        #retorna um retângulo que envolve o contorno em questão
        xRect, yRect, wRect, hRect = cv2.boundingRect(cntMaxArea)
        #desenha caixa envolvente com espessura 3
        cv2.rectangle(frame, (xRect, yRect), (xRect + wRect, yRect + hRect), (211, 0, 148), 2) #bgr
        pontoInicial = int(xRect+wRect/2),int(yRect+hRect/2)
        texto = str(int(xRect+wRect/2))+","+str(int(yRect+hRect/2))
        cv2.putText(frame, texto, pontoInicial, fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 1, color = (250,225,100))
    return frame, gray

trackbarWindow = "trackbar window"
cv2.namedWindow(trackbarWindow)
cv2.resizeWindow("trackbar window", 500,500)

def onChange(val):
    return

cv2.createTrackbar("Min Hue", trackbarWindow, 0, 255, onChange)
cv2.createTrackbar("Max Hue", trackbarWindow, 255, 255, onChange)

cv2.createTrackbar("Min Saturation", trackbarWindow, 0, 255, onChange)
cv2.createTrackbar("Max Saturation", trackbarWindow, 255, 255, onChange)

cv2.createTrackbar("Min Value", trackbarWindow, 0, 255, onChange)
cv2.createTrackbar("Max Value", trackbarWindow, 255, 255, onChange)

min_hue = cv2.getTrackbarPos("Min Hue", trackbarWindow)
max_hue = cv2.getTrackbarPos("Max Hue", trackbarWindow)

min_sat = cv2.getTrackbarPos("Min Saturation", trackbarWindow)
max_sat = cv2.getTrackbarPos("Max Saturation", trackbarWindow)

min_val = cv2.getTrackbarPos("Min Value", trackbarWindow)
max_val = cv2.getTrackbarPos("Max Value", trackbarWindow)


cv2.setTrackbarPos("Min Hue", trackbarWindow,0)
cv2.setTrackbarPos("Max Hue", trackbarWindow,255)
cv2.setTrackbarPos("Min Saturation", trackbarWindow,0)
cv2.setTrackbarPos("Max Saturation", trackbarWindow,255)
cv2.setTrackbarPos("Min Value", trackbarWindow,0)
cv2.setTrackbarPos("Max Value", trackbarWindow,255)

while True:
    success, frame = cap.read()

    hue, sat, val  = setLimitsOfTrackbar()
    frame, gray = computeTracking(frame, hue, sat, val)

    cv2.imshow("mascara", gray)
    cv2.imshow("webcam", frame)

    key = cv2.waitKey(5)
    if key == 27: # ESC
        break

cap.release()
cv2.destroyAllWindows()