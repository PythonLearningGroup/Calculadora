from tkinter import *

# configuracion ventana principal
ventana = Tk()
ventana.geometry("240x240")
ventana.title("CALCULADORA")
ventana.configure(bg="light blue")

# widget de entrada de datos y salida
numero_a = IntVar()
numero_1 = Entry(ventana, textvariable=numero_a, width=18)

numero_b = IntVar()
numero_2 = Entry(ventana, textvariable=numero_b, width=18)

resultado = StringVar()

# definicion funciones botones


def hacer_suma():
    x = float(numero_a.get())
    y = float(numero_b.get())
    suma = x + y
    resultado.set(suma)


def hacer_resta():
    x = float(numero_a.get())
    y = float(numero_b.get())
    resta = x - y
    resultado.set(resta)


def hacer_multiplicacion():
    x = float(numero_a.get())
    y = float(numero_b.get())
    multiplicacion = x * y
    resultado.set(multiplicacion)


def hacer_division():
    x = float(numero_a.get())
    y = float(numero_b.get())
    if y != 0:
        division = x / y
    else:
        division = "ERROR!!!"
    resultado.set(division)


def reset():
    numero_a.set(0)
    numero_b.set(0)
    resultado.set(0)

# botones de comandos

boton_suma = Button(ventana, text="SUMA", command=hacer_suma, width=15)
boton_resta = Button(ventana, text="RESTA", command=hacer_resta, width=15)
boton_multiplicacion = Button(ventana, text="MULTIPLICACION", command=hacer_multiplicacion, width=15)
boton_division = Button(ventana, text="DIVISION", command=hacer_division, width=15)
boton_reset = Button(ventana, text="RESET", command=reset, width=15)
boton_salir = Button(ventana, text="SALIR", command=ventana.quit, width=15)

# salida de datos
res = Label(ventana, textvariable=resultado, bg="yellow", width=15, relief=SUNKEN)

# posicionamiento widgets

Label(ventana, text="", bg="light blue").grid(row=0)
Label(ventana, text="Ingrese primer Valor", bg="light blue").grid(row=1)
numero_1.grid(row=1, column=1)

Label(ventana, text="Ingrese segundo Valor", bg="light blue").grid(row=2)
numero_2.grid(row=2, column=1)

Label(ventana, text="", bg="light blue").grid(row=3)

boton_suma.grid(row=4, column=0)
boton_resta.grid(row=4, column=1)
boton_multiplicacion.grid(row=5, column=0)
boton_division.grid(row=5, column=1)

ventana.mainloop()
