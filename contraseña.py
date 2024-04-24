# Verifica si la contraseña cumple con todos los criterios de seguridad
def verificar_contrasena(contrasena):
    
    return (len(contrasena) >= 8 and
            any(c.isupper() for c in contrasena) and
            any(c.islower() for c in contrasena) and
            any(c.isdigit() for c in contrasena) and
            any(c in "!@#$%^&*()\-_=+{};:,<.>" for c in contrasena))

contrasena = input("Ingrese su contraseña: ")
# Luego se verifica la contraseña
if verificar_contrasena(contrasena):
    print("La contraseña es segura.")
else:
    print("La contraseña no cumple con los criterios de seguridad.")
