#Calcule el número de días que alguien ha vivido tomando en cuenta su fecha de nacimiento
from datetime import date
año=int(input("Ingrese su año de nacimiento: "))
mes=int(input("Ingrese su mes de nacimiento: "))
dia=int(input("Ingrese su día de nacimiento: "))

fecha_nacimiento=date(año,mes,dia)

año=int(input("Ingrese el año actual: "))
mes=int(input("Ingrese el mes actual: "))
dia=int(input("Ingrese el día actual: "))
fecha_hoy=date(año, mes,dia)

resta=fecha_hoy-fecha_nacimiento

print("Usted ha vivido", resta.days, "días")
