"""
La serie de Leibniz para calcular
PI es PI= 4*(1/1-1/3+1/5-1/7+1/9..... )
Haga un programa que calcule el valor
de PI, pidiendo previamente por teclado
el número de términos de la serie que
debemos utilizar.
"""

""" 
calculos = int(input("Introduce el numero de cálculos que quieres hacer:\n"))

suma = 0
contador = 1
division = 1

for numero in range(calculos):
    if (contador == 1):
        suma = suma + (1/division)
        contador +=1
    else:
        suma = suma - (1/division)
        contador = 1
    division = division + 2

#suma = suma * (-1)
Pi = 4 * suma

print("El numero pi es: ", Pi) """

""" calculos = int(input("intr. numero de termes de la serie"))
suma=0
boleano=True
divisor = 1
division = 0

for numero in range (calculos):
    if (boleano):
        division =  (1/divisor)        
        boleano = False
    else:
        division =  -1* (1/divisor)      
        boleano = True
    suma = suma + division
    divisor = divisor + 2
#suma = suma * (-1)
Pi = 4 * suma

print ("El numero pi es: ", Pi) """


calculos = int(input("intr. numero de termes de la serie"))

suma=0
boleano=True
divisor=1
division = 0

for numero in range (calculos):
    if (boleano):
        division =  (1/divisor)
    else:
        division =  -1* (1/divisor)
    boleano = not boleano
    suma = suma + division
    divisor = divisor + 2
#suma = suma * (-1)
Pi = 4 * suma

print ("El numero pi es: ", Pi)


