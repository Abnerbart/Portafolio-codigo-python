import tkinter as tk

window = tk.Tk()
window.title("calculo de perimetro y area de rectangulo") # change the title from the window

# create a square in the canvas

canvas = tk.Canvas(window, width=200, height=200) # size the canvas
canvas.pack()

# coordinates the square (x1,y1,x2,y2)
x1, y1, x2, y2 = 50,50,100,100

# creat the square with the blue filling
canvas.create_rectangle(x1,y1,x2,y2, fill="red", outline="blue")

# begin the principal bucle from the grafic interface

window.mainloop()




