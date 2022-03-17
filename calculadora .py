class Calculadora:

    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

    def sum(self):
        suma = self.num1 + self.num2
        print("El resultado de la suma es: ", suma)

    def res(self):
        resta = self.num1 - self.num2
        print("El resultado de la resta es: ", resta)

    def multip(self):
        multiplicacion = self.num1 * self.num2
        print("El resultado de la multiplicación es: ", multiplicacion)

    def div(self):
        divicion = self.num1 / self.num2
        print("El resultado de la divición es: ", divicion)
    def poten(self):
        potencia = self.num1 ** self.num2
        print("El resultado de la potencia: ", potencia)

num1 = input('Primer numero: ')
num2 = input('Segundo numero(*Exponente*): ')

calculadora = Calculadora(num1, num2)
calculadora.sum()
calculadora.res()
calculadora.multip()
calculadora.div()
calculadora.poten()
