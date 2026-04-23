#Raymundo Valentino Solorzano Larios
#Condicionales en python

edad = int(input("¿Cuál es tu edad? "))
tributar  = float(input("¿Cuales son tus ingresos mensuales? "))
if edad > 16 and tributar  >= 1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")