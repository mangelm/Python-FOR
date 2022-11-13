"""
Haga un programa que nos muestre mediante
un rango de números, todos los números
deficientes. Un número deficiente es un
entero positivo o natural donde la suma de
todos sus divisores, menos él mismo,
es menor a ese número. 6 no es deficiente,
por que 1 + 2 + 3 = 6
"""
"""
#Para un solo numero
numero = int(input("introduce el numero para comprobar"))
i = 1
suma = 0

for i in range(numero):
    if (numero%i == 0):
        suma = suma + i
if (numero == suma):
    print("Este numero no es deficiente")
else:
    print("El numero es deficiente")
"""
suma=0
ini= 1
fin = 10
for i in range (ini,fin):
    suma = 0
    for k in range (1,i):
        if (i%k==0) :
            suma = suma+k
    if (suma<i):
        print (i,"el numero es deficiente")

