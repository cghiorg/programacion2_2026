class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print("Hola, soy", self.nombre)
        
        
class Alumno(Persona):
    def __init__(self, materia):
        self.materia = materia
        
    def estudiar(self):
        print(self.nombre, "está estudiando")
        
    def que(self):
        print(self.materia, "está estudiando")
        
class Profesor(Persona):
    def clase(self):
        print(self.nombre, "estoy dando clases")
        
        
p1 = Persona("Carlos")

p1.presentarse()
      
a1 = Alumno("Juan", "Programacion")

a1.presentarse()
a1.estudiar()
a1.que

pro1 = Profesor("Pablo")
pro1.clase()