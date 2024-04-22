#Encuentre el factorial de cualquier número dado
numero=int(input("Ingrese un número: "))#5
factorial=1
for i in range(1, numero+1):
    factorial*=i 

print("El factorial de" , numero, "es: ", factorial)
