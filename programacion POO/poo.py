class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print("Hola mi nombre es:", self.nombre, "Tengo", self.edad, "años")
        
    
    def mostrar_edad(self):
        print("Tengo", self.edad, "años")

    def calcular_anio_nacimiento(self, anio_actual):
        anio_nacimiento = anio_actual - self.edad
        print("Nací aproximadamente en el año:", anio_nacimiento)


persona1 = Persona("Ana", 25)
persona2 = Persona("Juan", 40)

persona1.saludar()

persona3 = Persona("Carlos", 55)

persona3.saludar()

persona2.mostrar_edad()

persona3.calcular_anio_nacimiento(2026)

persona1.calcular_anio_nacimiento(2026)