A=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

#Puede verse row-like como:
    #[1   2  3
    # 4   5  6
    # 7   8  9 
    # 10 11 12]

#Puede verse column-like:
    #[1 4 7 10
    # 2 5 8 11
    # 3 6 9 12]


#Queremos recorrer por filas pero interpretando las listas como filas
#o como columnas

#Si interpretamos a A de manera "filar"
#Directo, agarras una fila y la recorres. Cada lista es una fila
for i in range(len(A)):
    for j in range(len(A[i])):
        print('El elemento de la fila '+str(i)+ ' y la columna '+str(j)+ ' es '+str(A[i][j]))


#Interpretando de manera "columnar"
#Cada lista es una columna, tenés que agarrar el elemento i-esimo de 
#cada lista. Eso constituye una fila
for i in range(len(A[0])):
    for j in range(len(A)):
        print('El elemento de la fila '+str(i)+ ' y la columna '+str(j)+ ' es '+str(A[j][i]))
        

#Interpretando la matriz A como filar o columnar. Desarrollar
#Funcion que sume todos los elementos de una matriz
def suma_elementos(A):
    pass

#Funcion que sume las filas de una matriz
def suma_elementos_fila(A):
    pass

#Function que toma una matriz cuadrada y suma su diagonal
def suma_elementos_diagonal(A):
    pass
    
#Harder: Function que toma cualquier matriz, cuadrada o no 
#y suma su diagonal
def suma_elementos_diagonal_any(A):
     pass
    
#Much harder: Function que toma una matriz y devuelve la matriz transpuesta
def transpuesta(A):
    #Creo una matriz vacia con dimensiones al reves
    pass
        
            
    
    
    
    
    
    
    
    
    