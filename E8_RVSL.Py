#Raymundo Valentino Solorzano Larios
#Condicionales en python
# Programa para evaluar la seguridad de una contraseña
# Solicitamos la contraseña
contraseña = input("Introduce una contraseña para evaluacion: ")

# Calculamos la longitud de la contraseña
longitud = len(contraseña)

# Verificamos si contiene numeros
contiene_numeros = any(char.isdigit() for char in contraseña)

# Verificamos si contiene mayuslas 
contiene_mayusculas = any(char.isupper() for char in contraseña)

# Evaluamos la seguridad de la contraseña
if longitud >= 12 and contiene_numeros and contiene_mayusculas:
    print("Contraseña fuerte.")
elif longitud >= 8 and (contiene_numeros and contiene_mayusculas):
    print("Contraseña moderada. Recomendado mejorar.")
else: 
    print("Contraseña debil. Cambiar inmediatamente")
# Mostramos detalles
print("longitud de la contraseña: ", longitud)
print("Contiene numeros?:", contiene_numeros)
print("Contiene mayusculas=", contiene_mayusculas)
