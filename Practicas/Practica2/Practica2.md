# Práctica 2

### Instalar rsync

Al lanzar la instrucción `apt-get install rsync` nos informa que ya está instalado en las máquinas virtuales que hemos configurado:

![Captura1](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica2/Capturas/instalacionRsync.png)

Comprobamos que funciona haciendo `rsync -avz -e ssh root@192.168.159.128:/var/www/ /var/www/`, y vemos como el archivo `hola.html` que antes no existía en la **máquina 2** ha sido copiado desde la **máquina 1**:

![Captura2](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica2/Capturas/comprobacionRsync.png)

### Configuración ssh

Primero creamos las claves públicas y privadas en la **máquina 2**:

![Captura3](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica2/Capturas/creacionClave.png)

Luego enviamos la clave pública a la **máquina 1**:

![Captura4](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica2/Capturas/envioClavePublica.png)

Tras esto comprobamos en la **máquina 1** que exite tal clave:

![Captura5](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica2/Capturas/comprobacionenM1DeClave.png)

Y luego probamos que podemos ejecutar comandos sobre la **máquina 1** desde la **máquina 2**, mostrando el mismo archivo que hemos mostrado en la captura anterior:

![Captura6](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica2/Capturas/comprobacionComandosEnRemoto.png)

###  Configurar crontab

Vamos a añadir al fichero de configuración de **crontab** `/etc/crontab` de la **máquina 2** la siguiente linea, para la ejecución de **rsync** cada hora:

`00 * * * * root rsync -avz -e ssh root@192.168.159.128:/var/www/ /var/www/`

El fichero queda así:

![Captura7](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica2/Capturas/CrontabModificado.png)

