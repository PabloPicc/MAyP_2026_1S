def sumar_todos(xs):
    ''' Develve la suma de todos los enteros de la lista xs. '''
    res = 0
    for x in xs:
        res = res + x
    return res

def sumar_positivos(xs):
    ''' Develve la suma de todos los enteros positivos de la lista xs. '''
    res = 0
    for x in xs:
        if x > 0:
            res = res + x
    return res

# Ejemplos para probar las funciones
print(sumar_todos([]))          # 0
print(sumar_todos([1,3,5]))     # 9
print(sumar_todos([1,3,5,-3]))  # 6

print(sumar_positivos([]))          # 0
print(sumar_positivos([7,-2,0,6]))  # 13
print(sumar_positivos([-1,-3,-5]))  # 0
