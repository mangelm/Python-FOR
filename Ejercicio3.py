"""
Haga un programa que muestre 
los primeros 1000 números impares
"""
numero = 0

#pongo 2002 porque si es 1000,
#me da los primeros 500 numeros impares
for numero in range(0,2002):
    if numero%2 != 0:
        print(numero)
""" 
for i in range (1, 2002, 2):
    print (i)
""" 
""" 
imp = 1
for i in range(0, 2002):  
    imp+=2
    print(imp)
   
"""
