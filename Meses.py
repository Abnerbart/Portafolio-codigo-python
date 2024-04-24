# En el global pedidos un número 
e = int(input("Ingresa un número: "))

# Se hacen los calculos de la lista simplemente digitando las fechas y dias
def calcular(n):
    meses_lista = [ "no","Enero, 30 dias", "Febrero, 28 dias", "Marzo, 31 dias", 
        "Abril, 30 dias", "Mayo, 31 dias", "Junio, 30 dias", "Julio, 31 dias",
        "Agosto, 31 dias", "Septiembre, 30 dias", "Octubre, 31 dias", "Noviembre, 30 dias",
        "Diciembre, 31 dias"

]

# Se calcula del uno al doce la lista anterior y luego imprime la fecha con dias establecidos
    if n < 1 or n > 12:
        print(meses_lista[0])
    else:
        print(meses_lista[n])

calcular(e)