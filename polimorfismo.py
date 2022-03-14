#polimorfismo
'''
es una repeticion del contructor sobre la clase
'''
class Empleado:
    def __init__(self, nombre, sueldoMensual):
        self.nombre=nombre
        self.sueldoMensual=sueldoMensual
    def calcularSueldoAnual(self):
        sueldo=12*sueldoMensual * (1+1/100)
        print(f'El sueldo anual de {self.nombre}, del Empleado regular, es de{sueldo}')
class Intructor(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual):
class Asistente_academico(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual):
    def calcularSueldoAnual(self):
        sueldo = 12 self.sueldoMensual*(1+4/100)
        print(f'El sueldo anual de {self.nombre}, - asist, Academico, es de {sueldo}')

class Director(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre. sueldoMensual)
    def calcularSueldoAnual(self):
        sueldo = 12* self.sueldoMensual*(1+6/100)
        print(f'El sueldo anual de {self.nombre}, - Director, es de {sueldo}')
