
# Creamos la lista que nos pide el ejercicio 2 
lista = [1,2,3,2,4,5,3,6,  1,2,3,4,5,6]

# Se convierte en un conjunto donde eliminanos los duplicados
conjunto = set(lista)

# Se transforma la lista con el codigo list y dentro conjunto
lista = list(conjunto)

# Se imprime en pantalla los resultados de los duplicados elmininados
print(lista)