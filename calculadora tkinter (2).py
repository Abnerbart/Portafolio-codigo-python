# Se importa esta categoria de tkinter para que importe todos los elementos como texto, END, entre otros.

from tkinter import *

expression = ""

# Esta función maneja el evento de presionar un botón numérico en la calculadora.
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

#
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="black")
    gui.title("calculadora")
    gui.geometry("270x300")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(row=0, column=0, columnspan=4, ipadx=70)

    Button1 = Button(gui, text='1', fg='black', bg='red', 
                    command=lambda: press(1), height=1, width=7)
    Button1.grid(row=2, column=0)

    Button2 = Button(gui, text='2', fg='black', bg='red', 
                    command=lambda: press(2), height=1, width=7)
    Button2.grid(row=2, column=1)

    Button3 = Button(gui, text='3', fg='black', bg='red', 
                    command=lambda: press(3), height=1, width=7)
    Button3.grid(row=2, column=2)

    Button4 = Button(gui, text='4', fg='black', bg='red', 
                    command=lambda: press(4), height=1, width=7)
    Button4.grid(row=3, column=0)

    Button5 = Button(gui, text='5', fg='black', bg='red', 
                    command=lambda: press(5), height=1, width=7)
    Button5.grid(row=3, column=1)

    Button6 = Button(gui, text='6', fg='black', bg='red', 
                    command=lambda: press(6), height=1, width=7)
    Button6.grid(row=3, column=2)

    Button7 = Button(gui, text='7', fg='black', bg='red', 
                    command=lambda: press(7), height=1, width=7)
    Button7.grid(row=4, column=0)

    Button8 = Button(gui, text='8', fg='black', bg='red', 
                    command=lambda: press(8), height=1, width=7)
    Button8.grid(row=4, column=1)

    Button9 = Button(gui, text='9', fg='black', bg='red', 
                    command=lambda: press(9), height=1, width=7)
    Button9.grid(row=4, column=2)
    
    Button0 = Button(gui, text='0', fg='black', bg='red', 
                    command=lambda: press(0), height=1, width=7)
    Button0.grid(row=5, column=0)

    plus = Button(gui, text='+', fg='black', bg='red',
                  command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text='-', fg='black', bg='red',
                  command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text='*', fg='black', bg='red',
                  command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text='/', fg='black', bg='red',
                  command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text='=', fg='black', bg='red',
                  command=equalpress, height=1, width=7)
    equal.grid(row=5, column=1)

    clear = Button(gui, text='C', fg='black', bg='red',
                  command=clear, height=1, width=7)
    clear.grid(row=5, column=2)
    
    decimal = Button(gui, text='.', fg='black', bg='red',
                  command=lambda: press("."), height=1, width=7)
    decimal.grid(row=6, column=0)
    
    gui.mainloop()
