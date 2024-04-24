import subprocess
import sys

def consultar_procesos(usuario, num_lineas):
    try:
        # Ejecutar el comando ps para obtener los procesos del usuario especificado
        resultado = subprocess.run(['ps', '-u', usuario], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Verificar si hubo algún error
        if resultado.returncode != 0:
            print("Error:", resultado.stderr)
            return

        # Obtener las primeras n líneas de la salida del comando
        lineas_salida = resultado.stdout.splitlines()[:num_lineas]

        # Escribir las líneas en el archivo de salida
        with open("procesos_usuario.txt", "w") as archivo_salida:
            for linea in lineas_salida:
                archivo_salida.write(linea + "\n")

        print(f"Se han guardado las primeras {num_lineas} líneas de los procesos del usuario {usuario} en procesos_usuario.txt.")
    
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python programa.py <usuario> <cantidad_de_lineas>")
        sys.exit(1)

    usuario = sys.argv[1]
    num_lineas = int(sys.argv[2])

    consultar_procesos(usuario, num_lineas)
