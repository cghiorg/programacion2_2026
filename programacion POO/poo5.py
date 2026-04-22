class Perro:
    def hablar(self):
        print("Guau")

class Gato:
    def hablar(self):
        print("Miau")

class humano:
    def hablar(self):
        print("Hola")



animales = [Perro(), Gato(), humano()]
        
for animal in animales:
    animal.hablar()