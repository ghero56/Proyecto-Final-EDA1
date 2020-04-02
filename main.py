import os
# estáticas
DATOS = [['FOLIO','CLIENTE','CONVENIO','CONCEPTO','DEUDOR','PAGOS FECHADOS','PAGO TOTAL ($)','PAGO PARCIAL ($)','ADEUDO PARCIAL','OBSERVACIONES','DOMICILIO','PROCEDIMIENTO JUDICIAL (Y/N)','JUZGADO','EXPEDIENTE','FECHA DE REQUERIMIENTO','FECHA DE FUERZA PUBLICA','EMBARGO','FECHA DE SENTENCIA']]
CON = 'root'

# funciones
def Menu():
    op = int(input("\n¿Qué deseas hacer?\n\n\t1) Ingresar nuevo deudor\n\n\t2) Leer datos\n\n\t3) Editar datos\n\n\t4) Borrar datos\n\n\t5) Guardar archivo\n\n\t6) salir\n\n\t\t->"))
    if(op == 1):
        Llenar()
    elif(op == 2):
        Leer()
    elif(op == 3):
        Editar()
    elif(op == 4):
        Editar()
    elif(op == 5):
        Guardar()
    elif(op == 6):
        print('Hasta Luego\n')
    else:
        os.system('cls')
        enter = input("intenta nuevamente\n PRESIONA ENTER")
        os.system('cls')
    return op

def Llenar():
    os.system('cls')
    aux = []
    aux.append(len(DATOS))
    for i in range(1,12,1):
        if i < 8:
            aux.append(input("Ingresa el {}: ".format(DATOS[0][i])))
        elif i == 8:
            aux.append(int(aux[6]) - int(aux[7]))
        elif i > 8 and i < 11:
            aux.append(input("Ingresa el {}: ".format(DATOS[0][i])))
        if i == 11:
            aux.append(input("Ingresa el {}: ".format(DATOS[0][i])))
            if(aux[i].upper() == 'Y' or aux[i].upper() == "SI"):
                for j in range(12,18,1):
                    aux.append(input("Ingresa el {}: ".format(DATOS[0][j])))
    DATOS.append(aux)
    print(DATOS)

def Leer():
    os.system('cls')
    for i in DATOS:
        for j in i:
            print(j," ", end="")
        print("\n")

def Editar():
    os.system('cls')
    print('¿Cuál deseas editar?')
    for i in range(1,len(DATOS),1):
        print(str(i) + ") " + DATOS[i][4])
    op = input("\t->")

def Guardar():
    os.system('cls')
    residual = open("test.txt","w")
    for i in DATOS :
        for j in i:
            residual.writelines("{}".format(j) + "\t")
        residual.write("\n")
    residual.close()
    print("Guardado")

def Ingresar():
    os.system('cls')
    contraseña = input("\n\n\tIngresa la contraseña de acceso -> ")
    if (contraseña == CON):
        Ban = True
    else:
        os.system('cls')
        Ban = Ingresar()
    return Ban

# main
Bandera = Ingresar()
while(True):
    op = Menu()
    if (op == 6):
        break
