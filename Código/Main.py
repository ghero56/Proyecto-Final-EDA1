import os
from tkinter import ttk
from tkinter import *

import Base

class Productos:

    def LlenarArbol(self): # funcion para actualizar la tabla
        # para limpiar el arbol
        residual = self.tabla.get_children()
        for i in residual:
            self.tabla.delete(i)

        # conexión y consulta
        Llenar = Base.read()
        for datos in Llenar:
            self.tabla.insert("",0,text=datos[1],values=datos[2]) # se mandan los datos a la interfaz

    def LlenarBase(self): # funcion para llenar la base
        if(len(self.Nombre.get()) !=0 and len(self.Precio.get()) !=0):
            Parametros = (self.Nombre.get(), self.Precio.get())
            Base.add(Parametros) # funcion para conectar y ejecutar
            self.Mensaje['text']='Producto {} añadido correctamente'.format((self.Nombre.get()).title())
            self.Nombre.delete(0,END)
            self.Precio.delete(0,END)
        else:
            self.Mensaje['text']='Datos Faltantes'
        self.LlenarArbol() # mandamos llamar la funcion par aactualizar la pantalla

    def BorrarProd(self):
        self.Mensaje['text']=''
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.Mensaje['text'] = 'Selecciona un dato'
            return
        self.Mensaje['text']=''
        parametro = self.tabla.item(self.tabla.selection())['text']
        Base.remove(parametro)
        self.Mensaje['text'] = 'Artículo {} eliminado correctamente'.format(parametro)
        self.LlenarArbol()

    def EditarProd(self):
        self.Mensaje['text']=''
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.Mensaje['text'] = 'Selecciona un dato'
            return
        self.Mensaje['text']=''
        n = self.tabla.item(self.tabla.selection())['text']
        p = self.tabla.item(self.tabla.selection())['values'][0]
        self.edicion = Toplevel() # ventana encima de la anterior
        self.edicion.title="Edición de productos"
        # nombre anterior
        Label(
            self.edicion,
            text='Nombre Actual'
        ).grid(
            row=0,
            column=1
        )
        Entry(
            self.edicion,
            textvariable=StringVar(self.edicion,value=n),
            state='readonly'
        ).grid(
            row=0,
            column=2
        )
        # nuevo nombre
        Label(
            self.edicion,
            text='Nuevo Nombre'
        ).grid(
            row=1,
            column=1
        )
        nuevoDatoN = Entry(
            self.edicion
        )
        nuevoDatoN.grid(
            row=1,
            column=2
        )
        # precio anterior
        Label(
            self.edicion,
            text='Precio Anterior'
        ).grid(
            row=2,
            column=1
        )
        Entry(
            self.edicion,
            textvariable=StringVar(self.edicion,value=p),
            state='readonly'
        ).grid(
            row=2,
            column=2
        )
        # nuevo precio
        Label(
            self.edicion,text='Nuevo Precio'
        ).grid(
            row=3,
            column=1
        )
        nuevoDatoP=Entry(
            self.edicion
        )
        nuevoDatoP.grid(
            row=3,column=2
        )
        # Base.edit(n,p)
        Button(
            self.edicion,
            text='Actualizar',
            command=lambda:Base.edit(self,nuevoDatoN.get(),nuevoDatoP.get(),n,p)
        ).grid(row=4,column=2,sticky=W)

    def __init__(self,root):
        self.wind = root # se coloca la raiz dentro de un atributo de la clase
        self.wind.title(  # titulo de la ventana
            "Gestión de Productos"
        )

        # contenedor principal
        frame = LabelFrame(
            self.wind, # Frame contenido en wind (root)
            text="Registrar nuevo Producto" # texto a mostrar
        )
        frame.grid( # ubicacion
            row=0, # fila
            column=0, # columna
            columnspan=3, # tamaño de 3 columnas
            pady=20 # espacio vertical
        )

        # label del nombre
        Label(
            frame,
            text='Nombre'
        ).grid(
            row=1,
            column=0
        )
        self.Nombre = Entry(frame)
        self.Nombre.focus()
        self.Nombre.grid(
            row=1,
            column=1
        )

        # label precio
        Label(
            frame,
            text='Precio'
        ).grid(
            row=2,
            column=0
        )
        self.Precio=Entry(frame)
        self.Precio.focus()
        self.Precio.grid(
            row=2,
            column=1
        )

        # boton Guardar
        ttk.Button(
            frame,
            text='Guardar',
            command=lambda:self.LlenarBase()
        ).grid(
            row=3,
            columnspan=2,
            sticky=W+E
        )
        # boton Borrar
        ttk.Button(# estará en la raiz, no lo incluyo al frame
            text='Borrar',
            command=lambda:self.BorrarProd()
        ).grid(
            row=5,
            column=0,
            sticky=W+E
        )
        # boton Editar
        ttk.Button(# estará en la raiz, no lo incluyo al frame
            text='Editar',
            command=lambda:self.EditarProd()
        ).grid(
            row=5,
            column=1,
            sticky=W+E
        )

        # notificación
        self.Mensaje = Label(
            text='',
            fg='red'
        )
        self.Mensaje.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky=W+E
        )

        # arbol de productos
        self.tabla = ttk.Treeview(
            height=10,
            columns=2
        )
        self.tabla.grid(
            row=4,
            column=0,
            columnspan=2
        )
        self.tabla.heading(
            '#0',
            text='NOMBRE',
            anchor=CENTER
        )
        self.tabla.heading(
            '#1',
            text='PRECIO',
            anchor=CENTER
        )
        self.LlenarArbol() # llenar el arbol anterior

def iniciar():
    root = Tk()
    Productos(root) # se instancia la pantalla principal
    root.mainloop()
    os.system('cls')

'''Barramenu = Menu(root)
root.config(menu=Barramenu)

archivoMenu=Menu(Barramenu)
edicionMenu=Menu(Barramenu)
herramientasMenu=Menu(Barramenu)
ayudaMenu=Menu(Barramenu)

Barramenu.add_cascade(label='Archivo',menu=archivoMenu)
Barramenu.add_cascade(label='Edición',menu=edicionMenu)
Barramenu.add_cascade(label='Herramientas',menu=herramientasMenu)
Barramenu.add_cascade(label='Ayuda',menu=ayudaMenu)'''
