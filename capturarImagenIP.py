from PIL import Image
from io import BytesIO
import requests
import os

def capturarImagen(url, usuario, contrasena, nombre):

	try:
		respuesta = requests.get(url, auth= (usuario, contrasena), timeout=10)
		
		if respuesta.status_code == 200:
			imgPil = Image.open(BytesIO(respuesta.content))
			imgPil.save(f'img/{nombre}.jpg', 'JPEG')
			print(f'Imagen guatdada de {nombre}')
		else:
			print('no se pudo capturar la imagen')
	
	except requests.RequestException as e:
		print('Error: ', e)

def main():
	
	urlCamara = 'http://192.168.1.114/doc/page/preview.asp'
	usuarioCamara = 'admin'
	contrasenaCamara = 'Marvic2023'

	if not os.path.exists('img'):
		os.makedirs('img')

	while True:
		print('\nMenu: ')
		print('1- Sacar Foto')
		print('2- Salir')
		
		opcion = input('Seleccione una opcion')

		if opcion == '1':
			capturarImagen(urlCamara, usuarioCamara, contrasenaCamara, 'camaraEntrada')
		else:
			print('Saliendo del programa')
			break

if __name__ == "__main__":
	main()
