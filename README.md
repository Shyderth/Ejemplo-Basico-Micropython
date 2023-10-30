# **Ejemplo-Basico-Micropython**
En este ejemplo se utilizan las funciones basicas de la libreria machine de micropython para controlar un led RGB con tres pulsadores.
Se utiliza la clase Pin para asignar los puertos de entrada a los pulsadores y las salidas para los colores del led.
## Consideraciones:
* Los pulsadores se encuentran en configuracion Pull-Up, por lo tanto el microcontrolador lee un '1' lógico cuando el pulsador se encuentra sin presionar.
* El led RGB es del tipo ánodo común. Cada color enciende con un '0' lógico y apaga con '1'.
* La función ``Pin.Value()`` devuelve un '1' al no recibir parametro y, por este motivo, se utiliza para preguntar el valor lógico de los pines de entrada (pulsadores).
