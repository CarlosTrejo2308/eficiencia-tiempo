# Eficiencia-tiempo

## Introducción
Repositorio para la clase "Calidad y Pruebas de Software"

En la norma ISO 9126 nos habla de las características de calidad. Entre ellas tenemos la "Eficiencia", donde a su vez tenemos Eficiencia en tiempo y Eficiencia en Recursos.

En este ejercicio haremos una prueba a un software y mediremos la eficiencia que tiene el software en cuanto al tiempo de ejecución.

Después adaptaremos nuestro código para poder probar la eficiencia de ejecución de cualquier función.

## Pasos

1. Prueba la función fiboRecursivo
2. Utiliza la funcion datetime.now para obtener el tiempo antes y después de mandar a ejecutar fiboRecursivo. Averigua cuanto tarda en calcular el Fibonacci 1, 5, 10, 15 y 20
3. Repite la operación anterior unas 5 veces para obtener un resultado promedio

### Mejorar el codigo
Una vez teniendo los resultado, prueba creando una version mejorada de la función de Fibonacci utilizando el método iterativo. Vuelve a ejecutar el codigo y compara las 2 funciones.

También puedes encapsular tu código de comparación encapsulando en otra función:
```
def eficienciaTiempo():
    # 1. Obtener el tiempo inicial
    # 2. Ejecutar el codigo
    # 3. Obtener el tiempo final
    # 4. Calcular y devolver la diferencia de tiempo
```

### Wrapper function
Finalmente, mejora esa función de tal manera que reciva como parametro una funcion cualquiera.

## Resultados
Anota tus resultados y conclusiones en un archivo llamado "resultados.md" y tu codigo dentro del archivo "fibo.py" con comentarios.