class Vehiculo:
    color = None
    ruedas = None
    puertas = None


class Coche(Vehiculo):
    velocidad = None
    cilindrada = None


miCoche = Coche()
miCoche.color = "verde"
miCoche.ruedas = 4
miCoche.puertas = 2
miCoche.velocidad = 210
miCoche.cilindrada = 2200

print("Mi Coche:")
print("Color:", miCoche.color)
print("Ruedas:", miCoche.ruedas)
print("Puertas:", miCoche.puertas)
print("Velocidad Max:", miCoche.velocidad, " Km/h")
print("Cilindrada:", miCoche.cilindrada, "cc")
