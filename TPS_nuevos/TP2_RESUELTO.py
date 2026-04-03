#TP N2. Manejo de APIs y Pandas

import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

#Posibles issues INTERESANTES que puden surgir en este TP:
    
    #a.La cantidad de datos que se trae la API de series temporales tiene un límite de 100
    #Osea, deberán jugar con las fechas si es que quieren traer mucha data
    
    #b. Puede ser que las series de tiempo que extraigan tengan distinta granularidad
    #temporal. Ahí va a ser interesante ver cómo se las arreglan


#Función que llame a la API dados un ID y 2 fechas
#No voy a usar kwargs ya que no es nomenclatura dada en clase.
#Pero los pibes lo pueden usar dado que la API que deben investigar lo usa
def llamo_api(idd,start_date,end_date):
    API_BASE_URL = "https://apis.datos.gob.ar/series/api/series?"
    url=API_BASE_URL+'start_date='+start_date+'&end_date='+end_date+'&ids='+idd
    result = requests.get(url).json()
    return result         

#Función que, dadas las series de tiempo devuelve un df
def unifica(series):
    #Caso puntual mio. 2017 es mi tiempo mínimo y 2025 mi máximo.
    #La mínima granularidad es mensual. 2 son mensuales y 2 anuales
    #Solución: a los parámetros anuales le pongo su valor anual a principio de año y luego
    #null
    #Los chicos pueden resolver esto como quieren: dejar el mismo valor anual para todos 
    #los meses, dejar el valor anual al final del año en lugar de al principio, etc
    futuro_df={}
    anios=['2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025']
    meses=['01','02','03','04','05','06','07','08','09','10','11','12']
    for serie in series:
        campo=[]
        if serie[0]=='38.3_V_1994_M_4':
            nombre_campo='Hectolitros_vino'
        elif serie[0]=='eoh_plazas_5':
            nombre_campo='ocupacion_hotelera'
        elif serie[0]=='snic_1_victimas_arg':
            nombre_campo='homicidios_anuales'
        else :
            nombre_campo='muertes_accidentes_anio'
        #Extraemos info
        datos=serie[1]['data']
        #Recorremos nuestro rango
        for anio in anios:
            for mes in meses:
                date=anio+'-'+mes+'-'+'01'
                ausente=True
                for info in datos:
                    if date==info[0]:
                        campo.append(info[1])
                        ausente=False
                if ausente:
                    campo.append(None)
        futuro_df[nombre_campo]=campo
    #Por último, las fechas
    fechas=[]
    for anio in anios:
        for mes in meses:
            date=anio+'-'+mes+'-'+'01'
            fechas.append(date)
    futuro_df['date']=fechas
    #Creo el df
    df=pd.DataFrame(futuro_df)
    df.to_csv('dataset.csv')
    return df
            
            




#Función que, dado el df unificado, crea los outputs de refutación
#basicamente es manejo de Pandas
def refuta_prueba(df):
    #Primero la de homicidios
    h_2017=int(df['homicidios_anuales'][df['date']=='2017-01-01'])
    h_2022=int(df['homicidios_anuales'][df['date']=='2022-01-01'])
    percent_murder=((h_2022-h_2017)/h_2017)*100
    print('Los homicidios crecieron un '+str(percent_murder)+' %')
    
    #Luego tasa ocupación hotelera
    #Comparamos desde 2023 a 2025 para ver que baja
    #Comparamos contra 2018 para ver que no está tan mal
    #Siempre Enero
    hot_2023=float(df['ocupacion_hotelera'][df['date']=='2023-01-01'])
    hot_2024=float(df['ocupacion_hotelera'][df['date']=='2024-01-01'])
    hot_2025=float(df['ocupacion_hotelera'][df['date']=='2025-01-01'])
    hot_post=float(df['ocupacion_hotelera'][df['date']=='2021-01-01'])
    percent_1=((hot_2024-hot_2023)/hot_2023)*100
    percent_2=((hot_2025-hot_2024)/hot_2024)*100
    percent_post=((hot_2025-hot_post)/hot_post)*100
    
    print('La ocupación hotelera creció un '+str(percent_1)+' % de 2023 a 2024')
    print('La ocupación hotelera creció un '+str(percent_2)+' % de 2024 a 2025')
    print('La ocupación hotelera creció un '+str(percent_post)+' % comparando 2025 con la post-pandemia')
    
    #Último. Cuestión vino vs accidentes comparando con matplotlib
    #matplotlib: 
    fechas=['2015-01-01','2016-01-01','2017-01-01','2018-01-01']
    df['date']=pd.to_datetime(df['date'])
    
    #Los picos de venta de vino por año
    vino_1=df.loc[
    (df['date'] >= '2015-01-01') & 
    (df['date'] < '2016-01-01'), 
    'Hectolitros_vino'].max()
    
    vino_2=df.loc[
    (df['date'] >= '2016-01-01') & 
    (df['date'] < '2017-01-01'), 
    'Hectolitros_vino'].max()
    
    vino_3=df.loc[
    (df['date'] >= '2017-01-01') & 
    (df['date'] < '2018-01-01'), 
    'Hectolitros_vino'].max()
    
    vino_4=df.loc[
    (df['date'] >= '2018-01-01') & 
    (df['date'] < '2019-01-01'), 
    'Hectolitros_vino'].max()
    
    vinos=[vino_1,vino_2,vino_3,vino_4]
    
    #Los accidentes
    accidentes=[
        float(df.loc[(df['date']=='2015-01-01'),'muertes_accidentes_anio']),
        float(df.loc[(df['date']=='2016-01-01'),'muertes_accidentes_anio']),
        float(df.loc[(df['date']=='2017-01-01'),'muertes_accidentes_anio']),
        float(df.loc[(df['date']=='2018-01-01'),'muertes_accidentes_anio'])
               ]
    #Comienzo con matplotlib
    fig,ax1=plt.subplots(figsize=(10,6))
    
    ax1.set_xlabel('date')
    ax1.set_ylabel('Hectolitros de vino vendidos')
    ax1.plot(fechas,vinos,color='blue',marker='o',linestyle='-',label='vino')
    ax1.tick_params(axis='y',labelcolor='blue')
    
    ax2=ax1.twinx()
    ax2.set_ylabel('Muertes por accidents de tránsito')
    ax2.plot(fechas,accidentes,color='red',marker='s',linestyle='--',label='accidentes')
    ax2.tick_params(axis='y',labelcolor='red')
    
    #Vemos que no hay correlación
    plt.tight_layout()
    plt.show()
    
    
    


def main():
    #Parámetros para llamar a la API
    #Ids: asesinatos, ocupación hotelera, vinos, accidentes de tránsito
    ids=['snic_1_victimas_arg','eoh_plazas_5','38.3_V_1994_M_4','snic_3_hechos_arg']
    
    #Primera aseveración: muy puntual, de 2017 a 2022
    #Segunda: mirar como era el panorama antes de la pandemia hasta hoy (2018-2027)
    #Decir 2027 es una manera de tomar hasta hoy
    #Tercera: Del 2015 al 2018 baja progresivamente la cantidad de vino vendido en mercado
    #local. En ese mismo período los accidentes suben
    start_dates=['2017-01','2018-01','2015-01','2015-01']
    end_dates=['2022-01','2027-01','2019-01','2018-01']
    
    #Genero las llamadas a las apis
    llamadas={}
    for i in range(len(ids)):
        llamadas[ids[i]]=llamo_api(ids[i],start_dates[i],end_dates[i])
        
    #Unifico todos los datos traídos en un pandas dataframe y
    #Lo exporto en forma de .csv
    df=unifica(list(llamadas.items()))
    
    #Genero las corroboraciones correspondientes
    refuta_prueba(df)
    

if __name__ == "__main__":
    main()