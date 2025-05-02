# primera forma de importar 
# import benchmarking as bm

# segunda forma de importacion
from benchmarking import benchmarking
#ARCHIVO PRINCIPAL O MAIN
from metodos_ordenamiento import MetodosOrdenamiento

#metodo main
if __name__ == "__main__":
    print("Funciona")

    benchmarking() #ejecuta el constructor
    
    bench= benchmarking()
    metodosO= MetodosOrdenamiento()
    
    #tam=10000
    tamanios= [5000,10000,10500]
    
    
    
    metodos_dic ={
        "burbuja":metodosO.sort_bubble,
        "burbuja_Mejorado":metodosO.sort_burbuja_mejorado_optimizado,
        "seleccion":metodosO.sort_seleccion,
        "shell":metodosO.shell_sort
    }
    
    resultados=[]
    for tam in tamanios:
        arreglo_base = bench.buil_arreglo(tam)
        for nombre, fun_metodo in metodos_dic.items():
            tiempo_resultado = bench.medir_tiempo(fun_metodo,arreglo_base)
            tupla_resultado =(tam,nombre,tiempo_resultado)
            resultados.append(tupla_resultado)
        
    for tam,nombre,tiempo in resultados:
        print(f"tamaño:  {tam}, nombre: {nombre}, tiempo: {tiempo:.6f} segundos")