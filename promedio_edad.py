n = int(input("Ingrese el numero de edades: "))
x = 1
suma = 0

while x <= n:
    edad = int(input("Ingresa la edad: "))
    suma = suma + edad
    x += 1
print("El promedio de edades es: ", suma/n)