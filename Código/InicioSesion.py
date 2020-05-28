from tkinter import *
import Main
import Base
import os

# comprobar la existencia de bases de datos
if os.path.isfile("./DataCenter"):
    print("todo bien todo correcto")
else:
    Base.create()

if os.path.isfile("./users"):
    print("y yo que me alegro")
else:
    Base.createOnce()

# función del botón para iniciar
def codigoBoton(obj):
    datos = []
    DatosEnBase = Base.OnlyRead()
    for i in DatosEnBase:
        datos.append(i)
    print(datos)
    if ((obj.User.get() == datos[0][1]) and (obj.Pass.get() == datos[0][2])):
        obj.Raiz.destroy()
        Main.IniciarAlpha()
    elif ((obj.User.get() == datos[1][1]) and (obj.Pass.get() == datos[1][2])):
        obj.Raiz.destroy()
        Main.IniciarBeta()
    elif ((obj.User.get() == datos[2][1]) and (obj.Pass.get() == datos[2][2])):
        obj.Raiz.destroy()
        Main.IniciarGamma()
    else:
        print("\a") # sonido del sistema
        obj.User.delete(0, END) # vaciamos la entrada
        obj.Pass.delete(0, END) # vaciamos la entrada

# clase iniciando
class starting:
    def __init__(self,base):
        # raiz
        self.Raiz = base
        self.Raiz.iconbitmap("./res/Logo.ico")
        self.Raiz.title("Iniciar sesión")

        # Frame Principal
        MainFrame = Frame(self.Raiz)
        MainFrame.grid(row=0,column=0)

        # Clase Imagen
        self.imagen = PhotoImage(file="./res/images.png")

        # Cuadro de Texto del Titulo
        Titulo = Label(MainFrame, text="Iniciar Sesion",font=("Arial",36))
        Titulo.grid(row=0,column=1,columnspan=2)

        # Apartado del Logo
        self.Logo = Label(MainFrame,image=self.imagen)
        self.Logo.grid(row=0,column=0,rowspan=3)

        # Cuadro de Texto Para el Usuario
        Label(MainFrame,text="Usuario: ").grid(row=1,column=1)
        self.User = Entry(MainFrame)
        self.User.grid(row=1,column=2)

        # Cuadro de Texto Para la Contraseña
        Label(MainFrame,text="Contraseña: ").grid(row=2,column=1)
        self.Pass = Entry(MainFrame)
        self.Pass.grid(row=2,column=2)
        self.Pass.config(show="·")

        ContinuarBoton = Button(MainFrame, text="Continuar", command=lambda:codigoBoton(self))
        ContinuarBoton.grid(row=3,column=1)

# comprobar la clase para ejecutar el programa
if __name__ == '__main__':
    base = Tk()
    starting(base) # instanciamos la clase starting
    base.mainloop()
