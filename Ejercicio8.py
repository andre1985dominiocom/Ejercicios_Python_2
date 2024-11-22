#Imprimir título
print("Programa para seleccionar cantidad de postulantes seleccionados en un equipo:")
#Función para evaluar los requisitos
def Evaluar_Postulante(Edad, Estatura, Peso):
    Requisitos_Cumplidos=0
    if Edad<=19:
        Requisitos_Cumplidos+=1
    if Estatura>175:
        Requisitos_Cumplidos+=1
    if 75<=Peso<=80:
        Requisitos_Cumplidos+=1
    return Requisitos_Cumplidos
#Ingresar datos de los postulantes
Total_Postulantes=int(input("Ingrese la cantidad de postulantes: "))
Pasaron=0
Desaprobaron=0
Cumplieron_Dos_Requisitos=0
#Utilizar bucle for i in y el range
for i in range(Total_Postulantes):
    print("Postulante N + 1:")
    Edad=int(input("Ingrese la edad en años:"))
    Estatura=float(input("Ingrese la estatura en cm:"))
    Peso=float(input("Ingrese el peso en kg:"))
    #Requisitos de postulación
    Requisitos=Evaluar_Postulante(Edad, Estatura, Peso)
    #Resultados de la selección
    if Requisitos==3:
        Pasaron+=1
    elif Requisitos==2:
        Cumplieron_Dos_Requisitos+=1
        Desaprobaron+=1 
    else:
        Desaprobaron+=1
#Imprimir los resultados
print("Resultados finales:")
print("Cantidad de alumnos que pasaron:" , Pasaron)
print("Cantidad de alumnos que desaprobaron:" , Desaprobaron)
print("Cantidad de alumnos que cumplieron dos de los requisitos:", Cumplieron_Dos_Requisitos)
#Programa cumple con las especificaciones solicitas