#Imprimir título
print("Programa para máquina expendedora de dulces y realizar devolución de cambio:")
#Función para simular la máquina expendedora
def maquina_expendedora(Monto):
    Costo_Dulce=2000
#Validar el monto ingresado
    if Monto==5000 or Monto==10000:
#Calcular el cambio
        cambio=monto-Costo_Dulce
#Entregar el dulce y el cambio
        return "Dulce entregado. Su cambio es de:"
    else:
#Si el monto no es válido, rechazar
        return "Monto inválido. Por favor, ingrese $5000 o $10000."
#Leer el monto ingresado por el usuario
Monto=int(input("Introduce el monto ingresado $5000 o $10000:"))
#Obtener la respuesta de la máquina
Respuesta=Maquina_Expendedor(Monto)
#Imprimir el resultado
print(Respuesta)

