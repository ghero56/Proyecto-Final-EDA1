import os
from random import randint
stuff = []
Mas = 'Y'
NumPro = 0
FirstTimeRunnig = True#cambiar
MorPro = False
Orden = 'N'
if(FirstTimeRunnig):
    FirstTimeRunnig = False
    #print(stuff)
    #Orden = input('¿Desea ordenarlos por orden alfabetico?\n\n\t(Y/N) -> ').upper()
    #if(Orden == 'Y'):
    #    stuff.
    
    #creacion de usuario
    nombre = input("\tDime tu nombre: ")#inicio del programa

    print("\n\n\tbienvenido/a " + nombre.title())#bienvenida
    print("\ntu usuario es: " + nombre.title() + "NET")#usuario

    contraseña = nombre[2].lower() + nombre[0].lower() + nombre[5].upper() + str(randint(0,20))#creacion de la contraseña
    print("\ntu contraseña es: " + contraseña)

    bande = input("\n\tPresiona 'Enter'")#limpiar pantalla
    os.system('cls')

    contras = input("\nIngresa tu contraseña para continuar\n\t->")#comprobacion de indentidad
    if (contras == contraseña):#se abre el archivo y se accede al sistema
        datos = open("Stuff.txt","w")
        while(Mas == 'Y'):
            stuff.append(input("Dime el Producto #"+str(NumPro+1)+"\n"))
            stuff[NumPro] = stuff[NumPro] + "\t" + input("Dime el precio: $")
            datos.writelines(stuff[NumPro])
            Mas = input('¿Desea agregar más?\n\n\t(Y/N) -> ').upper()
            datos.writelines("\n")
            NumPro += 1
        os.system('cls')
        
    else:
        print("Contraseña incorrecta\n\tSaliendo del programa...")#salir del programa
else:
    #contras = input("\nIngresa tu contraseña para continuar\n\t->")#comprobacion de indentidad
    #if (contras == contraseña):#se abre el archivo y se accede al sistema
    stuff = open("Stuff.txt","r")
    Readable = stuff.readlines()
    os.system('cls')
    [print(i.split('\t')[0]) for i in Readable]
    
    #else:
        #print("Contraseña incorrecta\n\tSaliendo del programa...")#salir del programa