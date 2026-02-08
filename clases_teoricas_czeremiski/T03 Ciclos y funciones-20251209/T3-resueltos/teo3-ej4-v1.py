# Se define una función que devuelve un str con los números del 1 al 5
def obtener_escalera():
  escalera = ''
  for i in range(1,6):
    escalera = escalera + str(i) + ' '
  return escalera

# Cuerpo principal del programa
print('Ana: ¡Yo tengo escalera!')
print(obtener_escalera())
print('Agustín: ¡Yo también!')
print(obtener_escalera())
print('¡Mirá qué casualidad!')
print(obtener_escalera())
