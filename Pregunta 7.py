#Programa que determine si un número es par o impar
numero = int(input("Ingresa un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")