import subprocess
import sys

def consultar(usuario, num_lineas):
    try:

        resultado = subprocess.run(['ps', '-u', usuario], capture_output=True, text=True)
    
        lineas_salida = resultado.stdout.splitlines()[:num_lineas]

        with open("procesos_usuario.txt", "w") as archivo_salida:
    
            for linea in lineas_salida:
                archivo_salida.write(linea + "\n")

        print(f"Se ha guardado las primeras lineas {num_lineas} líneas de los procesos del usuario {usuario} en procesos_usuario.txt.")
    
    except subprocess.CalledProcessError as e:
        print("Error:", e.output.strip())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python programa.py  <usuario> <cantidad_de_lineas>")
        sys.exit(1)

    usuario = sys.argv[1]
    num_lineas = int(sys.argv[2])

    consultar(usuario, num_lineas)
