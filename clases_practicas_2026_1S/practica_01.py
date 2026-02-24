# La función toma como parámetros dos números y retorna el mayor, en caso de ser iguales debe retornar
# "Los números son iguales".

def maximo(x,y):
	pass

# La función recibe como parámetro un número y retorna el valor booleano 'True' si es par y 'False' si no.

def es_par(x):
	pass

# La función recibe un el tamaño de un radio cualquiera y debe retornar el valor del área de un círculo.

def area_circulo(r):
	pass

# La función debe retornar las correspondientes raíces de una función cuadrática. En caso
# de que no tenga debe retornar "La función no posee raíces reales", si tiene dos debe retornar la menor.

def raices(a,b,c):
	pass

def main():

	print(maximo(2,4))
	print(maximo(6,3))
	print(maximo(1,1))

	print(es_par(4))
	print(es_par(6))
	print(es_par(36))
	print(es_par(71))

	print(area_circulo(1))
	print(area_circulo(2))
	print(area_circulo(3))

	print(raices(1,0,-4)) # 2 y -2
	print(raices(5,-20,15)) # 1 y 3
	print(raices(9,108,324)) # -6
	print(raices(1,2,2)) # La función no posee raíces reales

if __name__ == '__main__':
	main()