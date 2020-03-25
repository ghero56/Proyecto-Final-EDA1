import os

abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

cifrador = ['H','Ñ','$','%','&','(',')','@','?','=','-',':','_','¡','!','"',';',',','.','*','+','{',']','[','}','<','/']

def cifrado_caesar(palabra , abecedario, cifrador):
    cifrado = ''
    for i in palabra:
        for j in range(0,len(abecedario),1):
            if(i == abecedario[j]):
                cifrado = cifrado + cifrador[j]
    return cifrado

def descifrado_caesar(palabra , abecedario , cifrador):
    descifrado = ''
    for i in palabra:
        for j in range(0,len(cifrador),):
            if(i == cifrador[j]):
                descifrado = descifrado + abecedario[j]
    return descifrado
