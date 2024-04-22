#Te diga si un número es par o impar 
numero=int(input("Ingrese un número: "))
par=numero%2
if par==0:
    print("El número", numero, "es par")
else: 
    print("El número", numero, "es impar")