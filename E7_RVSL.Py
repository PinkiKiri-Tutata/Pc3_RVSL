#Raymundo Valentino Solorzano Larios
#Condicionales en python
#Programa para asignar proyectos segun experiencia y especialidad
#Solicitamos los años de experiencia
anios_experiencia = int(input("Introduce tus años de experiencia en programacion: "))
# Solicitamos el tipo de tecnologia preferida
tecnologia = input("Prefieres trabajar en (Backend/Fronted/Fullstack)? ").lower()
# Evaluamos si el desarrollador es senior (5 años o mas)
if anios_experiencia >= 5:
    senior = True
else:
    senior = False
# Evaluamos la tecnologia y la experiencia para asignar proyecto
if tecnologia == "Backend" and senior:
    print("Proyecto asignado: Microservicios para banca digital.")
elif tecnologia == "Frontend" and senior:
    print("Proyecto asignado: Plataforma de ventas en tiempo real. ")
elif tecnologia == "Fullstack" and senior:
    print("Proyecto asignado: Sistema ERP completo.")
elif tecnologia == "Backend" and not senior:
    print("Proyecto asignado: APIs Basicas para e-commerce.")
elif tecnologia == "Fronted" and senior:
    print("Proyecto asignado: Diseño de landing pages.")
elif tecnologia == "Fullstack" and not senior:
    print("Proyecto asignado: Modulo de autenticacion de usuarios.")
else: 
    print("Error: Tecnologia ingresada no reconocida.")
