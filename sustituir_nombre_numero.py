# En el global almacenaremos las siguientes variables como lista de numero con los cuales se sustituyes por nombres
unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
especiales = {
    10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince",
    16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve"
}

numero = input("Ingrese un número (0 - 150): ")


# Se realizan las siguientes conversiones para sustituir un numero entero por un string
if numero.isdigit():
    numero = int(numero)
    if 0 <= numero <= 150:
        if numero == 0:
            print("cero")
        elif numero < 10:
            print(unidades[numero])
        elif numero < 20:
            print(especiales[numero])
        elif numero < 100:
            if numero % 10 == 0:
                print(decenas[numero // 10])
            else:
                print(decenas[numero // 10] + " y " + unidades[numero % 10])
        elif numero == 100:
            print("cien")
        elif numero < 150:
            if numero % 100 == 0:
                print("ciento " + unidades[numero // 100])
            else:
                print("ciento " + especiales[numero % 100])
    else:
        print("Error: El número debe estar entre 0 y 150")
else:
    print("Error: Ingrese un número válido")
