import random
import numpy as np

class montecarlo():
    def __init__(self,probabilidad_cruceros, probabilidad_turistas,num_cruceros, num_turistas, ganancia, dias, iteraciones):
        self.probabilidad_cruceros = probabilidad_cruceros
        self.probabilidad_turistas = probabilidad_turistas
        self.num_cruceros = num_cruceros
        self.num_turistas = num_turistas
        self.ganancia = ganancia
        self.dias = dias
        self.iteraciones = iteraciones

        self.inf_cruceros = np.array([])
        self.sup_cruceros = np.array([])
        self.inf_turistas = np.array([])
        self.sup_turistas = np.array([])
        self.turistas_periodo = np.array([])
        self.ganancias_periodo = np.array([])
        self.data_iteraciones = []
    
    def acumuladas(self):
        inf_cruceros = np.array([])
        sup_cruceros = np.array([])

        # Cruceros Probabilidades acumuladas
        for i in range(len(self.probabilidad_cruceros)):
            if i == 0:
                inf_cruceros = np.append(inf_cruceros, [0])
                sup_cruceros = np.append(sup_cruceros, [self.probabilidad_cruceros[i]])
            else:
                inf_cruceros = np.append(inf_cruceros,[sup_cruceros[i-1]])
                sup_cruceros = np.append(sup_cruceros,[sup_cruceros[i-1] + self.probabilidad_cruceros[i]])
        
        self.inf_cruceros = inf_cruceros
        self.sup_cruceros = sup_cruceros

        # Turistas Probabilidades acumuladas
        inf_turistas = np.array([])
        sup_turistas = np.array([])

        for i in range(len(self.probabilidad_turistas)):
            if i == 0:
                inf_turistas = np.append(inf_turistas,[0])
                sup_turistas = np.append(sup_turistas,[self.probabilidad_turistas[i]])
            else:  
                inf_turistas = np.append(inf_turistas,[sup_turistas[i-1]])
                sup_turistas = np.append(sup_turistas,[sup_turistas[i-1] + self.probabilidad_turistas[i]])
        
        self.inf_turistas = inf_turistas
        self.sup_turistas = sup_turistas


    def sim_ganancia(self):
        self.acumuladas()

        respuesta = np.array([])
        # Simulacion de cruceros por dia que se repite para la cantidad de dias especificados
        for i in range(self.dias):
            t_diario = self.valores_random(self.inf_cruceros, self.sup_cruceros, self.num_cruceros)*self.valores_random(self.inf_turistas, self.sup_turistas, self.num_turistas)        
                    
            respuesta = np.append(respuesta,[t_diario])

        #Turistas por periodo y ganancias
        self.turistas_periodo =  respuesta            
        self.ganancias_periodo = respuesta * self.ganancia
    
    
    
    def valores_random(self, inferior, superior, datos):
        valor = 0
        semilla = random.randint(0,100)
        if semilla > inferior[0] and semilla <= superior[0]:
            valor = datos[0]

        elif semilla > inferior[1] and semilla <= superior[1]:
            valor = datos[1]

        elif semilla > inferior[2] and semilla <= superior[2]:
            valor = datos[2]

        elif semilla > inferior[3] and semilla <= superior[3]:
            valor = datos[3]
        
        return valor





