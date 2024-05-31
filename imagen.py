import cv2
#import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
imagen_original = cv2.imread('ruido.png')

# Convertir la imagen a escala de grises si es necesario
if len(imagen_original.shape) == 3:
    imagen_gris = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)
else:
    imagen_gris = imagen_original

# Aplicar el filtro de media para reducir el ruido
ventana_tamano = 3 # Tamaño de la ventana del filtro de media
imagen_filtrada = cv2.medianBlur(imagen_gris, ventana_tamano)

# Mostrar la imagen original y la imagen filtrada
#plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(imagen_gris, cmap='gray')
plt.title('Imagen Original')
plt.subplot(1, 2, 2)
plt.imshow(imagen_filtrada, cmap='gray')
plt.title('Sin Ruido')
plt.show()
