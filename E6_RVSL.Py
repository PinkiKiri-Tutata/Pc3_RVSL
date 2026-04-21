#Raymundo Valentino Solorzano Larios
#Condicionales en python
# Programa para diagnostico rapido de computadora
# Solicitamos al usuariop si la computadora enciende
encendido = input("La computadora enciende? (Si/no): ")

# Solicitamos si escucha algun pitido al encender
pitido = input("Escuchas algun pitido al encender? (Si/no): ")

# Solicitamos si el monitor muestra imagen
imagen = input("El monitor muestra imagen (Si/no)")

# Evaluamos si la computadora no enciende
if encendido == "no":
    print("Diagnostico: Verificar conexion electrica o fuente de poder.")
# Si enciende 
else: 
    # Evaluamos si hay pitidos 
    if pitido == "Si":
        print("Diagnostico: Problema de hardware detectado (Memoria RAM, targeta madre).")
    else:
        # Evaluamos si hay imagen
        if imagen == "si":
            print("Diagnostico: Revisar conexion del monitor o tarjeta de video.")
        else:
            print("Diagnostico: La computadora parece encender correctamente")