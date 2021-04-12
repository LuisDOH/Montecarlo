'''
    @LD-OH===================================================================
    Este es el programa principal para la simulacion de montecarlo que se
    usara para resolver el problema planteado en el siguiente video mediante
    python:
    
    https://www.youtube.com/watch?v=AsSbNQ-yatE
    
    [Con derechos de creacion I.N. Luis David Olguin H.]
'''    


from tkinter import*
# Importamos nuestro modulo de pantallas
from modulo_pantallas import*

raiz = Tk()
raiz.title("Metodo de Montecarlo")
raiz.geometry("900x700")
raiz.resizable(False, False)

#Instancia de la clase pantalla para crear la pantalla de inicio

app = Aplicacion(raiz)

if __name__ == '__main__':
    app.mainloop()
