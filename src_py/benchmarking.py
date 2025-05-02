from metodos_ordenamiento import MetodosOrdenamiento
#import metodos_ordenamiento as mO
import random
import time
#declaracion de la clase
class benchmarking:
    
    def __init__(self): #metodo constructor
        """
        print("Benchmarking Instanciado")
        self.mO =MetodosOrdenamiento()

        arreglo=self.buil_arreglo(10000)

        tarea= lambda:self.mO.sort_bubble(arreglo)

        tiempoM=self.contar_con_current_time_milles(tarea)
        tiempoN=self.contar_con_nano_times(tarea)
        #print(f"tiempo en milisegundos: {tiempoM}")
        print(f"tiempo en nanosegundos: {tiempoN}")

        tarea1= lambda:self.mO.sort_burbuja_mejorado_optimizado(arreglo)
        tiempoM=self.contar_con_current_time_milles(tarea1)
        tiempoN=self.contar_con_nano_times(tarea1)
        #print(f"tiempo en milisegundos: {tiempoM}")
        print(f"tiempo en nanosegundos: {tiempoN}")
        
        tarea2= lambda:self.mO.sort_seleccion(arreglo)
        tiempoM=self.contar_con_current_time_milles(tarea2)
        tiempoN=self.contar_con_nano_times(tarea2)
        #print(f"tiempo en milisegundos: {tiempoM}")
        print(f"tiempo en nanosegundos: {tiempoN}")
        
        """
        
    def medir_tiempo(self, funcion, array):
        inicio= time.perf_counter()
        funcion(array)
        fin= time.perf_counter()
        return fin -inicio
    
    def buil_arreglo(self, tamaño):
        arreglo=[]
        for i in range(tamaño):
            numero= random.randint(0,99999)
            arreglo.append(numero)
        return arreglo

    #importar archivo tipo time
    #milisegundos en segundos con #x= time.time()
    #nanosegindos con x= time.time_ns()
    def contar_con_current_time_milles(self,tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        tiempoSegundos = fin-inicio
        return tiempoSegundos

    def contar_con_nano_times(self,tarea):
        inicio =time.time_ns()
        tarea()
        fin=time.time_ns()
        tiempons=(fin -inicio)/1_000_000_000.0
        return tiempons

