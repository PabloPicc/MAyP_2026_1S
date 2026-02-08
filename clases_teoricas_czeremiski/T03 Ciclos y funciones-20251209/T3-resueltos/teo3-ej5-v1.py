# Se define una función que devuelve un string con los números de 1 a n (parámentro).
def primeros_numeros(n):
  res = ''
  for i in range(1,n+1):
    res = res + str(i) + ' '
  return res

# Cuerpo principal del prog.: se prueba la función usando distintos argumentos.
print(primeros_numeros(1))
print(primeros_numeros(3))
print(primeros_numeros(6))
print(primeros_numeros(10))
