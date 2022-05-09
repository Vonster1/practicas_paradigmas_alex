#==============================
#  CONJUNTO EN PYTHON
#==============================
even_nums = {2,4,6,8,10}  #Conjunto de numeros pares
print(even_nums)

# El bool no es parte del conjunto
emp = {1,'Alex',10.5,True}  #Conjunto de diferentes objetos 
print(emp)

nums = {1,2,2,3,4,4,5,5}
print(nums)

#=========================================
# Convertir secuancia a numero
# No lo genera en orden
#=========================================
s = set('Hello')
print(s)
s = set((1,2,3,4,5)) #Tupla a conjunto
print(s)

#===============================================
# De diccionario a conjunto: conjunto de llaves
#===============================================
d = {1:'One', 2:'Two'}
s = set(d)
print(s)

s.add(100)
print(s)

s.update(nums)
print(s)

s.remove(100)
print(s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

su = s1|s2 #Union
print(su)
si = s1&s2 #Interseccion
print(si)

sr = s1-s2 
print(sr)

ss = si^s2 #Diferencia simetrica
print(ss)

#================================
# Uso de diccionarios
#================================
capitals = {"USA":"Washington D.C", "France":"Paris", "India":"New Delhi"}
print(capitals)

#=========================================
# llave:valor
#=========================================
#diccionario vacio
d = {}

# Llave entera, valor string
numNames={1:"One", 2:"Two", 3:"Three"}

# Llave real, valor string
decNames={1.5:"One and Half", 2.5:"Two and Half", 3.5:"Three and Half"}

# Llave tupla, valor string
items={("Parker","Reynolds","Camlin"):"pen", ("LG","Whirlpool","Samsung"): "Refrigerator"}

# Llave string, valor int
romanNums = {'I':1, 'II':2, 'III':3, 'IV':3, 'V':5}
print(romanNums)
print(romanNums["I"])

print(capitals.get("India"))
print(capitals.get("india"))

# Reportar llave y valor
for k in capitals:
    print("Key = " + k +", Value = " + capitals[k])

# Nuevo dato del diccionario
capitals["Mexico"] = "CDMX"
print(capitals)

# Borrar dato del diccionario
del capitals["Mexico"]
print(capitals)

# Borrar todo el diccionario
del capitals

# Reportar llaves
print(romanNums.keys())

# Reportar valores
print(romanNums.values())

# Juicio de llave (esta o no esta la llave en el diccionario)
print("I" in romanNums)
print("X" in romanNums)
print("XX" not in romanNums)



























































