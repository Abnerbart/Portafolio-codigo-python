usuario = input("Ingresa una palabra: ")

def palindromo(usuario):

    reverse = str(usuario).lower().replace(' ', '')
    print(reverse,reverse[::-1])
    if reverse == reverse [::-1]:
        return True
    else:
        return False
        
print(palindromo(usuario))

