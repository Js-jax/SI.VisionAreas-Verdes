import cv2
import numpy as np
kernel = np.ones((5,5), np.uint8) 

# Cargar la imagen
imagen = cv2.imread("maps1.png")

imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
# Convertir la imagen a formato HSV (Hue, Saturation, Value)
verde_bajo1 = np.array([35, 40, 40])  # Rango mínimo de tono, saturación y valor
verde_alto1 = np.array([85, 255, 255])  # Rango máximo de tono, saturación y valor

verde_bajo2 = np.array([85, 40, 40])  # Segundo rango mínimo de tono, saturación y valor
verde_alto2 = np.array([120, 255, 255])  # Segundo rango máximo de tono, saturación y valor

# Crear máscaras para los rangos de color verde
mascara_verde1 = cv2.inRange(imagen_hsv, verde_bajo1, verde_alto1)
mascara_verde2 = cv2.inRange(imagen_hsv, verde_bajo2, verde_alto2)

# Combinar las máscaras para detectar ambos rangos de color verde
mascara_combinada = cv2.bitwise_or(mascara_verde1, mascara_verde2)

# Aplicar la máscara combinada a la imagen original
resultado = cv2.bitwise_and(imagen, imagen, mask=mascara_combinada)


gauss = cv2.GaussianBlur(resultado, (5,5), 0)

cv2.imshow("gauss", gauss)


img_erosion = cv2.erode(gauss, kernel, iterations=1) 
img_dilation = cv2.dilate(gauss, kernel, iterations=1)

cv2.imshow("erosion", img_erosion)



bordes = cv2.Canny(img_erosion, 80, 180)

cv2.imshow("canny", bordes)

(contornos,_) = cv2.findContours(bordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Areas Verdes {} ".format(len(contornos)))

cv2.drawContours(imagen,contornos,-1,(0,0,255), 2)

cv2.imshow("Areas Verdes", imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()
