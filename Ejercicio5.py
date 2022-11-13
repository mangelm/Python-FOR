"""
Haga un programa que sume una serie de números desde
del inicio y final variable y un incremento variable.
"""

inicial = int (input("Introduzca número inicial"))
final = int (input("Introduzca número final"))
incremento = int (input("Introduzca incremento"))

for numero in range (inicial, final, incremento):
    print (numero)
""" 
i = 0
numero = 0
ini = 1
fin = 25
inc = 3
for i in range (ini,fin,inc):
    numero = numero + i
    print (numero) 
"""
