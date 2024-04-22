#Calcule los días que faltan para día de muertos y navidad
from datetime import date
año=int(input("Ingrese el año actual: "))
mes=int(input("Ingrese el mes actual: "))
dia=int(input("Ingrese el día actual: "))
fecha_hoy=date(año, mes,dia)
fecha_día_muertos= date(2024,11,2)
fecha_navidad=date(2024,12,24)

resta1=fecha_día_muertos-fecha_hoy
resta2=fecha_navidad-fecha_hoy

print("Para que sea día de los muertos faltan", resta1.days, "días")
print("Para que sea navidad faltan", resta2.days, "días")