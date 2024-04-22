#Calcule el incremento salarial de una persona: Si su salario es menor a 15mil el incremento será del 20% y 
# si es mayor a 15mil el incremento será del 15%
salario=int(input("Ingrese su salario en números: "))
if salario<15000:
    incremento=salario*0.20
    salario=salario+incremento
    print("El incrementos es: ",incremento)
    print("Su salario total es de: ", salario)
else: 
    incremento=salario*0.15
    salario=salario+incremento
    print("El incrementos es: ",incremento)
    print("Su salario total es de: ", salario)