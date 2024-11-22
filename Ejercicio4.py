#Imprimir título
print("Programa para mostrar el signo zodiacal según el mes de nacimiento:")
#Función para determinar el signo zodiacal
def Obtener_Signo_Zodiacal (Mes, Dia):
#Utilizar condiconates anidados
    if Mes=="Enero":
        if 1<=Dia<=19:
            return "Capricornio"
        else:
            return "Acuario"
    elif Mes=="Febrero":
        if 1<=Dia<=18:
            return "Acuario"
        else:
            return "Piscis"
    elif Mes=="Marzo":
        if 1<=Dia<=20:
            return "Piscis"
        else:
            return "Aries"
    elif Mes=="Abril":
        if 1<=Dia<=19:
            return "Aries"
        else:
            return "Tauro"
    elif Mes=="Mayo":
        if 1<=Dia<=20:
            return "Tauro"
        else:
            return "Géminis"
    elif Mes=="junio":
        if 1<=Dia<=20:
            return "Géminis"
        else:
            return "Cáncer"
    elif Mes=="Julio":
        if 1<=Dia<=22:
            return "Cáncer"
        else:
            return "Leo"
    elif Mes=="Agosto":
        if 1<=Dia<=22:
            return "Leo"
        else:
            return "Virgo"
    elif Mes=="Septiembre":
        if 1<=Dia<=22:
            return "Virgo"
        else:
            return "Libra"
    elif Mes=="Octubre":
        if 1<=Dia<=22:
            return "Libra"
        else:
            return "Escorpio"
    elif Mes=="Noviembre":
        if 1<=Dia<=21:
            return "Escorpio"
        else:
            return "Sagitario"
    elif Mes=="Diciembre":
        if 1<=Dia<=21:
            return "Sagitario"
        else:
            return "Capricornio"
    else:
        return "Mes inválido"
#Leer el mes y el día
Mes=input("Introduce el mes (en minúsculas): ") 
Dia=int(input("Introduce el día del mes: "))
#Obtener el signo zodiacal
Signo=("Obtener_Signo_Zodiacal:" , Mes, Dia)
#Imprimir el signo zodiacal
print("El signo zodiacal es:" , Signo)
#El programa no registra el signo zodiacal