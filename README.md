## Problema:

El problema consiste en determinar si un año dado es un año bisiesto o no. En el calendario gregoriano, un año bisiesto ocurre aproximadamente cada cuatro años, añadiendo un día extra al calendario en forma de un 29 de febrero. Sin embargo, existen algunas excepciones a esta regla.

### Condiciones para determinar un año bisiesto en el calendario gregoriano:
1. Si el año es divisible uniformemente por 4, es un año bisiesto, a menos que:
2. El año es divisible uniformemente por 100, entonces NO es un año bisiesto, a menos que:
3. El año también es divisible uniformemente por 400. En este caso, es un año bisiesto.

## Solución:

Para resolver el problema, se utiliza una función llamada `is_leap(year)` que toma un año como entrada y devuelve `True` si el año es bisiesto según las condiciones mencionadas, y `False` en caso contrario. La función utiliza la lógica de las condiciones especificadas en el enunciado para determinar si el año es bisiesto o no.

Primero, se verifica si el año es divisible uniformemente por 4. Si es así, se comprueba si es divisible uniformemente por 100. Si lo es, se verifica si también es divisible uniformemente por 400. Si cumple con todas estas condiciones, se establece la variable `leap` en `True`, indicando que el año es bisiesto. En cualquier otro caso, la variable `leap` se mantiene en `False`.

Una vez que se ha determinado si el año es bisiesto o no utilizando la función `is_leap(year)`, se imprime el resultado. Esto se hace leyendo el año desde la entrada estándar y luego llamando a la función `is_leap(year)` con ese año como argumento. El resultado se imprime en la salida estándar.
