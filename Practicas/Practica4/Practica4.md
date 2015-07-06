#Practica 4

Para la toma de datos, hemos creado dos scripts para la automatización del proceso, que se encuentran en este mismo repositorio. Después se tomaron los datos de las tres configuraciones realizadas: un solo servidor, Nginx y Haproxy.

Como veremos, los resultados no muestran lo que esperabamos. La configuración de un solo servidor funciona mejor que las soluciones con balanceador. Esto puede ser debido al sistema de simulación de las máquina virtuales o a limitaciones de la máquina física que ha ejecutado la prueba.

Las opciones de ambas pruebas, tanto AB como SIEGE, han sido elegidas intentando alcanzar un alto grado de carga. Encontramos que en estas condiciones, el sistema o siempre funcionaba, o se quedaba congelado, y por tanto nos quedabamos sin datos para poder analizar su funcionamiento. Por tanto, elegimos un alto grado de carga que no paralice el sistema.

## ApacheBench

Los resultados obtenidos son:

Un servidor:
![Captura 1](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica4/Capturas/Tabla1.png)

Nginx:
![Captura 2](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica4/Capturas/Tabla2.png)

Haproxy:
![Captura 3](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica4/Capturas/Tabla3.png)


No mostramos la gráfica de "Failed request", pues no hemos obtenido información, como ya hemos comentado anteriormente.

![Captura 4](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica4/Capturas/Grafica1.png)

![Captura 5](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica4/Capturas/Grafica1.png)

## SIEGE

Los resultados obtenidos son:

Un servidor:
![Captura 6](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica4/Capturas/Tabla4.png)

Nginx:
![Captura 7](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica4/Capturas/Tabla5.png)

Haproxy:
![Captura 8](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica4/Capturas/Tabla6.png)

En este caso, las gráficas de "Response time" y "Failed Transactions" no nos ofrecen ninguna información. Veamos las otras gráficas:

![Captura 9](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica4/Capturas/Grafica3.png)

![Captura 10](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica4/Capturas/Grafica4.png)

## Conclusiones

Como ya hemos dicho, los datos no parecen correctos. Un único servidor es más rápido que una configuración con más máquinas, de la misma potencia. Esto puede ser debido a como se simula el sistema, y a las diferencias que esto tiene con respecto a un sistema real.

De todas maneras, este tipo de resultados podrían darse en la un ejemplo real, ya que el intercambio de mensajes entre el balanceador y las máquinas servidoras realentizan la respuesta.

Por lo que podemos ver, el balanceo con Haproxy es más efectivo que con Nginx, pero un único servidor realiza de una manera más efectiva la tarea.
