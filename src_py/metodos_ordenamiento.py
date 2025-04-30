#crear clase metodos de ordenamiento
class MetodosOrdenamiento:

    def sort_bubble(self, array):
        arreglo=array.copy()
        n=len(arreglo)
        for i in range(n):
            for j in range(i+1,n):
                if arreglo[i]>arreglo[j]:
                    #aux=arreglo[j]
                    #arreglo[j]=arreglo[i]
                    #arreglo[i]=aux
                    #asignacion en una sola linea
                    arreglo[i],arreglo[j] = arreglo[j],arreglo[i]
        return arreglo

    #programar cada metodo
    #medir el tiempo con nano
    #imprimir 3 resultados, indicando cual es el mas optimo

    def sort_burbuja_mejorado_optimizado(self, array):
        arreglo=array.copy()
        tamaño = len(arreglo)
        for i in range(tamaño):
            for j in range(tamaño-1-i):
                if arreglo[j]<arreglo[j+1]:
                    #aux=arreglo[j]
                    #arreglo[j]=arreglo[j+1]
                    #arreglo[j+1]=aux
                    arreglo[j],arreglo[j+1]=arreglo[j+1],arreglo[j]  
        return arreglo

    def sort_seleccion(self, array):
        arreglo= array.copy()
        tamaño=len(arreglo)
        for i in range(tamaño-1):
            im=i
            for j in range(i+1,tamaño-1):
                if arreglo[j]<arreglo[im]:
                    im=j
            if i!=im:
                aux = arreglo[i]
                arreglo[i] = arreglo[im]
                arreglo[im] = aux
        return arreglo