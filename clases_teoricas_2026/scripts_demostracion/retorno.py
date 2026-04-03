from datetime import datetime

#Retorno de una acción

def retorno(precio_venta,precio_compra):
    ganancia=precio_venta-precio_compra
    return (ganancia/precio_compra)*100
    
def horas_minutos(t):
    horas=t//60
    minutos=t%60
    return 'estos son '+str(horas)+' horas y '+str(minutos)+' minutos ' 

def bisiesto():
    current_year=datetime.now().year
    bisiesto=False
    if current_year%4 == 0:
        if current_year%100 != 0:
            bisiesto=True
        else:
            if current_year%400 ==0:
                bisiesto=True
    return bisiesto
        

    
def fibo(num):
    if num<=1:
        return num
    else:
        return fibo(num-2)+fibo(num-1)
    

def fibo_while(num):
    i=1
    ante=1
    ult=0
    fibo=1
    while i<num:
        fibo=
        num=num+1
    return fibo
        

    
  
    
def main():
    compra=50
    venta=75
    print(retorno(venta,compra))
    
    f=570
    print(horas_minutos(f))
    
    print(bisiesto())

#d.- Inicializador. Este pedazo de código debe ir siempre
if __name__ == "__main__":
    main()