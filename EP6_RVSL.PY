#Raymundo Valentino Solorzano Larios
#Condicionales en python

nombre = input("¿Cómo te llamas? ")
Sexito = input("¿Cuál es tu sexo (M o H)? ")
if Sexito == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("Tu grupo es " + grupo)

