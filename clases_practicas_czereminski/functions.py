# 1. Programar una función que tome una lista y devuelva True si está ordenada de mayor a menor o False si no.

def esta_ordenada(l):
	pass

# 2. Programar una función que calcule el producto interno entre dos vectores
# (en este caso pensados como dos listas de números).

def producto_interno(l1,l2):
	pass


# 3. Programar una función que calcule la media de una lista de números.

def media(l):
	pass

# 4. Programar una función que calcule la varianza de una lista de números.
# (Hint: reutilizar la función 3).

def varianza(l):
	pass

# 5. Cada uno de los elementos de cierta lista L será el divisor de un parámetro
# en una prueba de laboratorio. Esta lista surgió de un experimento en el que 
# hubo errores que arrojaron valores igual a 0.
# A modo de anular estos errores (y evitar el error NaN) se podría reemplazar
# los 0 de la lista por un número enorme.
# Crear una función que recorra la lista L y reemplace el valor 
# "antiguo" por el valor "nuevo" y retorne la lista con los valores reemplazados

def reemplaza(L,antiguo,nuevo):
	pass

# 6. Programar una función que tome una lista y devuelva True si todos los elementos
# ubicados en posiciones pares son números pares y los ubicados en posiciones impares
# son números impares y False si no ocurre eso.

def pares_impares(l):
	pass

# 7. Programar una función que genere una lista nueva que sea la réplica de
# una existente, pero que no modifique la original.

def duplicar_lista(l):
	pass

# 8. Programar una función que tome una lista y retorne otra en dónde cada
# posición es el doble de la posición original, además, no se debe modificar
# la lista inicial.

def doble_lista(l):
	pass

# 9. Programar una función que tome una lista como parámetro y le sume a cada
# posición un 1. Notar que la lista original debe ser modificada.

def modificar_lista(l):
	pass


print("--- Probando esta_ordenada ---")
A = [9, 5, 4, 3, 2, -8, -9]
B = [8, 5, 4, 2, 8, -1, 0]
print("La lista " + str(A) + " está ordenada de mayor a menor: " + str(esta_ordenada(A)))
print("La lista " + str(B) + " está ordenada de mayor a menor: " + str(esta_ordenada(B)))
print("\n")

print("--- Probando producto_interno ---")
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print("El producto interno de " + str(l1) + " y " + str(l2) + " es: " + str(producto_interno(l1, l2)))
print("\n")

print("--- Probando media ---")
print("La media de " + str(l1) + " es: " + str(media(l1)))
print("La media de " + str(l2) + " es: " + str(media(l2)))
print("\n")

print("--- Probando varianza ---")
print("La varianza de " + str(l1) + " es: " + str(varianza(l1)))
print("La varianza de " + str(l2) + " es: " + str(varianza(l2)))
print("\n")

print("--- Probando reemplaza ---")
antiguo = 0
nuevo = 10000000000
l3 = [1, 4, 0, 9, 8, 9, 0, 0, 0, 9, 8, 7, 3, 4, 5, 3, 0, 3, 5, 6, 7, 0, 7, 6, 0]
print("Lista original: " + str(l3))
reemplaza(l3, antiguo, nuevo)
print("La lista nueva es: " + str(l3))
print("\n")

print("--- Probando pares_impares ---")
l4 = [2, 1, 8, 7, 16, 99]
l5 = [2, 1, 5, 7, 16, 99]
print("Prueba con " + str(l4) + ": " + str(pares_impares(l4)))
print("Prueba con " + str(l5) + ": " + str(pares_impares(l5)))
print("\n")

print("--- Probando duplicar_lista ---")
l8 = duplicar_lista(l1)
print("Lista original l1: " + str(l1))
print("Lista duplicada l8: " + str(l8))
# Para probar que no se modifica la original
if l8 is not None:
    l8.append("MODIFICADO")
print("Modificamos la copia: " + str(l8))
print("La original sigue intacta: " + str(l1))
print("\n")

print("--- Probando doble_lista ---")
l9 = doble_lista(l2)
print("Lista original l2: " + str(l2))
print("Lista con valores dobles l9: " + str(l9))
print("\n")

print("--- Probando modificar_lista ---")
# Usamos l1, que originalmente era [1,2,3]
print("Lista l1 antes de modificar: " + str(l1))
modificar_lista(l1)
print("Lista l1 después de modificar: " + str(l1))
print("\n")