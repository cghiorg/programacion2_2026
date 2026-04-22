class MetodoPago:
    def pagar(self, monto):
        print("Procesando pago...")
        
class Tarjeta(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando ${monto} con tarjeta (requiere autorización)")
        
class Efectivo(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando ${monto} en efectivo")

class Transferencia(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando ${monto} por transferencia bancaria")
        

pagos = [
    Tarjeta(),
    Efectivo(),
    Transferencia()
]

for metodo in pagos:
    metodo.pagar(10000)