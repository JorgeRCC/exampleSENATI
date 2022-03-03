#herencia nivel
#clase general
class Dispositivo:
	def __init__(self):
		pass
	def enLlamada(self):
	 	print('llamada en curso')
	def enEspera(self):
	 	print('llamada en espera')
class Imagen:
	def __init__(self):
		pass
	def capturarFoto(self):
		print('Camara activa')
	def enviarFoto(self):
		print('Foto enviada')
class Multimedia:
 	def __init__(self):
 		pass 
 	def capturarVideo(self):
 		print('Video en grabacion')
 	def reproducirMusica(self):
 		print('Escuchar musica')

class EquipoMovil(Dispositivo, Imagen, Multimedia):
	def __del__(self):
		pass
		print('El resto de utilidades detenidas')

smartphone = EquipoMovil()
print(smartphone.reproducirMusica())
