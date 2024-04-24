# Se llama a la función bisiesto por un if con el cual se determina los años bisiestos con los booleanos a continuación.
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

anio_nacimiento = int(input("Ingrese su año de nacimiento: "))

if es_bisiesto(anio_nacimiento):
    print(f"¡El año {anio_nacimiento} es bisiesto!")
else:
    print(f"El año {anio_nacimiento} no es bisiesto.")
