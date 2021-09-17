import tkinter as tk
from tkinter import messagebox
from tkinter import colorchooser

def saludar():
    texto = caja_texto.get()
    if texto == '':
        messagebox.showinfo('Saludando', 'Hola Mundo')
    else:
        messagebox.showinfo('Saludando', 'Hola ' + texto)

def colorear():
    color = colorchooser.askcolor()[1]
    frame.config(bg = color)
    label_nombre.config(bg = color)

print("Hola mundo")
print("Hola mundo")
print("Hola mundo")
print("Hola mundo por deiber")
print("Hola mundo (Daniel H)")
print("Hola mundo Oscar")

root = tk.Tk()
root.resizable(0,0)

frame = tk.Frame(root, bg = 'red')
frame.pack()

label_nombre = tk.Label(frame, text = 'Nombre:', bg = 'red')
label_nombre.grid(row = 0, column = 0, padx = 5, pady = 5)

caja_texto = tk.Entry(frame)
caja_texto.grid(row = 0, column = 1, padx = 5, pady = 5)

button1 = tk.Button(frame, text = 'Saludar', command = lambda:saludar())
button1.grid(row = 1, column = 0, padx = 5, pady = 5)

button2 = tk.Button(frame, text = 'Escoje un color', command = lambda:colorear())
button2.grid(row = 1, column = 1, padx = 5, pady = 5)

root.mainloop()