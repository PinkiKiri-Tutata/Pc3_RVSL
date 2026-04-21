#Raymundo Valentino Solorzano Larios
#Condicionales en python
# Programa para clasificar un ticket de soporte

# Solicitamos el área del problema
area = input("¿En qué área es el problema? (software/hardware/red): ").lower()

# Solicitamos la gravedad del problema
gravedad = input("¿Qué tan grave es el problema? (alta/media/baja): ").lower()

# Clasificamos el ticket
if area == "software" and gravedad == "alta":
    print("Ticket: Prioridad crítica. Escalar a desarrolladores senior.")
elif area == "software" and gravedad == "media":
    print("Ticket: Prioridad alta. Resolver en menos de 24 horas.")
elif area == "hardware" and gravedad == "alta":
    print("Ticket: Prioridad crítica. Enviar equipo de reparación.")
elif area == "hardware" and gravedad == "media":
    print("Ticket: Prioridad alta. Evaluación remota.")
elif area == "red" and gravedad == "alta":
    print("Ticket: Prioridad crítica. Escalar a administradores de red.")
elif area == "red" and gravedad == "media":
    print("Ticket: Prioridad alta. Diagnóstico inmediato.")
else:
    print("Ticket: Prioridad normal. Programar revisión en 48 horas.")