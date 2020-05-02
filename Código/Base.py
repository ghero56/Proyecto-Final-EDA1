import sqlite3
import Main

f1 = "CREATE TABLE prod (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,NOMBRE_ARTICULO VARCHAR(50) NOT NULL,PRECIO REAL NOT NULL)"
f2 = "SELECT * FROM prod ORDER BY NOMBRE_ARTICULO DESC"
f3 = "INSERT INTO prod VALUES(NULL, ?, ?)"
f4 = "DELETE FROM prod WHERE NOMBRE_ARTICULO = ?"
f5 = "UPDATE prod SET NOMBRE_ARTICULO = ?, PRECIO = ? WHERE NOMBRE_ARTICULO = ? AND PRECIO = ?"

def create(): # creación única de la tabla
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Cursor.execute(
        f1
    )
    Conexión.close()

def remove(param):
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Cursor.execute(
        f4,(param,)
    )
    Conexión.commit()
    Conexión.close()

def read():
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Datos = Cursor.execute(
        f2
    )
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
