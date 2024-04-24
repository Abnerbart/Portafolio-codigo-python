import tkinter as tk

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Mi Ventana")  # Cambiar el título de la ventana

# Crear un cuadrado en el lienzo
canvas = tk.Canvas(ventana, width=200, height=200)  # Tamaño del lienzo
canvas.pack()  # Empaquetar el lienzo en la ventana

# Coordenadas del cuadrado (x1, y1, x2, y2)
x1, y1, x2, y2 = 50, 50, 150, 150

# Crear el cuadrado con relleno azul
canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="blue")

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
