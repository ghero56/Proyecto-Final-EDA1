import os
from random import randint
import Fun
import FTR
import Save
import Datos
import MenuFTR
import Menu

Mas = 'Y'
NumPro = 0


MorPro = False
Orden = 'N'
if(FirstTimeRunnig):
    MenuFTR
else:
    #contras = input("\nIngresa tu contraseña para continuar\n\t->")#comprobacion de indentidad
    #if (contras == contraseña):#se abre el archivo y se accede al sistema
    stuff = open("Stuff.txt","r")
    Readable = stuff.readlines()
    os.system('cls')
    [print(i.split('\t')[0]) for i in Readable]

    #else:
        #print("Contraseña incorrecta\n\tSaliendo del programa...")#salir del programa
    stuff.close()
