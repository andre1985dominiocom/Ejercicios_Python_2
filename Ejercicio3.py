#Imprimir título
print("Programa para registrar rango de calificaciones:")
#Función para asignar la calificación literal
def Asignar_Calificacion(Calificacion):
    if 9.1<=Calificacion<=10:
        return "A-Excelente:"
    elif 8.1<=Calificacion<=9:
        return "A-Muy bien:"
    elif 7.5<=Calificacion<=8:
        return "A-Bien:"
    else:
        return "NA-No Aprobado:"
#Leer la calificación numérica
Calificacion=float(input("Introduce la calificación numérica:"))
#Obtener la calificación literal
Calificacion_Literal=Asignar_Calificacion(Calificacion)
#Imprimir la calificación literal
print("La calificación literal es:")
Excelente=float(input("Ingrese la calificación:"))
Muy_Bien=float(input("Ingrese la calificación:"))
Bien=float(input("Ingrese la calificación:"))
No_Aprobado=float(input("Ingrese la calificación:"))
if Excelente>9.1 and 10:
  print("Mostrar A")
elif Muy_Bien>8.1 and 9:
  print("Mostrar A")
elif Bien>7.5 and 8:
  print("Mostrar A")
else:
  print("Mostrar No Aprobado")
#El programa solo muestra la califiación como resultado A