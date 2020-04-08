# se guarda el archivo en formato pyw (PYthonWindow) para ocultar la consola de comandos
from tkinter import * # importamos TODO lo contenido en la libreria

Root = Tk() # variable que contiene a nuestro programa

Root.title("Ventana de pruebas") # añadimos un titulo a nuestro programa

Root.resizable(True , True)# recibe dos datos booleanos para permitir cambiar el tamaño de la ventana
'''
Root.iconbitmap("ARCHIVO.ico") # le cambiamos el icono a la aplicacion por uno en disco
'''
Root.geometry("650x350") # ancho y alto de la ventana

Root.config(bg = "black") # funcion que recibe varias opciones

# la instruccion mainloop siempre debe estar en ultimo lugar
Root.mainloop() # llamamos a la funcion mainloop en nuestra clase Tk, bucle infinito par que se ejecute siempre
