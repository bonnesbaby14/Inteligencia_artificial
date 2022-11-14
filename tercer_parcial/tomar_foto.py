
import cv2

# abrir la cámara
cap = cv2.VideoCapture(0)

# establecer dimensiones
cap.set(cv2.CAP_PROP_FRAME_WIDTH,2560) # ancho
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1440) # alto

# Tomar una imagen
ret, frame = cap.read()
# Guardamos la imagen en un archivo
cv2.imwrite('/home/bonnesbaby14/Escritorio/CETI/INTELIGENCIA ARTIFICIAL/tercer_parcial/foto.jpg',frame)
#Liberamos la cámara
cap.release()

cv2.imshow('Imagen',frame)