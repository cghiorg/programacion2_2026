class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Saldo insuficiente")

    def ver_saldo(self):
        return self.__saldo

    def transferir(self, otra_cuenta, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            otra_cuenta.__saldo += monto
            print(self.titular, "le transfirió $", monto, "a", otra_cuenta.titular)
        else:
            print("Saldo insuficiente")


cuenta1 = CuentaBancaria("Juan", 20000)
cuenta2 = CuentaBancaria("Ana", 20000)

print(cuenta1.titular)
print(cuenta1.ver_saldo())

cuenta1.depositar(10000)
print(cuenta1.ver_saldo())

cuenta1.retirar(5000)
print(cuenta1.ver_saldo())

cuenta1.transferir(cuenta2, 2500)

print("Saldo de Juan:", cuenta1.ver_saldo())
print("Saldo de Ana:", cuenta2.ver_saldo())