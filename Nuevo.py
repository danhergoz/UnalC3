import tkinter as tk
from tkinter import messagebox
from tkinter import colorchooser

def saludar():
    messagebox.showinfo('Saludando', 'Hola Mundo')

def colorear():
    color = colorchooser.askcolor()[1]
    frame.config(bg = color)

print("Hola mundo")
print("Hola mundo")
print("Hola mundo")
print("Hola mundo por deiber")
print("Hola mundo (Daniel H)")
print("Hola mundo Oscar")

root = tk.Tk()

frame = tk.Frame(root, bg = 'red')
frame.pack()

button1 = tk.Button(frame, text = 'Saludar', command = lambda:saludar())
button1.grid(row = 0, column = 0, padx = 5, pady = 5)

button2 = tk.Button(frame, text = 'Escoje un color', command = lambda:colorear())
button2.grid(row = 0, column = 1, padx = 5, pady = 5)

root.mainloop()