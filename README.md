## Problema:

Cuando los usuarios publican una actualización en las redes sociales, como una URL, imagen, actualización de estado, etc., otros usuarios en su red pueden ver esta nueva publicación en su feed de noticias. Los usuarios también pueden ver exactamente cuándo se publicó la publicación, es decir, cuántas horas, minutos o segundos han pasado desde entonces. Dado que a veces las publicaciones se publican y se ven en diferentes zonas horarias, esto puede ser confuso. Se te proporcionan dos marcas de tiempo de una de esas publicaciones que un usuario puede ver en su feed de noticias en el siguiente formato:

Day dd Mon yyyy hh:mm:ss +xxxx

Aquí +xxxx representa la zona horaria. Tu tarea es imprimir la diferencia absoluta (en segundos) entre ellos.

### Formato de Entrada:

La primera línea contiene , el número de casos de prueba.

Cada caso de prueba contiene  líneas, representando la marca de tiempo  y la marca de tiempo .

### Restricciones:

- La entrada contiene solo marcas de tiempo válidas.

### Formato de Salida:

Imprime la diferencia absoluta  en segundos.

### Ejemplo de Entrada:

Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000


### Ejemplo de Salida:

25200
88200

### Explicación:

En la primera consulta, cuando comparamos la hora en UTC para ambas marcas de tiempo, vemos una diferencia de 7 horas, que es 25200 segundos.

Similarmente, en la segunda consulta, la diferencia de tiempo es de 5 horas y 30 minutos para ajustar la zona horaria, por lo que tenemos una diferencia de 1 día y 30 minutos, lo que equivale a 88200 segundos.

