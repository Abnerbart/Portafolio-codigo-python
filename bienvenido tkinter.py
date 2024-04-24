# se importa tkinter para mostrar en la interfaz gráfica.......
import tkinter as tk

root = tk.Tk()

mensaje = tk.Label(root, text="Bienvenido!")
mensaje.pack()

root.mainloop()
