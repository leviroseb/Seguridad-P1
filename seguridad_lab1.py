#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 10:17:43 2021

@author: LEVI
"""

#ALUMNO: Jhon Ismael Flores Pacheco

#%%

import unicodedata

#Ejercicio 1
def sustitucion(texto_plano,texto_cifrado):
    while True:
        letra=texto_plano.read(1)
        if letra=='j' or letra=='h':
            texto_cifrado.write('i')
        elif letra=='ñ':
            texto_cifrado.write('n')
        elif letra=='k':
            texto_cifrado.write('l')
        elif letra=='u' or letra=='w' or letra=='ú':
            texto_cifrado.write('v')
        elif letra=='y':
            texto_cifrado.write('z')
        else:
            texto_cifrado.write(letra)
        if not letra:
            break

#Ejercicio 2
def quitar_tildes(texto_plano,texto_cifrado):
    while True:
        letra=texto_plano.read(1)
        trans = ''.join((c for c in unicodedata.normalize('NFD',letra) if unicodedata.category(c) != 'Mn'))
        
        texto_cifrado.write(trans)
        if not letra:
            break


#Ejercicio 3
def mayusculas(texto_plano,texto_cifrado):
    while True:
        letra=texto_plano.read(1)
        letra_mayuscula=letra.upper()
        texto_cifrado.write(letra_mayuscula)
        if not letra:
            break


#Ejercicio 4
def quitar_signos_espacios(texto_plano,texto_cifrado):
    while True:
        letra=texto_plano.read(1)
        s1="".join(c for c in letra if c.isalnum())
        texto_cifrado.write(s1)
        if not letra:
            break

f=open('heraldos.txt','r',encoding=('utf-8'))
g=open('trans.txt','w',encoding=('utf-8'))
sustitucion(f,g)

f=open('trans.txt','r',encoding=('utf-8'))
g=open('trans2.txt','w',encoding=('utf-8'))
quitar_tildes(f,g)

f=open('trans2.txt','r')
g=open('trans3.txt','w')
mayusculas(f,g)

f=open('trans3.txt','r',encoding=('utf-8'))
g=open('HERALDOSNEGROS_pre.txt','w',encoding=('utf-8'))
quitar_signos_espacios(f,g)
g.close()



# %%

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Ejercicio 5

f=open('HERALDOSNEGROs_pre.txt','r')

def frecuencias(texto_cifrado):
    tabla={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,
    'L':0,'M':0,'N':0,'Ñ':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
    while True:
        letra=texto_cifrado.read(1)
        for clave in tabla:
            if clave==letra:
                tabla[clave]+=1
        if not letra:
            break
    
    z=tabla.copy()

    for i in range (5):
        n=0
        for clave in z:
            if z[clave]>=n:
                n=tabla[clave]
                c=clave
        t=z.pop(c)
        print(c,':',t)
    return tabla

frecuencias(f)

# %%

#Ejercicio 6
f=open('HERALDOSNEGROS_pre.txt','r')

def kasiski(texto_cifrado):
    A=[]
    B=[]
    while True:
        letra=texto_cifrado.read(1)
        A.append(letra)
        if not letra:
            break
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]==A[j] and A[i+1]==A[j+1] and A[i+2]==A[j+2]:
                n=i
                B.append(j-i)
        print((A[n],A[n+1],A[n+2]),B)
    print(len(A))


kasiski(f)


# %%

#Ejercicio 7
f=open('heraldos.txt','r')
g=open('unicode.txt','w',encoding=('utf-8'))

def unicode(texto_plano,texto_cifrado):
    while True:
        letra=texto_plano.read(1)
        texto_cifrado.write(letra)
        if not letra:
            break
    
unicode(f,g)
g.close()


# %%
#Ejercicio 8
f=open('heraldos.txt','r')
g=open('unicode_8230.txt','w',encoding=('utf-32'))

def unicode(texto_plano,texto_cifrado):
    while True:
        letra=texto_plano.read(1)
        texto_cifrado.write(letra)
        if not letra:
            break
    
unicode(f,g)
g.close()
# %%
