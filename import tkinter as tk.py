import tkinter as tk

def calcular_promedio():
    try:
        n = int(entry_edades.get())
        suma = 0
        for _ in range(n):
            edad = int(entry_edad.get())
            suma += edad
        promedio = suma / n
        resultado.config(text="El promedio de edades es: {:.2f}".format(promedio))
    except ValueError:
        resultado.config(text="Por favor ingrese un número válido para el número de edades y para cada edad.")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Cálculo de Promedio de Edades")

# Etiqueta y campo de entrada para el número de edades
etiqueta_edades = tk.Label(ventana, text="Ingrese el número de edades:")
etiqueta_edades.pack()
entry_edades = tk.Entry(ventana)
entry_edades.pack()

# Etiqueta y campo de entrada para cada edad
etiqueta_edad = tk.Label(ventana, text="Ingrese cada edad una por una:")
etiqueta_edad.pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

# Botón para calcular el promedio
boton_calcular = tk.Button(ventana, text="Calcular Promedio", command=calcular_promedio)
boton_calcular.pack()

# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

# Ejecutar la ventana
ventana.mainloop()
