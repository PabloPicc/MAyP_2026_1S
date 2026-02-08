import random
import matplotlib.pyplot as plt

def simular_jugada_individual():
    '''
    Devuelve el saldo resultante de simular una jugada individual, considerando tanto el costo de jugar como los posibles premios de la máquina tragamonedas.
    '''
    # BORRAR LA SIGUIENTE LÍNEA Y COMPLETAR
    pass

def ganancia_promedio_por_jugada():
    '''
    Devuelve el promedio estimado de ganancia por jugada a partir de 10000 simulaciones independientes.
    '''
    # BORRAR LA SIGUIENTE LÍNEA Y COMPLETAR
    pass

def probabilidad_de_ganar():
    '''
    Devuelve la probabilidad estimada de obtener una ganancia neta en una jugada, realizando 10000 simulaciones independientes.
    '''
    # BORRAR LA SIGUIENTE LÍNEA Y COMPLETAR
    pass


######## Funciones para jugadores con saldo objetivo ########

def jugador_alcanza_saldo_objetivo(saldo_objetivo):
    '''
    Simula el progreso de un jugador hasta alcanzar el saldo objetivo o quedarse sin dinero, asumiendo un capital inicial de $500. Devuelve True si logra el objetivo y False en caso contrario.
    '''
    # BORRAR LA SIGUIENTE LÍNEA Y COMPLETAR
    pass

def probabilidad_alcanzar_saldo_objetivo(saldo_objetivo):
    '''
    Devuelve la probabilidad estimada de que un jugador alcance el saldo objetivo, , asumiendo un capital inicial de $500, a partir de 1000 simulaciones independientes.
    '''
    # BORRAR LA SIGUIENTE LÍNEA Y COMPLETAR
    pass

def graficar_probabilidades_de_exito():
    '''
    Grafica la probabilidad (eje y) de que un jugador alcance el saldo objetivo (eje x), variando dicho saldo objetivo entre 501 y 600.
    '''
    # BORRAR LA SIGUIENTE LÍNEA Y COMPLETAR
    pass


########### CUERPO PRINCIPAL DEL PROGRAMA ###########
random.seed(42)

ganancia_promedio = ganancia_promedio_por_jugada()
print('Ganancia promedio por jugada: ' + str(ganancia_promedio))

probabilidad_de_ganar = probabilidad_de_ganar()
print('Probabilidad de ganar en una jugada: ' + str(probabilidad_de_ganar))

graficar_probabilidades_de_exito()
