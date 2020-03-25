import Main

comprobar = open("cache.txt","r") # abrimos el archivo cache para comprobar
# la cantidad de veces que se ha abierto el programa

aux = str(comprobar.readlines) # leemos y lo mandamos a una variable

if(aux == "1"):
    FirstTimeRunnig = False
else:
    FirstTimeRunnig = True
