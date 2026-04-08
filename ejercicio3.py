alumno = {
    "nombre": "Lucía",
    "edad": 21,
    "carrera": "Ciencia de Datos"
}

print(alumno["nombre"])
print(alumno["edad"])

alumno["edad"] = 22

print(alumno["nombre"])
print(alumno["edad"])

alumno["sexo"] = "Femenino"

print(alumno["nombre"])
print(alumno["edad"])
print(alumno["sexo"])

alumno.pop("edad")

