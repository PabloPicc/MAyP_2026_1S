#Tenemos un diccionario así

#Tenemos una lista de diccionarios donde cada diccionario representa a una 
#persona económicamente activa del país

#El diccionario posee: 
    #el año de cuando se tomó la muestra (siempre 2025)
    #una lista con los ingresos mes a mes de esa persona
    #una lista con los gastos de ese año mes a mes
    #Los datos personales de esa persona: edad al momento de la encuesta, nombre y sexo
    



{'year':2025,
 'salary_usd':[1000,900,1100,1000,800,850,800,1000,900,920,850,1000],
 'costs':[600,600,620,630,700,700,700,790,800,700,700,710],
 'personal_data':{
     'name':'Carlos Espinoza',
     'age':31,
     'gender':'M'
     }
 }


#a.- Generar una function que tome como input UN DICCIONARIO de la lista y deuelva
     #una tupla de 2 valores: 
         #*el dinero adeudado/ahorrado en el año
         #La cantidad de años que le falta a la persona para la jubilación (60 mujeres y 65 hombres)
         
#b.- Generar una function que tome como input LA LISTA ENTERA DE DICCIONARIOS
# y devuelva otra lista de igual dimensión con los montos que los ciudadanos ahorrarán/adeudarán al jubilarse
#SUPONER que cada persona de aca hasta jubilarse ahorra/adeuda por año lo mismo que en 2025

#c.- Reutilizando la función "b" crear una function que tome como input LA LISTA ENTERA DE DICCIONARIOS
#Y devuelva True en caso de que el país prospere (ahorro neto de la población) y False en caso de que
#quiebre (deuda neta de la población)

#a.-
def neto_flujo(dicc):
    ahorro=0
    for i in range(len(dicc['salary_usd'])):
        ahorro=ahorro+(dicc['salary_usd'][i]-dicc['costs'][i])
    if dicc['personal_data']['gender']=='F':
        anios=60-dicc['personal_data']['age']
    else:
        anios=65-dicc['personal_data']['age']
    return (ahorro,anios)
        
#b.-     
        
        
        

def main():
    carlos={'year':2025,
     'salary_usd':[1000,900,1100,1000,800,850,800,1000,900,920,850,1000],
     'costs':[600,600,620,630,700,700,700,790,800,700,700,710],
     'personal_data':{
         'name':'Carlos Espinoza',
         'age':31,
         'gender':'M'
         }
     }
    
    carlina={'year':2025,
     'salary_usd':[1000,900,1100,1000,800,850,800,1000,900,920,850,1000],
     'costs':[600,600,620,630,700,700,700,790,800,700,700,710],
     'personal_data':{
         'name':'Carlina Perez',
         'age':30,
         'gender':'F'
         }
     }
    
    L=[carlos,carlina]











