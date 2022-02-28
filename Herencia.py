#HERENCIA

class Animal:
	pass
	def __init__(self, nombre, tipo):
		self.nombre = nombre
		self.tipo = tipo

	#metodo
	def descripcion(self):
		return 'Este animal es {}'.format(self.nombre, self.tipo)

#clase subclase
class Perro(Animal):
	def sonido(self,tipoSonido):
		return '{} todo el tiempo {}'.format(self.nombre, tipoSonido)

class Gato:
	def sonido(self,tipoSonido):
		return '{} todo el tiempo {}'.format(self.nombre, tipoSonido)

#OBJETO
nuevoAnimal = Perro('firulays', 'ladra')
print(nuevoAnimal.descripcion())
print(nuevoAnimal.sonido('Ladra'))

otroAnimal = Perro('rex', 'sabueso')
print(otroAnimal.descripcion())
print(otroAnimal.sonido('aulla'))

animalito = Gato('Minina', 'Persa')
print(animalito.descripcion())
print(animalito.sonido('Maulla'))
