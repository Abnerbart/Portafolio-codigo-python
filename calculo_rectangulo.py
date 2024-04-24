base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

area = base * altura 
perimetro = 2 * base + 2 * altura

def calcular_base_altura(area_perimetro):
    if calcular_base_altura == area:
        return area
    elif calcular_base_altura == perimetro:
        return perimetro
    else:
        print("No existen coincidencias.")

print("El Área es:", area)
print("El perimetro es" , perimetro)
