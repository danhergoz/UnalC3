import tkinter as tk
from tkinter import messagebox

def saludar():
    messagebox.showinfo('Saludando', 'Hola Mundo')

print("Hola mundo")
print("Hola mundo")
print("Hola mundo")
print("Hola mundo por deiber")
print("Hola mundo (Daniel H)")
print("Hola mundo Oscar")

root = tk.Tk()

frame = tk.Frame(root, bg = 'red')
frame.pack()

button = tk.Button(frame, text = 'Saludar', command = lambda:saludar())
button.pack()

root.mainloop()