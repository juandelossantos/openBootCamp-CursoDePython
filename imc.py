peso = input("Escriba su peso en kilogramos: ")
altura = input("Escriba su altura en metros (decimales): ")

# Convierto los datos recibidos en números

peso = float(peso);
altura = float(altura)

# Calculo el IMC

imc = peso // (altura * altura)

# Muestro el resultado

print('\n________\nEl IMC de acuerdo con los datos recibidos es: ', imc)
