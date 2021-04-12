from tkinter import*
from tkinter import messagebox
import numpy as np

# Importamos el modulo montecarlo
from modulo_montecarlo import*

# Definicion de colores
fondo = "#f2f3f4"
fc1 = "#2471a3"
font_size = 15
fuente = ("Arial",13)

lvl1 = 0.15
lvl2 = 0.2

class Aplicacion(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(width = 850, height = 650, bg = fondo)
        Label(self, text = "Montecarlo", font = ("Arial", 20), bg = fondo, fg = "#22a200").place(relx = 0.4, rely = 0.05)
        
        #Llegada de cruceros al dia
        Label(self, text = "Llegada de cruceros al dia",font = ("Arial", font_size), bg = fondo, fg = fc1).place(relx = 0.1, rely = lvl1)

        # Tabla
        Label(self,text = "No. Cruceros",font = ("Arial", font_size-2), bg = fondo, fg = fc1).place(relx = 0.1, rely = lvl2)
        Label(self,text = "Probabilidad (%)",font = ("Arial", font_size-2), bg = fondo, fg = fc1).place(relx = 0.3, rely = lvl2)

        self.txt_cruceros00 = Entry(self, font = fuente, justify = CENTER)
        self.txt_cruceros01 = Entry(self, font = fuente, justify = CENTER)
        self.txt_cruceros02 = Entry(self, font = fuente, justify = CENTER)
        self.txt_cruceros03 = Entry(self, font = fuente, justify = CENTER)
        self.txt_cruceros00.place(relx = 0.1, rely = 0.25, relwidth = 0.15)
        self.txt_cruceros01.place(relx = 0.1, rely = 0.29, relwidth = 0.15)
        self.txt_cruceros02.place(relx = 0.1, rely = 0.33, relwidth = 0.15)
        self.txt_cruceros03.place(relx = 0.1, rely = 0.37, relwidth = 0.15)

        self.txt_cruceros10 = Entry(self, font = fuente, justify = CENTER)
        self.txt_cruceros11 = Entry(self, font = fuente, justify = CENTER)
        self.txt_cruceros12 = Entry(self, font = fuente, justify = CENTER)
        self.txt_cruceros13 = Entry(self, font = fuente, justify = CENTER)
        self.txt_cruceros10.place(relx = 0.3, rely = 0.25, relwidth = 0.15)
        self.txt_cruceros11.place(relx = 0.3, rely = 0.29, relwidth = 0.15)
        self.txt_cruceros12.place(relx = 0.3, rely = 0.33, relwidth = 0.15)
        self.txt_cruceros13.place(relx = 0.3, rely = 0.37, relwidth = 0.15)
        


        #Llegada turistas por crucero
        self.lbl_prob_cruceros = Label(self, text = "Turistas por crucero al dia",font = ("Arial", font_size), bg = fondo, fg = fc1)
        self.lbl_prob_cruceros.place(relx = 0.55, rely = lvl1)

        # Tabla
        Label(self,text = "No. Turistas",font = ("Arial", font_size-2), bg = fondo, fg = fc1).place(relx = 0.55, rely = lvl2)
        Label(self,text = "Probabilidad (%)",font = ("Arial", font_size-2), bg = fondo, fg = fc1).place(relx = 0.75, rely = lvl2)

        self.txt_turistas00 = Entry(self, font = fuente, justify = CENTER)
        self.txt_turistas01 = Entry(self, font = fuente, justify = CENTER)
        self.txt_turistas02 = Entry(self, font = fuente, justify = CENTER)
        self.txt_turistas03 = Entry(self, font = fuente, justify = CENTER)
        self.txt_turistas00.place(relx = 0.55, rely = 0.25, relwidth = 0.15)
        self.txt_turistas01.place(relx = 0.55, rely = 0.29, relwidth = 0.15)
        self.txt_turistas02.place(relx = 0.55, rely = 0.33, relwidth = 0.15)
        self.txt_turistas03.place(relx = 0.55, rely = 0.37, relwidth = 0.15)

        self.txt_turistas10 = Entry(self, font = fuente, justify = CENTER)
        self.txt_turistas11 = Entry(self, font = fuente, justify = CENTER)
        self.txt_turistas12 = Entry(self, font = fuente, justify = CENTER)
        self.txt_turistas13 = Entry(self, font = fuente, justify = CENTER)
        self.txt_turistas10.place(relx = 0.75, rely = 0.25, relwidth = 0.15)
        self.txt_turistas11.place(relx = 0.75, rely = 0.29, relwidth = 0.15)
        self.txt_turistas12.place(relx = 0.75, rely = 0.33, relwidth = 0.15)
        self.txt_turistas13.place(relx = 0.75, rely = 0.37, relwidth = 0.15)

        # Datos para la simulacion
        Label(self,text = "Ganancia por turista", font = ("Arial", font_size-2), bg = fondo, fg = fc1).place(relx = 0.1, rely = 0.45)
        Label(self,text = "Numero de Dias", font = ("Arial", font_size-2), bg = fondo, fg = fc1).place(relx = 0.4, rely = 0.45)
        Label(self,text = "Iteraciones", font = ("Arial", font_size-2), bg = fondo, fg = fc1).place(relx = 0.7, rely = 0.45)

        self.txt_ganacia = Entry(self, font = fuente, justify = CENTER)
        self.txt_dias = Entry(self, font = fuente, justify = CENTER)
        self.txt_iteraciones = Entry(self, font = fuente, justify = CENTER)

        self.txt_ganacia.place(relx = 0.1, rely = 0.5, relwidth = 0.20)
        self.txt_dias.place(relx = 0.4, rely = 0.5, relwidth = 0.20)
        self.txt_iteraciones.place(relx = 0.7, rely = 0.5, relwidth = 0.20)
        
        # Seccion de impresion de resultados en la aplicacion
        self.respuesta_texto = StringVar()
        self.lbl_respuesta = Label(self, textvariable = self.respuesta_texto, bg = fondo, font = fuente)
        self.lbl_respuesta.place(relx = 0.10, rely = 0.6)


        # Botones 
        self.btn_calculo = Button(self, text = "Simular", bg = "#f5b041", command = self.recopilar_datos)
        self.btn_calculo.place(relx = 0.1, rely = 0.8, relwidth = 0.30)
        self.pack()

        self.btn_limpiar = Button(self, text = "Limpiar")
        self.btn_limpiar.place(relx = 0.50, rely = 0.8, relwidth = 0.30)
        self.pack()

       

    def recopilar_datos(self):
        try:
            num_cruceros = np.array([
                float(self.txt_cruceros00.get()),
                float(self.txt_cruceros01.get()),
                float(self.txt_cruceros02.get()),
                float(self.txt_cruceros03.get())
                ])

            probabilidad_cruceros = np.array([
                float(self.txt_cruceros10.get()),
                float(self.txt_cruceros11.get()),
                float(self.txt_cruceros12.get()),
                float(self.txt_cruceros13.get())
                ])

            num_turistas = np.array([
                float(self.txt_turistas00.get()),
                float(self.txt_turistas01.get()),
                float(self.txt_turistas02.get()),
                float(self.txt_turistas03.get())
                ])

            probabilidad_turistas = np.array([
                float(self.txt_turistas10.get()),
                float(self.txt_turistas11.get()),
                float(self.txt_turistas12.get()),
                float(self.txt_turistas13.get())
                ])
                
            iteraciones = int(self.txt_iteraciones.get())
            dias = int(self.txt_dias.get())
            ganancia = float(self.txt_ganacia.get())
            
        except:
            messagebox.showwarning(message = f"Deben llenarse todos los campos", title = "Alerta")
            return

        # Iniciamos una simulacion    
        resultado_simulacion = self.ejecutar_simulacion(probabilidad_cruceros, probabilidad_turistas,num_cruceros, num_turistas, ganancia, dias, iteraciones)
        
        self.respuesta_texto.set(f"El promedio global, la ganancia estimada por el periodo de {dias} dias para una aportacion \npor turista de ${ganancia} haciendo {iteraciones} iteraciones es: ${resultado_simulacion}")

        print(f"El promedio global, la ganancia estimada por el periodo de {dias} dias para una ganancia de ${ganancia} haciendo {iteraciones} iteraciones es: ${resultado_simulacion}")
        
        
    def ejecutar_simulacion(self, probabilidad_cruceros, probabilidad_turistas,num_cruceros, num_turistas, ganancia, dias, iteraciones):
        # Limpiamos el Label donde imprimimos la respuesta
        self.respuesta_texto.set("")

        # Creamos un objeto de tipo montecarlo para que haga los calculos
        simulacion = montecarlo(probabilidad_cruceros, probabilidad_turistas,num_cruceros, num_turistas, ganancia, dias, iteraciones)

        #Creamos vector para guardar el resumen de ganancias de cada corrida
        resumen_ganancias = []
        # Ejecutamos la simulacion montecarlo la cantidad de iteraciones especificadas por el usuario
        for i in range(iteraciones):
            # Ejecutamos el metodo sim_ganancia para calcular la ganancia de un periodo de x dias
            simulacion.sim_ganancia()
            # imprimimos en consola las ganancias por dia de cada periodo
            #print(simulacion.ganancias_periodo)

            
            # Anexamos y guardamos cada uno de los resultados en una lista para despues obtener sus promedios
            resumen_ganancias.append(simulacion.ganancias_periodo)

        # Creamos un vector para guardar los promedios de cada iteracion
        resumen_promedios = np.array([])
        for semana in resumen_ganancias:
            # Creamos una variable para guardar el valor del promedio de cada iteracion 
            # (Cada iteracion contiene la informacion de la cantidad de dias especificada para cada periodo por ejemplo 7 dias, 5 dias, dos semanas)
            prom_iteracion = 0
            for dia  in semana:
                # Se suman las cantidades obtenidas de cada dia del periodo especificado
                prom_iteracion += dia
            # La suma de las ganancias de cada periodo (iteracion) se guarda en el vectorque contendra las ganancias semanales de cada iteracion
            resumen_promedios = np.append(resumen_promedios, [prom_iteracion])
        
        # Finalmente obtenemos el promedio global, que es el resultado final de nuestro metodo montecarlo
        promedio_global = 0
        for resultado in resumen_promedios:
            # Sumamos todos los resultados del promedio para cada iteracion
            promedio_global += resultado

        # Obtenemos el promedio final de todas las iteraciones
        promedio_global = round(promedio_global/len(resumen_promedios), 3)

        print(resumen_promedios)
        return promedio_global
        # Limpiamos espacio en memoria
        del(simulacion)