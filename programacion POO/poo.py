class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print("Hola mi nombre es:", self.nombre)



persona1 = Persona("Ana", 25)
persona2 = Persona("Juan", 40)

persona2.saludar()
