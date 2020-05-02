import sqlite3
import Main

f1 = "CREATE TABLE prod (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,NOMBRE_ARTICULO VARCHAR(50) NOT NULL,PRECIO REAL NOT NULL)"
f2 = "SELECT * FROM prod ORDER BY NOMBRE_ARTICULO DESC"
f3 = "INSERT INTO prod VALUES(NULL, ?, ?)"
f4 = "DELETE FROM prod WHERE NOMBRE_ARTICULO = ?"
f5 = "UPDATE prod SET NOMBRE_ARTICULO = ?, PRECIO = ? WHERE NOMBRE_ARTICULO = ? AND PRECIO = ?"

fy = "CREATE TABLE users (Usuario VARCHAR(8), Contrasena VARCHAR(10))"
fx = "SELECT * FROM users"
fz = "INSERT INTO users VALUES(?, ?)"
fc = "UPDATE users SET Usuario = ? WHERE Usuario = ? AND Contrasena = ?"
fu = "UPDATE users SET Contrasena = ? WHERE Usuario = ? AND Contrasena = ?"

def createOnce(): # creación única de la tabla
    Conexión = sqlite3.connect("users")
    Cursor = Conexión.cursor()
    Cursor.execute(fy)
    Conexión.commit()
    Cursor.execute(fz,('fernando','root'))
    Conexión.commit()
    Conexión.close()

def OnlyRead(): # creación única de la tabla
    Conexión = sqlite3.connect("users")
    Cursor = Conexión.cursor()
    comprobante = Cursor.execute(fx)
    for i in comprobante:
        return i
    Conexión.commit()
    Conexión.close()

def CambioContra(tipo,cambios):
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

def create(): # creación única de la tabla
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Cursor.execute(f1)
    Conexión.close()

def remove(param):
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Cursor.execute(
        f4,
        (param,)
    )
    Conexión.commit()
    Conexión.close()

def read():
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Datos = Cursor.execute(f2)
    Conexión.commit()
    return Datos
    Conexión.close()

def add(param):
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Cursor.execute(
        f3,
        param
    )
    Conexión.commit()
    Conexión.close()

def edit(Raiz,N,P,n,p):
    param=(N,P,n,p)
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Cursor.execute(
        f5,
        param
    )
    Conexión.commit()
    Conexión.close()
    Raiz.edicion.destroy()
    Raiz.Mensaje['text'] = 'Artículo {} actualizado correctamente'.format(n)
    Raiz.LlenarArbol()
