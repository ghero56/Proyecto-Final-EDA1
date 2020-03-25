import Main # importamos Main
import Caesar # importacion del cifrado

# archivo cache
RES = open("cache.txt","w") # se abre en modo escritura
RES.writelines("1\n") # se escribe el valor 1 para comprobar en otros metodos
RES.close() # cerramos el archivo (ya no es necesario) para liberar memoria

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
RES.close()
datos.close()




#Orden = input('¿Desea ordenarlos por orden alfabetico?\n\n\t(Y/N) -> ').upper()
#if(Orden == 'Y'):
