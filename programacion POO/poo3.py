class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, monto):
        self.__saldo += monto

    def ver_saldo(self):
        return self.__saldo
    
    
cuenta1 = CuentaBancaria("Juan", 50000)

print(cuenta1.titular)

print(cuenta1.ver_saldo())

cuenta1.depositar(10000)

print(cuenta1.ver_saldo())

cuenta1.ver_saldo()