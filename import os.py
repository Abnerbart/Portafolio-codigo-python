import os 
import time

def ejecutar_tiempo(comando):
    inicio = time.time()
    os.system(comando)
    fin = time.time()
    tiempo_total = fin - inicio
    print("Tiempo de ejecución:", tiempo_total, "segundos")

archivo_entrada = "file1"
archivo_salida = "file_salida"
palabra = "palabra"

comando = f"grep {palabra} {archivo_entrada} | sort -r | uniq > {archivo_salida}"

ejecutar_tiempo(comando)