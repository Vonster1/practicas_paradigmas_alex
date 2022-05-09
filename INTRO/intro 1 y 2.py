print("ok")
if 10>5:
    print("verdadero")
    if 10 < 20:
        print("verdadero")
elif 5>3: #comienza el segundo condicional
    print("esto no se imprimira")
else:
    print("aqui nunca llega")
#======================
# FUNCIONES
#======================
def say_hello(name):
    print("Hello ", name)
    print("Welcome to Phyton Tutorials")

say_hello("Alex")
 

''' ESTE ES UN SUPERCOMENTARIO 
    DE INICIO A NUESTRO RESUMEN
'''
#======================
# OPERACIONES BASICAS
#======================
print (2+3)
print (2*3)
print (2/3)
print (2**10)
print (2**0.5)
print (10%2) 
print (10%0.1) #exclusivo en python

#===========================================
# PARA SABER EL TIPO DE OBJETO SE USA TYPE
#===========================================
t=0
print (type(t)) #entero
t=3.6
print (type(t)) #real (flotante)
t=True
print (type(t)) #booleano

#=======================
# MENSAJES EN PANTALLA
#=======================
print ("Este es un comando de Python. ", "Este es otro enunciado.",t)
print ('id: ',1)
print ('First Name: ', 'Alex')
print ('Last Name: ', 'Von')
print ("vamos a sumar esto" + "con esto otro")

#================================================
# CONTINUAR UNA INSTRUCCION EN VARIOS RENGLONES
#================================================
if 100 > 99 and \
        200 <= 300 and \
        True != False:
            print('Hello World')

#========================================
# COMANDOS DIFERENTES EN LA MISMA LINEA
#========================================
print("HOla "); print("tu!!") #Se considera mala practica

#=================================================
# USANDO PARENTESIS REDONDOS, CUDRADOS O LLAVES
# SE PUEDE ESCRIBIR EN VARIOS RENGLONES
#=================================================
matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]
list = [1,2,3,4,5,6,7,8,9]
print(list)
print(matriz)

#=================================================================
# INDENTACION ESTRICTA PARA PROCESOS DEPEDIENTES DE: (DOS PUNTOS)
#=================================================================
# EL CODIGO YA FUE ESCRITO AL PRINCIPIO DEL EDITOR DE TEXTO
#------------------------------------------------------------------------------------------------

#=======================================================
# INPUT PERMITE OBTENER DATOS DEL USUARIO EN PROMPTER
#=======================================================
nombre = input("Dame tu nombre: ")
print("Hola como estas",nombre)

#========================================
# LOS ENTEROS SON DE PRECISION ILIMITADA
#========================================
y = 50000000000000000000000000000000000
print(y)

#==============================================================
# SE PUEDEN DELIMITAR NUMEROS CON GUION BAJO PERO NO CON COMA
#==============================================================
y = 5_000_000
print(y)

#=====================================================
# LA FUNCION int() CAMBIA STRINGS Y FLOATS A ENTEROS
#=====================================================
numero = int(input("Dame tu edad: "))
type(numero)

#====================================================
# LA NOTACION CIENTIFICA DE FLOTANTES UTILIZA e o E
#====================================================
#1.2 x 10^{-9}
#====================================================
y = 1.2E-09
print(y)

#=========================================================
# LA FUNCION float() CONVIERTE STRINGS Y ENTEROS A FLOATS
#=========================================================
y = float("14.3")
print(y)

#======================================================
# LOS COMPLEJOS SE ESCRIBEN CON LA RAIZ DE MENOS UNO 
# j SIEMPRE CON UN NUMERO COMO PREFIJO
# NO ACEPTA LA j SUELTA
#======================================================
z = 1+1j

# suma +
# resta -
# multiplicacion *
# division /
# modulo %
# exponente **
# // funcion piso
# funciones para trsformar numeros int() float() complex()
# operaciones abs() round() pow()

print(round(3.14159,4))

#==========================
# STRINGS DE VARIAS LINEAS
#==========================
parrafo = """ En el bosque de la china
            la chinita se perdio """
print(parrafo)

#===============================================
# LA FUNCION len() OBTIENE EL TAMAÑO DEL STRING
#===============================================
n = len(parrafo)
print(n)

#=============================================================
# LAS LETRAS EN UN STRING OCUPAN LUGARES COMO EN UN ARREGLO
# (TAMBIEN DE ATRAS PARA ADELANTE COMENZANDO EN -1 EL ULTIMO)
#=============================================================
palabra = "hola"
print(palabra[0])
print(palabra[-4])






















































