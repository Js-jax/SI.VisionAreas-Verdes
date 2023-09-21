import cv2
import numpy as np
kernel = np.ones((5,5), np.uint8) 

# Cargar la imagen
imagen = cv2.imread("maps.png")

# Convertir la imagen a formato HSV (Hue, Saturation, Value)
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Definir los rangos de color verde en formato HSV
verde_bajo = np.array([40, 40, 40])  # Rango mínimo de tono, saturación y valor
verde_alto = np.array([80, 255, 255])  # Rango máximo de tono, saturación y valor

# Crear una máscara para el color verde
mascara_verde = cv2.inRange(imagen_hsv, verde_bajo, verde_alto)

gauss = cv2.GaussianBlur(mascara_verde, (5,5), 0)

cv2.imshow("gauss", gauss)


img_erosion = cv2.erode(gauss, kernel, iterations=1) 
img_dilation = cv2.dilate(gauss, kernel, iterations=1)

cv2.imshow("erosion", img_erosion)



bordes = cv2.Canny(img_erosion, 200, 400)

cv2.imshow("canny", bordes)

(contornos,_) = cv2.findContours(bordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Piedras {} ".format(len(contornos)))

cv2.drawContours(imagen,contornos,-1,(0,0,255), 2)

cv2.imshow("Piedras", imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()
