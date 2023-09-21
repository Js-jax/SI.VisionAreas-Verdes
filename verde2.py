import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

# Cargar la imagen
imagen = cv2.imread("maps3.png")

imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Rangos de color verde
verde_bajo1 = np.array([35, 40, 40])
verde_alto1 = np.array([85, 255, 255])
verde_bajo2 = np.array([85, 40, 40])
verde_alto2 = np.array([120, 255, 255])

# Crear máscaras para los rangos de color verde
mascara_verde1 = cv2.inRange(imagen_hsv, verde_bajo1, verde_alto1)
mascara_verde2 = cv2.inRange(imagen_hsv, verde_bajo2, verde_alto2)

# Combinar las máscaras para detectar ambos rangos de color verde
mascara_combinada = cv2.bitwise_or(mascara_verde1, mascara_verde2)

# Aplicar la máscara combinada a la imagen original
resultado = cv2.bitwise_and(imagen, imagen, mask=mascara_combinada)

# Aplicar filtro Gaussiano
gauss = cv2.GaussianBlur(resultado, (5, 5), 0)

# Aplicar erosión y dilatación
img_erosion = cv2.erode(gauss, kernel, iterations=1)
img_dilation = cv2.dilate(gauss, kernel, iterations=1)

# Aplicar detección de bordes Canny
bordes = cv2.Canny(img_erosion, 80, 180)

# Encontrar contornos en la imagen de bordes
(contornos, _) = cv2.findContours(bordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Calcular el área total de la imagen
area_total = imagen.shape[0] * imagen.shape[1]

# Calcular el área de las áreas verdes
area_areas_verdes = sum(cv2.contourArea(contorno) for contorno in contornos)

# Calcular el porcentaje de áreas verdes
porcentaje_areas_verdes = (area_areas_verdes / area_total) * 100

print("Área Total de la Imagen: {} pixeles cuadrados".format(area_total))
print("Área de Áreas Verdes: {} pixeles cuadrados".format(area_areas_verdes))
print("Porcentaje de Áreas Verdes: {:.2f}%".format(porcentaje_areas_verdes))

# Dibujar contornos en la imagen original
cv2.drawContours(imagen, contornos, -1, (0, 0, 255), 2)

# Mostrar la imagen con los contornos
cv2.imshow("Áreas Verdes", imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()
