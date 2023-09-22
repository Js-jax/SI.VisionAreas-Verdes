# ECOVISION

<aside>
💡 Vehículos aéreos no tripulados (UAV): Estos vehículos son los encargados de realizar la recopilación de datos. Están equipados con sensores que permiten medir el índice de calidad del aire, cambios climáticos y otros parámetros ambientales.

Componentes eléctricos para medir el nivel de CO2: Estos componentes son los que permiten realizar las mediciones de CO2 en el aire.

Programa por visión por computadora para estimar y proponer acciones: Este programa utiliza los datos recopilados por los UAV y los componentes eléctricos para estimar la calidad del aire y proponer acciones para mejorarla.

</aside>

# 🧭 Objetivo

---

> El objetivo del proyecto es desarrollar un sistema de visión por computadora para el análisis de la superficie, con el objetivo de detectar e identificar las emisiones de CO2 y el porcentaje de áreas verdes para la disminución de la contaminación.
> 

# 🔍 Alcance

---

> El sistema estará diseñado para ser utilizado con vehículos aéreos no tripulados (UAV), los cuales se utilizarán para realizar mediciones ambientales de manera estratégica. El sistema deberá ser capaz de detectar y clasificar las emisiones de CO2 y las áreas verdes, con una precisión de al menos el 90%.
> 

---

# SOFTWARE

Utilizar un sensor de imagen de alta resolución para la captura de imágenes de la superficie.

Implementar algoritmos de visión por computadora para la detección y clasificación de emisiones de CO2 y áreas verdes

Dentro del sistema se ve efectuada segmentación para la detección por partes del entorno

A continuación, fragmentos de código en el cual se muestran los diferentes filtros utilizados: 

```python
# Aplicar umbral adaptativo en escala de grises
gray = cv2.cvtColor(media, cv2.COLOR_BGR2GRAY)
_, bordes = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#Deteccion de Color Verde en diferentes rangos
mascara_verde1 = cv2.inRange(imagen_hsv, verde_bajo1, verde_alto1)
mascara_verde2 = cv2.inRange(imagen_hsv, verde_bajo2, verde_alto2)

#Filtro de modo GAusiano
gauss = cv2.GaussianBlur(resultado, (5, 5), 0)
cv2.imshow("Gausiano", gauss)

#Filtro Blur
media = cv2.medianBlur(gauss, ksize=5);
cv2.imshow("media", media)

# Aplicacion umbral adaptativo en escala de grises
gray = cv2.cvtColor(media, cv2.COLOR_BGR2GRAY)
_, bordes = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Encontrar contornos en la imagen de bordes
(contornos, _) = cv2.findContours(bordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filtrar contornos pequeños (áreas irrelevantes)
contornos_filtrados = [contorno for contorno in contornos if cv2.contourArea(contorno) > 100]
```

Cada Filtro aplicado se desarrolló dentro de rango y especificaciones para la detección de las áreas verdes dentro de un rango: 

![maps1.png](ECOVISION%20cae6d17e550b4d7381dcc6162fec11d7/maps1.png)

![Gausiano1.png](ECOVISION%20cae6d17e550b4d7381dcc6162fec11d7/Gausiano1.png)

![areas.png](ECOVISION%20cae6d17e550b4d7381dcc6162fec11d7/areas.png)

La primera captura es la imagen original en la siguiente se ve la detección de las áreas verdes y al final  se ve aplicado la generacion de bordes al espacio ya filtrado.