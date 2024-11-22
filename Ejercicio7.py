#Imprimir título
print("Programa para seleccionar jugadores para un equipo de baloncesto:")
#Función para determinar si el postulante es apto
def Evaluar_Postulante(Edad, Estatura, Peso):
    if Edad<=19 and Estatura>175 and 75<=Peso<=80:
        return "El postulante cumple con los requisitos para el equipo de baloncesto:"
    else:
        return "El postulante no cumple con los requisitos para el equipo de baloncesto:"
#Solicitar los datos del postulante
print("Evaluación para el equipo de baloncesto:")
Edad=int(input("Ingrese la edad del postulante en años:"))
Estatura=float(input("Ingrese la estatura del postulante (en cm): "))
Peso=float(input("Ingrese el peso del postulante (en kg): "))
#Evaluar al postulante
Resultado=Evaluar_Postulante(Edad, Estatura, Peso)
#Imprimir el resultado
print(Resultado)
#Programa cumple con las especificaciones solicitadas