import os
# estáticas
DATOS = [['No. Producto','Nombre de Producto','Precio de Producto']]
CON = 'root'

# funciones
#---------------------------------------------------#
def Menu():
    op = input("\n¿Qué deseas hacer?\n\n\t1) Ingresar nuevo producto\n\n\t2) Leer la lista de productos\n\n\t3) Editar datos\n\n\t4) Borrar datos\n\n\t5) Guardar archivo\n\n\t6) salir\n\n\t\t->")
    if op.isdigit():
        if(int(op) == 1):
            Llenar()
        elif(int(op) == 2):
            Leer()
        elif(int(op) == 3):
            Editar(int(op))
        elif(int(op) == 4):
            Editar(int(op))
        elif(int(op) == 5):
            Guardar()
        elif(int(op) == 6):
            print('Hasta Luego\n')
    else:
        os.system('cls')
        enter = input("\n\n\n\n\tintenta nuevamente\n*****************PRESIONA ENTER*****************")
        os.system('cls')
    return op

#---------------------------------------------------#
def Llenar():
    os.system('cls')
    aux = []
    aux.append(len(DATOS))
    for i in range(1,3,1):
        aux.append(input('\nIngresa el {}: '.format(DATOS[0][i])))
    DATOS.append(aux)
    bandera = input("\n\t¿Deseas añadir mas? (Y/N): ")
    if bandera.upper() == 'Y':
        Llenar()
    else:
        ENTER=input("\n\n\n\nProducto(s) Agregado(s) correctamente \n\n\n\t(PRESIONA ENTER PARA CONTINUAR)\n")
        os.system('cls')

#---------------------------------------------------#
def Leer():
    os.system('cls')
    for i in DATOS:
        for j in i:
            print(j," ", end="")
        print("\n")

#---------------------------------------------------#
def OrdenarNum():
    for i in range(len(DATOS)-1,0,-1):
        DATOS[i][0] = i

#---------------------------------------------------#
def Borrar(auxiliar):
    DATOS.pop(auxiliar)
    OrdenarNum()

#---------------------------------------------------#
def Editar(opcion):
    os.system('cls')
    if ( int(opcion) == 3 ):
        print('¿Cuál deseas editar?')
    else:
        print('¿Cuál deseas borrar?')
    for i in range(1,len(DATOS),1):
        print(str(i) + ") " + DATOS[i][1])
    aux = input("\t->")
    if aux.isdigit() :
        aux = int(aux)
        if opcion == 4 :
            Borrar(aux)
            print("Borrado con éxito\n")
        else :
            for i in range(1,3,1):
                DATOS[aux].pop()
                listEdit = input('\nIngresa el {}: '.format(DATOS[0][i]))
                DATOS[aux].insert(i,listEdit)
            bandera = input("\n\t¿Deseas Editar mas? (Y/N): ")
            if bandera.upper() == 'Y':
                Editar(3)
            ENTER = input("\n\n\nProducto(s) Editado(s) correctamente \n\n\n\t(PRESIONA ENTER PARA CONTINUAR)\n")
            os.system('cls')
    else:
        Editar(opcion)

#---------------------------------------------------#
def Guardar():
    os.system('cls')
    residual = open("test.txt","w")
    for i in range(1,len(DATOS),1) :
        for j in DATOS[i]:
            residual.writelines("{}".format(j) + "\t")
        residual.write("\n")
    residual.close()
    print("Guardado")

#---------------------------------------------------#
def Ingresar():
    os.system('cls')
    contraseña = input("\n\n\tIngresa la contraseña de acceso -> ")
    if (contraseña == CON):
        Ban = True
    else:
        os.system('cls')
        Ban = Ingresar()
    return Ban

#---------------------------------------------------#
# main
Bandera = Ingresar()
while(Bandera):
    op = Menu()
    if(op.isdigit()):
        if (int(op) == 6):
            break
