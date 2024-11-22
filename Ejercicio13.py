#Imprimir título
print("Programa para procesar observaciones de la clase de ingles:")
#Función para calcular el porcentaje
def Calcular_Porcentaje(Aprobados, Total):
    return (Aprobados/Total)*100 
if Total>0:
else:0
#Definir variables de los días con niveles
Niveles_Por_Dia=("lunes nivel inicial")
("martes nivel intermedio")
("miércoles nivel avanzado")
("jueves práctica hablada")
("viernes inglés para viajeros")
#Ingresar el dia de la semana
Dia=input("Ingrese el día de la semana:")
#Se muestra el día ingresado
if Dia not in Niveles_Por_Dia:
    print("Error día de la semana inexistente:")
else:
#Mostrar el nivel según el día
    Nivel=Niveles_Por_Dia
    print("Hoy se dicta el nivel:")
#Mostrar si el nivel tiene exámenes
    if Nivel in ("nivel inicial", "nivel intermedio", "nivel avanzado"):
#Ingresar datos sobre exámenes
        Hubo_Examenes=input("¿Se tomaron exámenes hoy? Si/No:")
        if Hubo_Examenes=="Sí":
            Aprobados=int(input("Ingrese la cantidad de alumnos aprobados:"))
            Reprobados=int(input("Ingrese la cantidad de alumnos reprobados:"))
            Total=Aprobados+Reprobados
            Porcentaje_Aprobados=Calcular_Porcentaje(Aprobados, Total)
#Imprimir resultados
            print("Porcentaje de alumnos aprobados:" , Porcentaje_Aprobados)
        else:
            print("No se tomaron exámenes hoy:")
    else:
        print("Este nivel no tiene exámenes:")
#Se produce error en las lineas 6 y 7