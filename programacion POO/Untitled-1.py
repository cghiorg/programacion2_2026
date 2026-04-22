class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
       
    def venta(self):
         print(f"El vehículo que nos acaba de llegar es marca: {self.marca} y el modelo: {self.modelo}")
       
vehiculo1 = Vehiculo("Audi" ,"A4")        
vehiculo2 = Vehiculo("BMW" ,"M3")  
 
vehiculo1.venta()