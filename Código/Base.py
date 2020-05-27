import sqlite3
import Main

# funciones para la base de productos
f1 = "CREATE TABLE products (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,NOMBRE_ARTICULO VARCHAR(50) NOT NULL,PRECIO REAL NOT NULL)"
f2 = "SELECT * FROM products ORDER BY NOMBRE_ARTICULO DESC"
f3 = "INSERT INTO products VALUES(NULL, ?, ?)"
f4 = "DELETE FROM products WHERE NOMBRE_ARTICULO = ?"
f5 = "UPDATE products SET NOMBRE_ARTICULO = ?, PRECIO = ? WHERE NOMBRE_ARTICULO = ? AND PRECIO = ?"

# funciones para la base de usuarios
fy = "CREATE TABLE users (Usuario VARCHAR(8), Contrasena VARCHAR(10))"
fx = "SELECT * FROM users"
fz = "INSERT INTO users VALUES(?, ?)"
fc = "UPDATE users SET Usuario = ? WHERE Usuario = ? AND Contrasena = ?"
fu = "UPDATE users SET Contrasena = ? WHERE Usuario = ? AND Contrasena = ?"

def createOnce(): # creación única de la tabla usuarios
    Conexión = sqlite3.connect("users")
    Cursor = Conexión.cursor()
    Cursor.execute(fy)
    Conexión.commit()
    Cursor.execute(fz,('root','root'))
    Conexión.commit()
    Conexión.close()

def OnlyRead(): # lectura única de la tabla
    Conexión = sqlite3.connect("users")
    Cursor = Conexión.cursor()
    comprobante = Cursor.execute(fx)
    for i in comprobante:
        return i
    Conexión.commit()
    Conexión.close()

def Cambio_InicioSesion(tipo,cambios): # cambiar usuario/contraseña
    old = OnlyRead()
    list = (cambios,old[0],old[1])
    if tipo == "user":
        Conexión = sqlite3.connect("users")
        Cursor = Conexión.cursor()
        Cursor.execute(fc,list)
        Conexión.commit()
        Conexión.close()
    else:
        Conexión = sqlite3.connect("users")
        Cursor = Conexión.cursor()
        Cursor.execute(fu,list)
        Conexión.commit()
        Conexión.close()

def create(): # creación única de la tabla productos
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Cursor.execute(f1)
    Conexión.close()

def remove(param): # borrar productos
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Cursor.execute(f4,(param,))
    Conexión.commit()
    Conexión.close()

def read(): # lectura de productos
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Datos = Cursor.execute(f2)
    Conexión.commit()
    return Datos
    Conexión.close()

def add(param): # añadir producto
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Cursor.execute(f3,param)
    Conexión.commit()
    Conexión.close()

def edit(Raiz,N,P,n,p): # editar un producto
    if (N and P):
        param = (N,P,n,p)
        Conexión = sqlite3.connect("DataCenter") # nos conectamos
        Cursor = Conexión.cursor() # se crea el cursor para modificar la base
        Cursor.execute(f5,param) # se ejecuta un comando en la base y se mandan los parametros para complementar
        Conexión.commit() # se guardan los cambios en la base
        Conexión.close() # se cierra la conexión a la base de datos
        Raiz.edicion.destroy() # se destruye la ventana
        Raiz.Mensaje['fg'] = 'green'
        Raiz.Mensaje['text'] = 'Artículo {} actualizado correctamente'.format(n)
        Raiz.LlenarArbol()
    else:
        Raiz.edicion.destroy() # se destruye la ventana
        Raiz.Mensaje['fg'] = 'red'
        Raiz.Mensaje['text'] = 'Artículo {} actualizado incorrectamente'.format(n)
