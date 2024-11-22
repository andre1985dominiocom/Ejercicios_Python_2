#Imprimir título
print("Programa para calcular el costo de los cursos:")
#Función para calcular el costo de los cursos
def Calcular_Pago(Cursos):
    if Cursos<=6 and Cursos>=6:
        Costo_Por_Curso=2000000
    else:
        Costo_Por_Curso=1200000
    return Cursos*Costo_Por_Curso
#Ingresar la cantidad de cursos
Cursos=int(input("Ingrese la cantidad de cursos que lleva el alumno:"))
#Calcular el pago total
Pago_Total=Calcular_Pago(Cursos)
#Imprimir el resultado
print("El costo total de los cursos es:" , Pago_Total)
