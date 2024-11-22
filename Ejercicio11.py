#Imprimir título
print("Programa para ingresar letras:")
#Ingresar las letras del abecedario
Letra=input("Ingrese una letra:")
#Solictar el ingreso de una sola letra
if len(Letra)!=1:
    print("No se puede procesar el dato se debe ingresar un solo carácter.")
else:
#Ingresar solo letras
    Letra=Letra
#Mostrar si es una vocal
    if Letra in "aeiou":
        print("Es vocal:")
    else:
        print("No es una vocal:")
