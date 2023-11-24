import cv2

# Dirección RTSP de la cámara Hikvision
rtsp_url = 'rtsp://marvic:Marvic2023@192.168.1.114:545/h264/ch(1)/main/av_stream'
# Reemplaza USUARIO, PASSWORD, IP, PORT y CANAL con tus propias credenciales y detalles de la cámara

# Conectarse a la cámara
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error al conectar a la cámara")
else:
    # Capturar un fotograma
    ret, frame = cap.read()
    if ret:
        # Mostrar la imagen capturada
        cv2.imshow('Captura de cámara', frame)
        
        # Guardar la imagen capturada en un archivo
        cv2.imwrite('captura_camara.jpg', frame)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error al capturar el fotograma")

# Liberar la cámara
cap.release()
