# Ejercicio 1a:
# La función recibe un número n y retorna la suma de los primeros n números naturales.

def suma_n(n):
    pass


# Ejercicio 1b:
# La función recibe un número n e imprime todos los números pares menores o iguales a n.

def pares_hasta_n(n):
	pass

# Ejercicio 2:
# La función recibe una lista de números y retorna:
# - la suma de sus elementos
# - el valor máximo
# (sin usar sum() ni max())

def suma_y_max(lista):
	pass


# Ejercicio 3:
# La función recibe una lista y retorna True si está ordenada de mayor a menor,
# y False en caso contrario.

def esta_ordenada(lista):
	pass


# Ejercicio 4:
# La función recibe una lista y retorna:
# - los primeros 3 elementos
# - los últimos 3 elementos
# - la lista invertida
# - los elementos en posiciones impares
# (usar slicing)

def analizar_lista(lista):
	pass


# Ejercicio 5
# En un experimento de laboratorio se registraron mediciones en una lista L. 
# Debido a un error del sensor, algunos valores aparecen como 0, lo que indica que la medición falló.
# Para poder realizar los cálculos posteriores sin errores, se desea reemplazar esos valores defectuosos por otro número.

# a) Escribir una función def reemplaza(L, antiguo, nuevo):
# que recorra la lista L y reemplace todas las apariciones del valor antiguo por el valor nuevo.
# b) Modificar la función anterior para que la lista original no sea modificada, sino que la función devuelva una nueva lista con los cambios realizados.


def reemplaza(L, antiguo, nuevo):
	pass

# Ejercicio 5b:
# La función recibe una lista L y retorna una nueva lista donde se reemplazan
# todas las apariciones de 'antiguo' por 'nuevo', sin modificar la original.

def reemplaza_nueva(L, antiguo, nuevo):
	pass


def main():

	print(" Ejercicio 1a")
	print(suma_n(5))
	print(suma_n(10))

	print("\n Ejercicio 1b")
	pares_hasta_n(10)

	print("\n Ejercicio 2")
	print(suma_y_max([4, 7, 2, 9, 1]))
	print(suma_y_max([10, 3, 8]))

	print("\n Ejercicio 3")
	print(esta_ordenada([9, 7, 5, 3, 1]))
	print(esta_ordenada([9, 7, 8, 3, 1]))

	print("\n Ejercicio 4")
	print(analizar_lista([10, 20, 30, 40, 50, 60]))

	print("\n Ejercicio 5a")
	L = [4, 0, 7, 0, 5]
	reemplaza(L, 0, 1)
	print(L)

	print("\n Ejercicio 5b")
	L = [4, 0, 7, 0, 5]
	print(reemplaza_nueva(L, 0, 1))
	print(L)


if __name__ == '__main__':
	main()