import java.util.Random;



public class Benchmarking {
    private MetodosOrdenamiento MetodosOrdenamiento;
    public Benchmarking(){
        long currentMillis = System.currentTimeMillis();//sacar la fecha
        long currentNano = System.nanoTime();
        System.out.println(""+currentMillis);
        System.out.println("" +currentNano);

        MetodosOrdenamiento =new MetodosOrdenamiento();

        int [] arreglo= generarArregloAleatorio(1000);
        Runnable tarea = ()-> MetodosOrdenamiento.burbujaTradicional(arreglo);
        double tiempoDuracionMilis= medirConCurrerntTimeMiles(tarea);
        double tiempoDuracionNano= medirNanoTieme(tarea);

        System.out.println("tiempo en milisegundos: "+ tiempoDuracionMilis);
        System.out.println("tiempo en nanosegundos: "+ tiempoDuracionNano);

    }


    private int[] generarArregloAleatorio(int tamaño) {
        int []array =new int[tamaño];
        Random random = new Random();
        for (int i=0;i<tamaño;i++) {
            array[i]= random.nextInt(100000);
        }
        return array; 
    }

    public double medirConCurrerntTimeMiles(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        double tiempoSegundos = ((fin-inicio) / 1000.0);
        return tiempoSegundos;
    }

    public double medirNanoTieme(Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin= System.nanoTime();
        double tiempoSegundos= ((fin-inicio) / 1000000000.0);
        return tiempoSegundos;
    }
    
}
