#Imprimir título
print("Programa para calcular la seguridad social de un trabajador colombiano:")
#Función para calcular el costo del riesgo laboral
def Calcular_ARL(Clase_Riesgo, Base_Cotizacion):
#Definir porcentajes según la clase de riesgo
    Porcentaje_Riesgo="I: 0.0038"
    "II 0.00435"
    "III 0.00783"
    "IV 0.014"  
# Ingresar el porcentaje correspondiente al riesgo
    Porcentaje=Porcentaje_Riesgo(Clase_Riesgo)
    if Porcentaje:
        print("Error clase de riesgo no válida:")
    return Base_Cotizacion*Porcentaje
#Ingresar datos
Sueldo_Base=float(input("Ingrese el sueldo base del trabajador:"))
Clase_Riesgo=input("Ingrese la clase de riesgo (I, II, III, IV):")
#Calcular el 40% del sueldo base como base de cotización
Base_Cotizacion=Sueldo_Base*0.4
#Calcular valores de EPS, pensión y ARL
EPS=Base_Cotizacion*0.12 
Pension=Base_Cotizacion*0.16
ARL=Calcular_ARL(Clase_Riesgo, Base_Cotizacion) 
#Uso del condicionante 
if ARL:
#Calcular el total a pagar
    Total_Seguridad_Social=EPS+Pension+ARL
#Imprimir resultados
    print("Resumen del Pago de Seguridad Social:")
    print("Sueldo base:" , Sueldo_Base)
    print("Base de cotización 40% del sueldo:" , Base_Cotizacion)
    print("EPS 12%:" , EPS)
    print("Pensión 16%:" , Pension)
    print("ARL Riesgo:" , ARL)
    print("Total a pagar seguridad social:" , Total_Seguridad_Social)
#Problemas con las lineas 11 y 23