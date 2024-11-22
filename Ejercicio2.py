#Impimir título
print("Programa para calcular los intereses que se pagan en el banco a los usuarios")
#Función para calcular el interés y el saldo final
def Calcular_Interes(Saldo):
 if Saldo<100000:
#Si el saldo es menor a 100,000, se paga un 3% de interés
  Interes=Saldo*0.03
  Saldo_Final=Saldo+Interes
#Si el saldo es mayor a 100,000, se paga un 4% de interés
 else:
   interes=Saldo*0.04
   Saldo_Final=Saldo+Interes  
   return Saldo_Final, Interes
#Leer el saldo inicial
Saldo=float(input("Introduce el saldo de la cuenta: "))
#Calcular el interés y el saldo final
interes=Calcular_Interes*Saldo
#Imprimir los resultados
print("Saldo final:")
print("Interés pagado:")
Saldo_Final=float(input("Mostrar el saldo final con los intereses:"))
Interes=float(input("Mostrar intereses pagados:"))
if 100000<0.3:
  print("Calcular el interes pagado")
elif 100000>0.4:
  print("Calcular intereses pagados")
  