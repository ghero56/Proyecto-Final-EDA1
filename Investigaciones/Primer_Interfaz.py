# se utiliza la libreria Tkinter (por defecto en python)
from tkinter import * # importamos TODO lo contenido en la libreria

'''
# nomenclatura
    clases:
        Tk() -> clase que retorna una raiz
        Frame() -> clase que retorna un frame en un lugar aleatorio (con pack() se introduce en la raiz)
    funciones:
        title() -> para el titulo
        resizable -> (opcional) para permitir cambiar el tamaño de la ventana
        geometry -> indicar el tamaño de la ventana o frame
        config -> funcion con muchas aplicaciones
        mainloop -> loop infinito para la aplicacion
        pack -> ingresa el frame a la raiz
        variables:
            bg = background
            side = lado al que se anclará el frame
            width = anchura del frame dentro de la raiz
            height = altura del frame dentro de la raiz
            anchor = lugar al que quedara anclado el frame (n = norte, s = sur, w = oeste, e = este)
            expand = permite al frame seguir el comportamiento de la raiz
            fill = sigue a la raiz en un eje ("x","y") o ambos ("both")
            cursor = elige el cursor a mostrar dentro de la pantalla
'''

# se crea la raiz del programa
Root = Tk() # variable que contiene a nuestro programa

Root.title("Ventana de pruebas") # añadimos un titulo a nuestro programa

Root.resizable(True , True)# recibe dos datos booleanos para permitir cambiar el tamaño de la ventana (opcional)
'''
Root.iconbitmap("ARCHIVO.ico") # le cambiamos el icono a la aplicacion por uno en disco
'''
Root.geometry("650x350") # ancho y alto de la ventana

Root.config(bg = "black") # funcion que recibe varias opciones, en este caso bg con el nombre en inglés del color de fondo

# se crea el frame (contenedor de widgets) [a su vez un frame es un widget]
main = Frame() # varbiale que contiene el Frame

main.pack(side = "left", anchor = "n" , expand = "True" ) # se llama a la funcion pack para empaquetar el frame en la raiz, el frame modifica su posicion desde esta funcion

# main.pack(fill = "Y")

main.config(width = "200",height = "150",bg = "red") # funcion config nuevamente pero ahora recibe dos nuevos datos (alto y ancho del frame)

main.config(cursor = "hand2") # se cambia el cursor denro del frame ("pirate" es un ejemplo)

main.config(bd = 15) # bd es el ancho y recibe un entero

main.config(relief = "groove") # valor relief recibe el borde

# la instruccion mainloop siempre debe estar en ultimo lugar
Root.mainloop() # llamamos a la funcion mainloop en nuestra clase Tk, bucle infinito par que se ejecute siempre
