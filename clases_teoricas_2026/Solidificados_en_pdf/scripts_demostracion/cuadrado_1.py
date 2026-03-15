import math as mt
# Palabra clave class + nombre de la clase que estás creando
class Cuadrado:
    
    # Incicializador, si o si debe tenerlo. 
    # El input de la función init es lo que obligatoriamente debés pasarle a la class
    # La palabra clara "self" refiera al objeto que estás creando al ejecutar esta clase
    def __init__(self,lado):
        self.lado=lado
        self.perimetro=4*lado
        self.sup=lado**2
    
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
       
        
       
        
        