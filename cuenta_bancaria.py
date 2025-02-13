class CuentaBancaria:

    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial


    def ingresar(self, cantidad):
        self.__saldo += cantidad

    def sacar_dinero(self, cantidad):
        if cantidad > self.__saldo:
            raise ValueError("No hay saldo suficiente")
        self.__saldo -= cantidad

    @property
    def saldo(self):
        return self.__saldo


    def __lt__(self, otra):
        return self.__saldo < otra.__saldo
    

c1 = CuentaBancaria(1000)
c1.ingresar(700)
#c1.saldo -= 2500
#c.sacar_dinero(2500)

c2 = CuentaBancaria(10000)

print(c1.saldo)

if c2 < c1:
    print("c1 tiene más dinero que c2")
else:
    print("Es c2 el que más dinero tiene")
