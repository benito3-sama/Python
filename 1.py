canasta = {}
continuar = True
while continuar:
    item = input('Introduce un articulo: ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    canasta[item] = precio
    #para continuar s edebe escribir si
    continuar = input('¿Quieres añadir articulos a la lista (si/no)? ') == "si"
coste = 0
print('Lista de la compra')
for item, precio in canasta.items():
    print(item, '\t', precio)
    coste += precio
print('Coste total: ', coste)
