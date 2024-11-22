#Imprimir título
print("Programa para calcular las notas de los alumnos:")
#Definir variables
Notas=100-1
Maxima_Nota=100
Contador_Maxima_Nota=0
Rango_a=0
Rango_b=0
Rango_c=0
Rango_d=0
#Ingresar la cantidad de estudiantes
n=int(input("Ingrese la cantidad de alumnos:"))
#Ingresar las notas de los estudiantes, utilizando el bucle for i in white y range
for i in range(n):
    Nota=int(input("Ingrese la nota del alumno n + 1 (1-100):"))
    while Nota<1 and Nota>100:
        print("Nota inválida. Debe estar entre 1 y 100.")
        Nota=int(input("Ingrese la nota del alumno n + 1 1-100:"))
    (Notas)
#Calcular resultados
Nota_Alta=max(Notas)
Nota_Baja=min(Notas)
for Nota in Notas:
    if Nota==Maxima_Nota:
        Contador_Maxima_Nota+=1
    elif 90<=Nota<100:
        Rango_a+=1
    elif 80<=Nota<90:
        Rango_b+=1
    elif 70<=Nota<80:
        Rango_c+=1
    elif 60<=Nota<70:
        Rango_d+=1
#Imprimir resultados
print("Resultados:")
print("Nota más alta:" , Nota_Alta)
print("Nota más baja:" , Nota_Baja)
print("Cantidad de alumnos con la máxima nota (100):" , Maxima_Nota)
print("Cantidad de alumnos en el rango 'a' (90-99):" , Rango_a)
print("Cantidad de alumnos en el rango 'b' (80-89):" , Rango_b)
print("Cantidad de alumnos en el rango 'c' (70-79):" , Rango_c)
print("Cantidad de alumnos en el rango 'd' (60-69):" , Rango_d)
