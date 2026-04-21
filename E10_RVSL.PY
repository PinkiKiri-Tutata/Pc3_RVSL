#Raymundo Valentino Solorzano Larios
#Condicionales en python
# Programa para validar elegibilidad para bono

# Solicitamos el nombre del empleado
nombre = input("Introduce tu nombre: ")
# Solicitamos la cantidad de proyectos completados
proyectos = int(input("¿Cuántos proyectos completaste este año? "))
# Solicitamos la cantidad de cursos completados
cursos = int(input("¿Cuántos cursos de formación completaste este año? "))
# Solicitamos si recibió algún reconocimiento
reconocimiento = input("¿Recibiste un reconocimiento oficial? (si/no): ").lower()

# Evaluamos si cumple con los requisitos del bono máximo
if proyectos >= 5 and cursos >= 3 and reconocimiento == "si":
    print(nombre, ", ¡Felicidades! Eres elegible para el bono máximo.")
# Evaluamos si cumple para un bono estándar
elif proyectos >= 3 and cursos >= 2:
    print(nombre, ", Eres elegible para un bono estándar.")
# Evaluamos si al menos completó un proyecto
elif proyectos >= 1:
    print(nombre, ", Recibirás un bono de participación.")
# Si no cumple con ninguno
else:
    print(nombre, ", No calificas para bono este año. ¡Ánimo para la próxima!")