#Imprimir título
print("Programa para calcular los angulos en grados y radianes:")
import math
#Función para convertir de grados a radianes
def Grados_a_Radianes(Grados):
    return Grados*(math.pi/180)
#Función para convertir de radianes a grados
def Radianes_a_Grados(Radianes):
    return Radianes*(180/math.pi)
#Seleccionar el tipo de conversión
print("Seleccione la conversión que desea realizar:")
print("Primero: Convertir de grados a radianes:")
print("Segundo: Convertir de radianes a grados")
Opcion=int(input("Ingrese su opción 1 o 2:"))
#Solicitar el ángulo y realizar la conversión
if Opcion==1:
    Grados=float(input("Ingrese el ángulo en grados:"))
    Radianes=Grados_a_Radianes(Grados)
    print("Grados equivalen a radianes.")
elif Opcion==2:
    Radianes=float(input("Ingrese el ángulo en radianes:"))
    grados=Radianes_a_Grados(Radianes)
    print("Radianes equivalen a grados.")
else:
    print("Opción no válida. Por favor, elija 1 o 2.")
