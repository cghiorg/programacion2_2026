class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)
        print("Stock:", self.stock)

    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        
        
p1 = Producto("Mouse", 10000, 1)
p2 = Producto("Impresora", 15000, 5)
p3 = Producto("Teclado", 5000, 8)



p1.mostrar_info()
p1.actualizar_stock (10)
p1.mostrar_info()
p1.actualizar_stock(-3)
p1.mostrar_info()        

print("----------------------------")
productos = [p1,p2,p3]

for producto in productos:
    producto.mostrar_info()
