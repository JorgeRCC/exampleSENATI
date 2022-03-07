#HERENCIA SUPER


class Persona():
    def __init__(self, apePat,):
        self.apellidoPat = apePat
        self.apellidoMat = apeMat
        self.nombres = nom

    #creacion
    def mostarNomb(self):
        mensaje = '\n{0}{1},{}\n'
        return mensaje.format(self.apellidoPat,self.apellidoMat,self.nombres)

class Estudiante(Persona):
    pass
class Intructor(Persona):
    def __init__(self, apePat, apellidoMat, nom, prof):
        super().__init__(apePat,apellidoMat,nom)
        self.profesion = prof

alumno = Estudiante('Flores', 'Zenteno', 'Juan Carlos','informatico')
print(alumno.mostrarNomb(), alumno.profesion)
