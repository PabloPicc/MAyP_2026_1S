#Problema N4 Simulación


#Un inversor puede elegir entre dos alternativas de inversión:
#▶ un bono seguro, que rinde 2 % anual,
#▶ un proyecto riesgoso, que tiene:
    #*** 15 % de probabilidad de pérdida del 20 %,
    #*** 85 % de probabilidad de ganancia del 10 %.
        
#Se pide escribir un programa en Python que:
#1. Simule 30 años (vida económicamente productiva) invirtiendo en ambas estrategias
#2. Estime el rendimiento promedio del bono y del proyecto riesgoso.
#3. Compare los resultados y discuta cuál conviene elegir según el rendimiento esperado.

#Corran esta simulación de 30 años 100K veces para sacar el promedio

#Sugerencia: usar random.random() para decidir si el proyecto riesgoso gana o pierde
#en cada simulación.
#Este tipo de simulaciones permite analizar decisiones financieras, de seguros o de
#inversión bajo incertidumbre.

import random


def resultado_anual():
    res=random.random()
    if res<=0.15:
        monto=-0.20
    else:
        monto=0.10
    return 1+monto


def comparacion_anios(N):
    rend_total_inversion=1
    rend_total_bono_seguro=1
    for i in range(N):
        rend_total_inversion=rend_total_inversion*resultado_anual()
        rend_total_bono_seguro=1.02*rend_total_bono_seguro
    return rend_total_inversion,rend_total_bono_seguro
        


def main():
    N=30
    simu_inversiones=[]
    simu_bono_seguro=[]
    for i in range(100000):
        res=comparacion_anios(N)
        simu_inversiones.append(res[0])
        simu_bono_seguro.append(res[1])
    prom_inv=sum(simu_inversiones)/100000
    prom_bono=sum(simu_bono_seguro)/100000
    print('En promedio, ir por la inversion riesgosa te dará este retorno: ',str(prom_inv))
    print('En promedio, ir por el bono seguro te dará este retorno: ',str(prom_bono))
    

if __name__ == "__main__":
    main()


































