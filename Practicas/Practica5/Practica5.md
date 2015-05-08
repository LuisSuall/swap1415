#Práctica 5

##Creación de la base de datos

Para empezar la realización de la práctica, primero vamos a crear una base de datos de prueba:

![Captura 1](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica5/Capturas/baseDatosInicial.png)

No hace falta una base de datos más complicada para la realización de esta práctica, pues lo importante no es la base de datos en si, si no su cunfiguración. Vamos a pasar a replicarla en una segunda máquina.

##Replicar una BD MySQL con mysqldump

Primero bloqueamos la BD.

![Captura 2](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica5/Capturas/bloqueoBD.png)

Tras esto, copiamos los datos de la BD.

![Captura 3](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica5/Capturas/copiaBD.png)

Y volvemos a desbloquear las tablas.

![Captura 4](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica5/Capturas/desbloqueoBD.png)

Ahora vamos a pasar a copiar los datos que hemos pasado al fichero sql dentro de la máquina que actuará como esclavo:

![Captura 5](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica5/Capturas/transferenciaDatosBD.png)

Vamos a pasar a continuación a crear una base de datos en la máquina esclavo donde cargaremos los datos que hemos importado desde la maestro.

Primero hemos creado, del mismo modo que antes, una base de datos llamada Contactos y luego hemos cargado los datos importados con la sentencia:

`mysql -u root -p contactos < /root/contactosdb.sql`

Podemos ver que todo ha funcionado correctamente mostrando los datos que hemos cargado en la máquina esclava:

![Captura 6](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica5/Capturas/comprobacionCopia.png)

##Replicación de BD mediante una configuración maestro-esclavo

Para ello, primero modificamos el archivo `/etc/mysql/my.cnf` generado por defecto modificando, comentando o añadiendo, en caso de no existir, las siguientes lineas:

	#bind-address 127.0.0.1
	log_error = /var/lg/mysql/error.log
	server-id = 1
	log_bin = /var/log/mysql/bin.log

Y tras esto, guardamos los cambios y reiniciamos el servicio:

![Captura 7](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica5/Capturas/reinicioTrasConfMaestro.png)

Realizamos el mismo proceso con el servidor esclavo, pero asignandole un identificador de servidor distinto, el 2, por ejemplo. Guardamos los cambios y también lo reiniciamos:

![Captura 8](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica5/Capturas/reinicioTrasConfEsclavo.png)

Volvemos a la máquina maestra, y creamos en mysql un nuevo usuario, y le damos permisos de replicación:

![Captura 9](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica5/Capturas/userEsclavo.png)

Y tras esto realizamos, en la misma máquina, la siguiente sentencia:

![Captura 10](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica5/Capturas/masterStatus.png)

Ahora, volvemos a la máquina esclava, para configurar el uso de la cuenta que acabamos de crear:

![Captura 11](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica5/Capturas/datosEsclavo.png)

Desbloqueamos las tablas en el maestro, y vemos si funciona correctamente el sistema:

![Captura 12](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica5/Capturas/ERROR.png)

No funciona correctamente, y por lo que indica el registro de error, no se ha realizado correctamente la creación del usuario 'esclavo'. Volvemos a repetir el proceso para su creación, modificando con los nuevos datos la información de la máquina esclava. Tras esto, el sistema funciona correctamente:

![Captura 13](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica5/Capturas/arreglado.png)

Realizamos una comprobación final, introduciendo una nueva tupla en la máquina maestra y viendo como, efectivamente, se copia en la máquina esclava:

![Captura 14](https://github.com/LuisSuall/swap1415/blob/master/Practicas/Practica5/Capturas/comprobacionFinal.png)
