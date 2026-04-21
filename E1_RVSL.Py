#Raymundo Valentino Solorzano Larios
#Condicionales en python

# Solicitamos la temperatura al usuario
temperatura = float(input("Introduce la temperatura actual en grados Celcius: "))

if temperatura > 35:
    print("Alerta: CALOR EXTREMO")
elif temperatura >= 26:
    print("Hace calor")
elif temperatura >= 16:
    print("Clima agradable")
elif temperatura >= 6:
    print("Hace frio")
else:
    print("Alerta: FRIO EXTREMO")

    