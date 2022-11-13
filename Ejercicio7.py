"""
Haga que el programa anterior muestre
también la media aritmética de los
importes.
"""
importe_total = 0
cantidad_facturas = 0
numero = 0
media = 0

cantidad_facturas = int(input("introdueixi la quantitat de factures a acumular:\n"))

for operaciones in range(cantidad_facturas):    
    numero = float(input("introduce un numero:\n"))
    importe_total += numero
    media = importe_total/cantidad_facturas
    print("El total de la factura es:",importe_total)

print("La media es:",media)

