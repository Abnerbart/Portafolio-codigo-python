edad = int(input("Ingrese la edad del usuario: "))

def usuario(edad):
    if edad:
        edad_proyectada = edad + 5
        return edad_proyectada
    else:
        print("No calza la edad")

resultado = usuario(edad)

print("La edad proyectada es de: ", resultado)