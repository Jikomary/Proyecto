class Nodo:
    def __init__(self,matriz,pos_bot,estado,recorrido,marcados):
        """
        matriz = Estado actual del juego
        pos_bot = posición actual del ratón x,y (enteros)
        estado = estado de los objetivos queso,pelota (booleanos)
        """
        self.matriz = matriz
        self.x = pos_bot[0]
        self.y = pos_bot[1]
        self.nemo = estado[0]
        self.marlin = estado[1]
        self.dori = estado[2]
        self.recorrido = recorrido
        self.marcados = marcados
#0=robot,1=roca,2=espacios disponibles,3=tiburon,4=torguda,5=dori,6=marlin,7=nemo,Acuaman=8


    def verificar_perdi(self):
        return self.matriz[self.y,self.x] == 3 or self.matriz[self.y,self.x] == 4 or self.matriz[self.y,self.x] == 8

    def verificar_ganar(self):
        return self.marlin and self.nemo and self.dori #Verificar que encontré los dos objetivos

    def marcar_objetivos(self):
        if  not(self.nemo) and self.matriz[self.y,self.x]== 7:
            self.nemo = True
            self.marcados = [] #Al encontrar el queso, puedo devolverme

        if  self.nemo and not (self.marlin) and self.matriz[self.y,self.x]== 6:
            self.marlin = True
            self.marcados = []    
        
        if self.matriz[self.y,self.x]==5 and self.nemo and self.marlin and not (self.dori):
            self.dori = True


    def generar_hijos(self):
        #Hijo de arriba
        hijos = []
        x = self.x
        y = self.y-1
        
        if y >= 0 and not((x,y) in self.marcados) and self.matriz[y,x]!=1: #Verificar que estoy en el tablero
            recorrido = self.recorrido.copy() #Garantizar que sea independiente
            recorrido.append((x,y)) #Agregar la posición actual
            marcados = self.marcados.copy() #Nodos ya visitados
            marcados.append((x,y)) 
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.nemo,self.marlin,self.dori),
                recorrido,   
                marcados   
            )
            hijo.marcar_objetivos()
            hijos.append(hijo)            
        #Hijo de abajo

        x = self.x
        y = self.y+1
        
        if y < self.matriz.shape[0]  and not((x,y) in self.marcados) and self.matriz[y,x]!=1: #Verificar que estoy en el tablero
            recorrido = self.recorrido.copy() #Garantizar que sea independiente
            recorrido.append((x,y)) #Agregar la posición actual
            marcados = self.marcados.copy() #Nodos ya visitados
            marcados.append((x,y)) 
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.nemo,self.marlin,self.dori),
                recorrido,   
                marcados    
            )
            hijo.marcar_objetivos()
            hijos.append(hijo)



        #Hijo de la izquierda

        x = self.x-1
        y = self.y
        
        if x >= 0 and not((x,y) in self.marcados) and self.matriz[y,x]!=1: #Verificar que estoy en el tablero
            recorrido = self.recorrido.copy() #Garantizar que sea independiente
            recorrido.append((x,y)) #Agregar la posición actual
            marcados = self.marcados.copy() #Nodos ya visitados
            marcados.append((x,y)) 
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.nemo,self.marlin,self.dori),
                recorrido,       
                marcados
            )
            hijo.marcar_objetivos()
            hijos.append(hijo)
       #Derecha
        x = self.x+1
        y = self.y
        
        if x < self.matriz.shape[1] and not((x,y) in self.marcados) and self.matriz[y,x]!=1: #Verificar que estoy en el tablero
            recorrido = self.recorrido.copy() #Garantizar que sea independiente
            recorrido.append((x,y)) #Agregar la posición actual
            marcados = self.marcados.copy() #Nodos ya visitados
            marcados.append((x,y)) 
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.nemo,self.marlin,self.dori),
                recorrido,
                marcados

            )
            hijo.marcar_objetivos()
            hijos.append(hijo)
 
        return hijos