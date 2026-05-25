#Cada diccionario de la lista resultante debiera tener una estructura coo esta

arab={
 'nombre':'Arabia Saudita',
 'copas':[],
 'subcampeonatos':[],
 'tercer_puesto':[],
 'participaciones':[1994,1998,2002,2006,2018,2022]
 }


def clasifica_equipos(lista):
    lista_nueva=[]
    for elemento in lista:
        if len(elemento['copas'])>=2:
            elemento['categoria']=1
        elif len(elemento['copas'])==1:
            elemento['categoria']=2
        elif len(elemento['copas'])==0 and (len(elemento['subcampeonatos'])+len(elemento['tercer_puesto']))>=2:
            elemento['categoria']=3
        elif (len(elemento['subcampeonatos'])+len(elemento['tercer_puesto']))>0:
            elemento['categoria']=4
        elif len(elemento['participaciones'])>=10:
            elemento['categoria']=5
        else:
            elemento['categoria']=6
        lista_nueva.append(elemento)
    return lista_nueva
            

def corrige_clasificacion(lista):
    date=2026-30
    for elemento in lista:
        n_sub=len(elemento['subcampeonatos'])
        n_tres=len(elemento['tercer_puesto'])
        n_part=len(elemento['participaciones'])
        maximo_1=0
        maximo_2=0
        if elemento['categoria']==1 and elemento['copas'][-1]<=date:
            elemento['categoria']=2
        elif elemento['categoria']==2 and elemento['copas'][-1]<=date:
            elemento['categoria']=3
        #Se complica la logica cuando empieza a depender de campeonatos o subcampeonatos
        elif elemento['categoria']==3:
            if n_sub>0:
                maximo_1=elemento['subcampeonatos'][-1]
            if n_tres>0:
                maximo_2=elemento['tercer_puesto'][-1]
            if maximo_2<=date and maximo_1<=date:
                elemento['categoria']==4
        elif elemento['categoria']==4:
            if n_sub>0:
                maximo_1=elemento['subcampeonatos'][-1]
            if n_tres>0:
                maximo_2=elemento['tercer_puesto'][-1]
            if maximo_2<=date and maximo_1<=date:
                elemento['categoria']==5
        elif elemento['categoria']==5 and n_part>0 and elemento['participaciones'][-1]<=date:
            elemento['categoria']=6
    return lista
            


def prode(lista):
    resultados={}
    for i in range(len(lista)):
        for j in range(len(lista)):
            if j>i:
                nombre=lista[i]['nombre']+'_'+lista[j]['nombre']
                if lista[i]['categoria']<lista[j]['categoria']:
                    val=lista[i]['nombre']+' le gana a '+lista[j]['nombre']
                elif lista[j]['categoria']<lista[i]['categoria']:
                    val=lista[j]['nombre']+' le gana a '+lista[i]['nombre']
                else:
                    val='Empatan'
                resultados[nombre]=val
    return resultados
        
                    
        
#Ejercicio 2

import random

class Turno:
    def __init__(self,n_lados):
        self.n_lados=n_lados
        
    def tirar_dados(self):
        self.dado_1=random.randint(1,self.n_lados)
        self.dado_2=random.randint(1,self.n_lados)
        

def suma_siete(n_lados):
    tirada=Turno(n_lados)
    tirada.tirar_dados()
    res=tirada.dado_1+tirada.dado_2
    print(res)
    if res==7:
        return True
    else:
        return False















