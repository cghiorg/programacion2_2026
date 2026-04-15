provincias = ["Buenos Aires", "Córdoba", "Santa Fe", "Mendoza", "Salta", "Chubut"]

print(provincias[:4])

provincias.insert(1,"La pampa")

print(provincias[:4])

masprovincias = ["Neuquen", "Rio Negro"]

print(masprovincias)

provincias.extend(masprovincias)

print(provincias)

provincias.remove("Chubut")

print(provincias)

ultima = provincias.pop()

print(ultima)

provincias.append("Salta")
provincias.append("Tierra del Fuego")

print(provincias)