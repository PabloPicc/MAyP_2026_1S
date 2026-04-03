class Cuadrado:
    
    def __init__(self,lado):
        self.lado=lado
    
    def calcula_perimetro(self):
        self.perimetro=4*self.lado
        
        
    def shrink(self,cuanto):
        self.lado=self.lado-cuanto
        
    def pasa_test(self):
        if self.lado>1:
            return True
        else:
            return False
    
    def __eq__(self, other):
        return self.lado == other.lado

cuad1=Cuadrado(4)
cuad2=Cuadrado(4)
cuad3=Cuadrado(5)
print(cuad1==cuad2)
print(cuad1==cuad3)





        
#Paso a paso, que estamos haciendo en cada secuencia?

cuadra=Cuadrado(5)
cuadra.perimetro
cuadra.lado
cuadra.calcula_perimetro()
cuadra.perimetro

cuadra.shrink(4.5)
cuadra.lado
cuadra.calcula_perimetro()
cuadra.perimetro
pasa=cuadra.pasa_test()
        
 
        
 
    

    
 
    
 
    
 
    
    
    #Aca estoy creando un método que resta la superficie de un cuadrado menor a nuestro 
    #cuadrado ya creado y con la sup restante crea un cuadrado más chico.
    #Redefiniendo el lado de nuestro cuadrado
    def resto_sup(self,lado_comparativo):
        if lado_comparativo>self.lado:
            return 'No se puede restar una sup. más grande que la sup. original'
        self.sup= self.sup-(lado_comparativo**2)
        self.lado=mt.sqrt(self.sup)
        self.perimetro=self.lado*4
        
    #Método para saber si el cuadrado resultante tiene una superficie "aceptable":
    #Decimos que aceptable es mayor a 4
    def es_aceptable(self):
        if self.sup>1:
            return True
        else:
            return False
       