class Botella:    
    def _init_(self, material, capacidad, forma, diseno, tapa, grabados):
        # Atributos
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa
        self.grabados = grabados
        self.contenido_actual = 0
        self.esta_cerrada = True
        self.tapa_abierta = True
    
    def contener_liquidos(selft):
       print (f"La botella de {selft.material} puede contener una cantidad de liquido de {selft.capacidad}")
       
    def facilitar_vertido(selft):
        if selft.tapa_abierta == True:
            return print(f"la {selft.tapa} esta {selft.esta_cerrada} ingrese la cantidad de liquido que quiere vertir, este es el contenido actual {selft.contenido_actual} y tiene una capacidad maxima de {selft.capacidad}")
    def Ciere_hermetico(selft):
        if selft.tapa_abierta == True:
            print (f"Se esta sellando la tapa hermeticamente, estado de la tapa es {selft.tapa_abierta}, con contenido de la botella de {selft.material} es de {selft.contenido_actual}")
    def transporte(selft):
        if selft.esta_cerrada == True:
            return print (f"Se empaqueta para entregar la botella de {selft.material} con el contenido de {selft.contenido_actual} y se empaqueta {selft.forma}")
        else:
            print (f"Se sellan la {selft.tapa} y se confirma que este cerrada para transportarse")    
    
    def Manejo(selft):
        print (f"La botella {selft.material} tiene una forma {selft.forma} la cual se optimizo el empaquetado, su manejo es comodo")
        
    def Compatibilidad_frio_caliente(selft):
        print (f"Gracias a que la botella es de material {selft.material} puede soportar frio sin comprometerse, en calor solo hasta cierto punto ")
         
    def Reutilizacion(selft):
        print (f"El contenido actual de la botella {selft.material} es de {selft.contenido_actual} con capacidad maxima de {selft.capacidad}")
    
    def Transparencia(selft):
        print (f"el estado de la tapa de la botella {selft.material} es de {selft.esta_cerrada}")
        
