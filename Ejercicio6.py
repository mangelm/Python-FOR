"""
Pediremos al usuario que introduzca
un número entero por teclado , con el
mensaje “introduzca la cantidad de
facturas a acumular”. A continuación el
programa pedirá consecutivamente tantos
importes como se han indicado anteriormente.
Una vez el usuario haya terminado de introducirlos
todos, el programa mostrará por pantalla la
suma total de los importes: “el importe total
es:....”
"""
importe_total = 0
cantidad_facturas = 0
numero = 0

cantidad_facturas = int(input("introdueixi la quantitat de factures a acumular:\n"))

for operaciones in range(cantidad_facturas):    
    numero = float(input("introduce un numero:\n"))
    importe_total += numero
    print("El total de la factura es:",importe_total)

