#=====================================
# POGRAMACION ORIENTADA A OBJETOS 
#=====================================

#=====================================
# Una clase para un objeto vacio
# no esta tan vacio, necesita
# la palabra pass = pasar 
#=====================================
class ObjetoVacio:
    pass
#=====================================
# nada es un ojeto vacio
#=====================================
nada = ObjetoVacio()
print(type(nada))

#==============================
# Clase llanta
#==============================
class Llanta:
    #=======================================
    # Variable cuenta es de toda la clase
    #=======================================
    cuenta = 0
    #=======================================
    # Funcion contructora de identidad 
    # __init__ es una funciñon reservada
    # comienza con uno mismo
    # pero puede ser otro nombre (mi) 
    # parametros de entrada = default
    #========================================
    def __init__(mi,radio=50,ancho=30,presion=1.5):
        # variable de la estructrura completa Llanta
        Llanta.cuenta += 1 
        # variables exclusivas de cada objeto 
        mi.radio = radio
        mi.ancho = ancho
        mi.presion = presion

#====================================
# Objetos (instanciados)
#====================================
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presion=1.2)
llanta3 = Llanta()
llanta4 = Llanta(40,30,1.6)

#====================================
# Objeto que contiene otros objetos
#====================================
class Coche:
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3 
        mi.llanta4 = ll4
        
micoche = Coche(llanta1,llanta2,llanta3,llanta4)

print("Total de llantas: ",Llanta.cuenta) # Variable global de la clase
print("Presion de la llanta 4 = " ,llanta4.presion) #Presion de la llanta 4
print("Radio de la llanta 4 = ",llanta4.radio)
print("Radio de la llanta 3 = ",llanta3.radio)
print("Presion de la llanta 1 de mi coche = ", micoche.llanta1.presion)

#==========================
# Encapsulamiento
#==========================

#========================================
# Uso de la funcion de python propety para poner y obtener atributos
#=========================================================================
class Estudiante:
    def __init__(mi):
        mi.__nombre = ''
    def ponerme_nombre(mi,nombre):
        print('se llamo a ponerme_nombre')
        mi.nombre = nombre
    def obtener_nombre(mi):
        print('se llamo a obtener nombre')
        return mi.__nombre
    nombre=property(obtener_nombre,ponerme_nombre)

#===================================================
# Creando objeto estudiante sin nombre
#===================================================
estudiante = Estudiante()

#=======================================================================
# Ponerle nombre usando la propiedad nombre y el metodo ponerme_nombre
# (sin tener que llamar explicitamente la funcion)
#========================================================================
estudiante.nombre = "Diego"

#========================================================================
# Obtener el nombre con el metodo obtener_nombre
# __nombre es una variable encapsulada (no visible desde fuera)
# (sin tener que llamar explicitamente a la fucion obtener_nombre)
#========================================================================
print(estudiante.nombre)

# Esto no es una funciona
# print(estudiante.__nombre)

#==========================
# Herencia de clases 
#==========================
class Cuadrilatero: 
    def __init__(mi, a, b, c, d):
        mi.lado1=a
        mi.lado2=b
        mi.lado3=c
        mi.lado4=d

    def perimetro(mi):
        p=mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4
        print("perimetro=" ,p)
        return p

#==========================================
# Su hijo rectangulo
# Rectangulo es hijo de Cuadrilatero
# Rectangulo(Cuadrilatero)
#==========================================
class Rectangulo(Cuadrilatero):
    def __inti__(self, a, b):
        #===================================
        # Constructor de su madre
        #===================================
        super().__init__(a, b, c, d)

#=========================
# Su hijo Cuadrilatero
# Hijo de Rectangulo 
#=========================
class Cuadrilatero(Rectangulo):
    def __init__(self, a):
        super().__init__(a,a)

    def area(self):
        area = self.lado1**2
        return area
    # def perimetro(self):
    #   p = 4.0*self.lado1
    #   print("perimetro =",p)
    #   return p

#================================
# Crear un cuadrado
#================================
cuadrado1 = Cuadrado(5)

#=======================================================
# Llamar al metodo perimetro de su abuelo Cuadrilatero
#=======================================================
perimetro1 = cuadrado1.perimetro()

#====================================
# Llamar a su propio metodo area
#====================================
area1 = cuadrado1.area()

print("Perimetro = ", perimetro1)
print("Area = " , area1)

#========================================================================
# Sobre-escribir un metodo de su madre o abuela o tatarabuela...
# Es volver a definir una funcion ya existente
#========================================================================












  






















