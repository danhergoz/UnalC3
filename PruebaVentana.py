#Prueba de Interfaz gráfica
from tkinter import *

raiz=Tk()

raiz.title("Ventana de Pruebas")
raiz.resizable(True,True)

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1)

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1)

cuadroTelefono=Entry(miFrame)
cuadroTelefono.grid(row=2, column=1)

labelNombre=Label(miFrame, text="Nombre")
labelNombre.grid(row=0, column=0, sticky="e", padx=10, pady=10)

labelApellido=Label(miFrame, text="Apellido")
labelApellido.grid(row=1, column=0, sticky="e", padx=10, pady=10)

labelTelefono=Label(miFrame, text="Telefono")
labelTelefono.grid(row=2, column=0, sticky="e", padx=10, pady=10)

raiz.mainloop()

