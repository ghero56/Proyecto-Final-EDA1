# entry -> cuadros de texto
from tkinter import *

root = Tk()
root.title("Cuadros de ingreso de texto")

MyFrame = Frame(root, width=600,height=400)
MyFrame.pack()

'''
otro parametro recibe las posiciones de la rosa de los vientos (n,w,e,s)
por ejemplo -> grid(sticky="n")

para tener mayor espacio entre elementos hay dos tipos (padx) y (pady)
reciben la cantidad de pixeles de separacion entre elementos
'''

#***********************************************************#
Cuadro_Nombre = Entry(MyFrame)
# Cuadro_Texto.place(x=100,y=100) # se puede usar place para trabajar con coordenadas
# es mejor trabajar con marcos (grid())
Cuadro_Nombre.grid(row=0,column=1,padx=10,pady=10)
Cuadro_Nombre.config(fg="blue",justify="center")
#***********************************************************#
Label_Nombre = Label(MyFrame,text="Nombre ")
Label_Nombre.grid(row=0,column=0)

# dos cuadros mas para otras cosas
Cuadro_Apellido = Entry(MyFrame)
Cuadro_Apellido.grid(row=1,column=1)
Label_Apellido = Label(MyFrame,text="Apellido ")
Label_Apellido.grid(row=1,column=0)

Cuadro_Edad = Entry(MyFrame)
Cuadro_Edad.grid(row=2,column=1)
Label_Edad = Label(MyFrame,text="Edad")
Label_Edad.grid(row=2,column=0)

# contraseña
Cuadro_Con = Entry(MyFrame)
Cuadro_Con.grid(row=3,column=2)
Cuadro_Con.config(fg="red",show="*") # show="[caracter]" muestra lo que sea y cubre lo que se escriba
Label_Con = Label(MyFrame,text="Password ")
Label_Con.grid(row=3,column=1,sticky="w")

root.mainloop()
