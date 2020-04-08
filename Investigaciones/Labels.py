# se crean labels para guardar imagenes y texto que no se interactuan en el programa
from tkinter import *

root = Tk() # la clase raiz
root.title("Labels de texto e imagen")

myFrame = Frame(root,width=500, height=400) # clase frame
myFrame.pack()

#***********************************************************#
# clase label de texto
myLabel = Label(myFrame, text="apple") # la primera es el lugar donde estara el label y la segunda son las opciones
myLabel.place(x=300,y=300) # place sirve para poner el texto y no forzar el formato de toda la ventana

# de forma abreviada para no crear variables en memoria
'''
Label(myFrame, text="Texto de ejemplo", fg="red", font=("Arial",12)).place(x=100,y=200)
'''

# label de imagen
myImage = PhotoImage(file="label.png") # clase imagen
Label(myFrame,image=myImage).place(x=1,y=1)
#***********************************************************#

root.mainloop()
