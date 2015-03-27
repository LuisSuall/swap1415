# Práctica 2

## nginx

### Instalar nginx

Hemos descargado la clave y después la hemos importado:

![Captura 1](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica3/Capturas/descargaClaveNginx.png)

Tras realizar esto, añadimos el repositorio a la lista de repositorios, y tras eso, instalamos nginx:

![Captura 2](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica3/Capturas/nginxInstalado.png)

### Configuración del balanceo con nginx

Hemos editado el archivo que configura el balanceo de carga de nginx, y queda así:

![Captura 3](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica3/Capturas/confNginx1.png)

Vamos a comprobar el funcionamiento correcto del balanceo por round-robin, para ello hemos modificado el archivo hola.html de la máquina 1 añadiendo una línea que dice que estamos en la máquina 1, el de la máquina dos lo hemos dejado como estaba. Hemos realizado dos peticiones a la IP del balanceador pidiendo dicho archivo, podemos ver cómo la primera la responde la máquina 1 y la segunda la máquina 2:

![Captura 4](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica3/Capturas/conmprobacionBalanceoRRNginx.png)

Ahora hemos modificado nuevamente la configuración, para añadir pesos a las máquinas. La **máquina 1** recibirá el doble de peticiones que la **máquina 2**. Esta imagen es la nueva configuración:

![Captura 5](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica3/Capturas/confNginx2.png)

Y aquí comprobamos que funciona:

![Captura 6](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica3/Capturas/conmprobacionBalanceoPesosNginx.png)

## haproxy

### Instalar haproxy

La instalación de haproxy es muy sencilla, simplemente tenemos que ejecutar el comando `apt-get install haproxy joe`

### Configurar haproxy

Modificamos el fichero `/etc/haproxy/haproxy.cfg` y queda así:

![Captura 7](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica3/Capturas/confHaproxy1.png)

Y ahora comprobamos que funciona correctamente:

![Captura 8](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica3/Capturas/comprobacionBalanceoRRHaproxy.png)

Como con nginx, ahora vamos a configurar haproxy para que la **máquina 1** reciba el doble de peticiones que la **máquina 2**. La configuración queda así:

![Captura 9](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica3/Capturas/confHaproxy2.png)

Y podemos ver que funciona correctamente:

![Captura 10](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica3/Capturas/comprobacionBalanceoPesosHaproxy.png)




