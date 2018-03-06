import calculadora_cli as calcu
import tkinter as tk
from tkinter import ttk

# #################### configuracion ventana principal #################### #
ventana = tk.Tk()
ventana.title("CALCULADORA")
ventana.resizable(0, 0)
# #################### FRAMES #################### #

parent_frame = ttk.Frame(ventana)
parent_frame.pack_propagate(0)
parent_frame.grid(column=0, row=0)

display_frame = ttk.Frame(parent_frame)
display_frame.grid(column=0, row=0, padx=1, pady=5)

comandos_frame = ttk.Frame(parent_frame)
comandos_frame.grid(column=0, row=1, padx=5, pady=5)

operadores_frame = ttk.Frame(comandos_frame)
operadores_frame.grid(column=1, row=0, padx=5, pady=5)

numeros_frame = ttk.Frame(comandos_frame)
numeros_frame.grid(column=0, row=0, padx=5, pady=5)

unoanueve_frame = ttk.Frame(numeros_frame)
unoanueve_frame.grid(column=0, row=0, padx=5, pady=5)

cero_frame = ttk.Frame(numeros_frame)
cero_frame.grid(column=0, row=9)


# #################### lOGICA ####################

def add(d):
    '''
    Toma el valor que le asigna al parametro d el evento de presionar uno de los botones
    y los inserta en el widget display
    :param d: string datos asignado al presionar un boton.
    '''
    display.insert(99, d)


def calculate(exprecion):
    '''
    Usa el modulo calculadora_cli para evaluar mediante evaluate(exprecion) la exprecion asignada
    :param exprecion:  String a ser evaluada
    '''
    data = calcu.evaluate(exprecion)
    print("data")
    print(data)
    display.delete(0, 98)
    display.insert(99, data)

# #################### WIDGETS #################### #

# DISPLAY
resultado = tk.StringVar()
display = tk.Entry(display_frame, width=30, textvariable=resultado)
display.grid(row=0, column=0)


# botones numeros 1-9

uno = tk.Button(unoanueve_frame, text=1, width=5, height=2, command=lambda: add(1))
uno.grid(row=0, column=0)

dos = tk.Button(unoanueve_frame, text=2, width=5, height=2, command=lambda: add(2))
dos.grid(row=0, column=1)

tres = tk.Button(unoanueve_frame, text=3, width=5, height=2, command=lambda: add(3))
tres.grid(row=0, column=2)

cuatro = tk.Button(unoanueve_frame, text=4, width=5, height=2, command=lambda: add(4))
cuatro.grid(row=1, column=0)

cinco = tk.Button(unoanueve_frame, text=5, width=5, height=2, command=lambda: add(5))
cinco.grid(row=1, column=1)

seis = tk.Button(unoanueve_frame, text=6, width=5, height=2, command=lambda: add(6))
seis.grid(row=1, column=2)

siete = tk.Button(unoanueve_frame, text=7, width=5, height=2, command=lambda: add(7))
siete.grid(row=2, column=0)

ocho = tk.Button(unoanueve_frame, text=8, width=5, height=2, command=lambda: add(8))
ocho.grid(row=2, column=1)

nueve = tk.Button(unoanueve_frame, text=9, width=5, height=2, command=lambda: add(9))
nueve.grid(row=2, column=2)


cero = tk.Button(cero_frame, text=0, width=15, height=2, command=lambda: add(0))
cero.grid(row=0, column=0)


# botones de comandos

mas = tk.Button(operadores_frame, text='+', width=4, command=lambda: add('+'))
mas.grid(row=0, column=1)

menos = tk.Button(operadores_frame, text='-', width=4, command=lambda: add('-'))
menos.grid(row=1, column=1)

por = tk.Button(operadores_frame, text='x', width=4, command=lambda: add('*'))
por.grid(row=2, column=1)

dividido = tk.Button(operadores_frame, text='/', width=4, command=lambda: add('/'))
dividido.grid(row=3, column=1)

igual = tk.Button(operadores_frame, text='=', width=4, command=lambda: calculate(resultado.get()))
igual.grid(row=4, column=1)

reset = tk.Button(operadores_frame, text='C', width=4, command=lambda: display.delete(0, 98))
reset.grid(row=5, column=1)

ventana.mainloop()

