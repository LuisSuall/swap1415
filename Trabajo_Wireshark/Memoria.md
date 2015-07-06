#Wireshark: analizando el tráfico
##Gustavo Rivas Gervilla & Luis Suárez Lloréns

## Resumen:

En este trabajo analizaremos la herramienta Wireshark la cual nos permite analizar el tráfico que pasa por una red, filtrando los paquetes y mostrando información de gran interés y utilidad. En un primer lugar daremos una vista preliminar de la herramienta, a modo de tutorial, donde explicaremos sus distintas funcionalidades y modo de empleo. 

A continuación presentaremos algunos casos de uso que pueden ser de interés y por qué no que puede ser divertido probarlos: robar una wifi, detectar fallos en la seguridad o seguir la traza de un paquete a través de una granja web; para por ejemplo comprobar cómo funciona un determinado algoritmo de balanceo de carga.

## ¿Por qué hemos elegido este trabajo?

El análisis del tráfico de red es una tarea crucial en casi cualquier aplicación de informática que implique conexión a Internet o a una red local, en particular, es interesante para el mantenimiento de un granja web.

Son multitud las herramientas para tal propósito, libres o de pago, nosotros hemos querido usar esta herramienta puesto que es libre, está disponible para multitud de sistemas operativos y tiene un uso muy extendido. Pretendemos que el lector aprenda mientras lee este documento igual que hemos aprendido nosotros mientras lo hacíamos, y que así tenga una opción para estudiar su red y comprender mejor el funcionamiento de Internet.

## Breve reseña histórica:

En los 90 Gerald Combs estaba trabajando en un pequeño proveedor de Internet, como en aquella época los analizadores de tráfico eran demasiado caros y además no estaban disponibles para la plataforma que usaba su empresa (Solarys y Linux) Gerald decidió crear su propio analizador. Tras algunos parones en el desarrollo finalmente en julio de 1998 se lanzó la primera versión de Ethereal. Al poco tiempo ya comenzaron a llegar reportes sobre errores y opiniones de los usuario, comenzando así el camino hacia el éxito de esta herramienta.

No muy tarde Gilbert Ramirez vio el potencial de este proyecto y aportó un desegmentador de paquetes de bajo nivel que permite obtener la información contenida en los mismos. También Guy Harris vio en el Ethereal una gran herramienta y comenzó a contribuir al proyecto.

Ya a finales de 1998 Richard Sharpe que estaba dando cursos sobre TCP/IP vió que Ethernet no soportaba algunos protocolos con los que él necesitaba trabajar así que aportó el código necesario para ello. El número de personas que han aportaron algo es enorme.

Ya en 2006 la herramienta resurge bajo el nombre actual de Wireshark y en 2008 salió ya la versión 1.0 del mismo, que ya se consideraba completa con el mínimo necesario de características implementado. El lanzamiento coincidió con la primera conferencia para usuarios y desarrolladores llamada Sharkfest.

En 2010 Riverbed Technology compró CACE (la empresa para la que trabajaba Combs y bajo la que desarrolló Wireshark, que tuvo que cambiar el nombre ya que contaba con derechos sobre la mayoría del código de Ethereal pero no del nombre) y se convirtió en el primer sponsor de Wireshark. El desarrollo de Ethereal se ha detenido y la compañía que se encargaba de ello recomienda pasar a usar Wireshark.

Wireshark ha ganado multitud de premios incluyendo: eWeek, InfoWorld y PC Magazine. Además está en la cabeza del ranking de los rastreadores de paquetes en la web Insecure.org y fue el proyecto del mes para SourceForge en agosto de 2010.

Combs continúa con el desarrollo de Wireshark y hay alrededor de 600 desarrolladores que han aportado algo al proyecto.

Aquí tenemos un vídeo que muestra gráficamente cómo se fue desarrollando el proyecto: https://blog.wireshark.org/2010/02/the-history-of-wireshark-in-3-minutes/

## ¿Qué es Wireshark?

Wireshark es un analizador de paquetes gratuito y open source. La función de un analizador de paquetes es interceptar y registrar el tráfico que encontramos en nuestra red.

Su uso, como norma general, se centra en la solución de problemas en redes, utilizando la información obtenida para encontrar los problemas del sistema. También encontramos entre sus usos el desarrollo de software y de protocolos y la educación, pues es una herramienta perfecta para ver los protocolos y sistemas reales en funcionamiento.

Entre las características más importantes, nos encontramos que se encuentra disponible para plataformas con Linux, Windows y Mac, su robustez, el ser compatible con más de 480 protocolos, generación automática de estadísticas, permitir reconstruir sesiones TCP, versión para terminal (Tshark) y aceptar capturas de otros 20 productos más, aparte de las realizadas con el mismo Wireshark.

La característica clave es el filtrado. En una red normal, la cantidad de paquetes que pasan por una máquina es muy grande, tanto que puede hacer inmanejable los datos obtenidos con el software. Las herramientas de filtrado nos permiten acotar los resultados que vemos, para facilitar nuestro trabajo. Existen dos tipos, de captura y de visualización. El primero restringe los mensajes que recopila de la red, según unas condiciones. Los segundos muestran sólo una parte de los mensajes registrados. Es en esta característica en la que nos centraremos, en especial en los filtros de visualización.

De todas maneras, Wireshark carece de una serie de capacidades, por ser un analizador de paquetes, que podrían ser interesantes. Por ejemplo no detecta si hay alguien infiltrado en tu red, pero si se hace un uso extraño de la red, puedes intuir el problema. Tampoco permite manipular objetos de la red ni enviar paquetes, lo cual podría ser muy útil, tanto a un nivel profesional como en educación.

## Instalación:

Wireshark está disponible para Windows, Mac y Linux. En Windows y Mac bastará con descargar el instalador adecuado para nuestra arquitectura y lanzarlo, en la siguiente URL están todos los instaladores que están disponibles:

https://www.wireshark.org/download.html

Como podemos ver en la misma web tenemos disponibles los código fuente para UNIX con lo que podemos descargarlos y compilarlos. Nosotros vamos a presentar la instalación sencilla en Ubuntu, ya que Wireshark está disponible en los repositorios y basta con ejecutar la siguiente orden en la terminal:

`sudo apt-get install wireshark`

Con esto ya tendremos instalado Wireshark (a partir de aquí lo abreviaremos por WS) y podremos empezar a trabajar y aprender con él. 
Pasamos ya a los casos de uso con los que pretendemos dar el primer contacto con WS. Señalemos que los ejemplos y capturas que vamos a realizar serán sobre Ubuntu, en cualquier caso los conocimientos básicos que se pretenden transmitir serán aplicables al resto de plataformas



## Primer ejemplo de uso:

En este ejemplo simplemente vamos a mostrar una traza de tráfico de nuestra red, con el objetivo de aprender a escanear un red y mostrar la cantidad de paquetes que pueden pasar por nuestra red en un periodo de tiempo sorprendentemente corto.:

Lo primero que tenemos que notar es que cuando instalamos WS sólo el usuario root tendrá permisos para escanear las redes de nuestra máquina, si queremos el resto de usuarios puedan hacerlo tendremos que hacerlos nosotros a mano. Aquí tenemos una explicación de cómo realizar dicha configuración: 

http://anonscm.debian.org/viewvc/collab-maint/ext-maint/wireshark/trunk/debian/README.Debian?view=markup

Cuando lanzamos WS con permisos de escaneo, podemos ver una lista de todas las interfaces disponibles en nuestro ordenador: red Wi-Fi (wlan0), cable (eth0), todas las interfaces USB y una interfaz que es un compendio de todas las interfaces de nuestro sistema. Más adelante veremos también las redes internas creadas entre las distintas máquinas virtuales que hayamos configurado en nuestro ordenador (en nuestro caso aquellas que hayamos creado para las prácticas de la asignatura). La lista está en la sección Capture de la ventana principal y si pulsamos sobre Interfaces List tenemos una vista más extensa de dicha lista:

![Captura 1](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/listaInterfaces.jpeg)

Como podemos ver en la lista detallada nos muestra los paquetes que han pasado por cada interfaz durante el tiempo que hemos estado ejecutando WS y los paquetes/segundo, también nos permite ver las opciones para cada interfaz o comenzar a escanear la interfaz pulsando Start, también podemos hacer doble click sobre la interfaz que deseemos en la sección Capture. Aquí podemos ver el tráfico que ha pasado por mi tarjeta de red en un minuto:

![Captura 2](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/paquetesEnMinuto.png)

La cantidad de paquetes e información que recibimos es enorme, poco a poco aprenderemos a extraer los datos que nos interesen.

### Siempre vigilados:

Como podemos ver en la captura anterior el destino y la fuente son IPs, que no aportan demasiada información sobre con qué sitios web nos estamos comunicando, lo que vamos a hacer es habilitar una opción de WS la cual realiza la traducción de IPs a nombres de dominio. Para mostrar el uso de esta útil funcionalidad, vamos a ver cómo cuando accedemos por ejemplo a una tienda online, los servidores de Google están recabando datos sobre nuestras consultas, para sus propios intereses. 
Vamos a visitar la web http://www.kaskus.co.id y veamos los paquetes que escaneamos con WS, en primer lugar vamos a activar la opción que hemos mencionado en `Edit > Preferences > Name Resolution > Enable network name resolution`.

![Captura 3](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/opcionResolucionNombres.png)

Entonces con un sencillo filtrado podemos ver los paquetes que se generan cuando realizamos un consulta sobre algún producto de la tienda:

![Captura 4](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/kaskus.png)

Veamos ahora qué pasa si aplicamos el mismo filtro que antes pero buscando a google-analytics, es decir, el filtro será `http contains “google-analytics”`:

![Captura 5](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/espia.png)


Con lo cual, cada vez que realicemos alguna consulta a través de Google hemos de saber que estan recabando datos de nosotros, algo que tuvo mucho revuelo hace algún tiempo.

Nota: Es posible que cuando realicemos el filtrado anterior aparezcan paquetes pero con otro nombre de destino o fuente, realmente sigue siendo lo mismo.

### Filtrado de paquetes:

Aquí vamos a ver de una forma algo más completa la forma en que podemos filtrar paquetes. El filtrado de paquetes es una de las cosas más útiles e importantes que nos ofrece WS, ya hemos vistos en el ejemplo anterior la ingente cantidad de información que podemos recopilar en pocos minutos, lo que la hace inmanejable. Si por el contrario podemos filtrarla y obtener sólo aquella que nos interesa podremos realizar un análisis más eficiente y concreto. En general la sintaxis que siguen los filtros de WS es:

`<campo a filtrar> <relación a cumplir> <valor de referencia>`

donde:

*	campo a filtrar es el campo sobre el que aplicaremos la condición booleana que establezcamos, de modo que sólo se mostrarán aquellos paquetes que cumplan dicha condición.
*	relación a cumplir, es un operador que relaciona el campo al filtrar con el valor de referencia.
*	el valor de referencia es el valor con el que se compara el contenido de aquel campo del paquete indicado por campo de referencia.
Las distintas relaciones a cumplir son:

*	present = TRUE si el campo indicado está presente en el paquete
*	operadores relacionales: != , == , < , <=, >, >=.
*	contains = TRUE si el campo indicado contiene el valor o el rango de valores indicados en el valor de referencia.
*	matches = TRUE si el campo coincide totalmente con el valor de referencia indicado.

A lo largo del texto veremos algunos ejemplos de los distintos filtros que podemos aplicar. Ahora bien, hay multitud de campos y de protocolos a filtrar, con el uso continuado de WS aprenderemos aquellos que nos sean de mayor utilidad. Pero es muy difícil acordarse de todos, por suerte WS incorpora un menú que hace que la creación de filtros sea mucho más sencilla:

![Captura 6](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/menuFiltros.png)

En la ventana donde se muestran todos los paquetes que hemos filtrado tenemos esta barra llamada Filter donde podemos introducir el filtro que queramos aplicar (el recuado se pone verde cuando la sintaxis es correcta y rojo en caso contrario). Si pulsamos en el botón Expression… aparece la ventana que se muestra en esta captura. Como vemos tenemos una lista completa de todos los protocolos, y algunos como es el caso de HTTP tiene una lista desplegable con todos aquellos campos que tienen relación con él. Para movernos rápidamente por la lista podemos teclear el nombre del protocolo que deseemos, en nuestro caso hemos tecleado ‘HTTP’. Luego podemos seleccionar la relación que deseemos e introducir el valor de referencia en el cuadro Value, elegir uno de los valores de Predefined values o introducir un rango de valores en el cuadro Range.

De este modo podemos escribir filtros sin necesidad de conocer la sintaxis, sólo lo que queremos buscar.

### Robando contraseñas:

Hay algunas webs poco seguras, cada vez son menos las que son vulnerables a este tipo de acciones, pero en aquellas que sí lo sean podemos sacarle algo de partido a WS. Lo que vamos a hacer es visitar una web en la que hemos de ingresar un usuario y una contraseña, estos dos campos se enviarán en texto plano sin proteger, a través de un paquete POST que es el método HTTP mediante el cual enviamos datos a las web. Entonces encontraremos el paquete con esos datos enviados y podremos ver el usuario y la contraseña.

La web que vamos a visitar es http://cvg.ugr.es/ed_game/ y en ella vamos a introducir usuario = Sorpresa y contraseña = excelente. En la siguiente captura de pantalla podemos ver el filtro que hemos aplicado, lo hemos construido con el menú que hemos mostrado en el apartado anterior, y vemos que hay un paquete que se corresponde con nuestro patrón de búsqueda:

![Captura 7](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/robopasspaquete.png)

Ahora para encontrar la información que queremos no tenemos más que hacer click derecho sobre el paquete y seleccionar Follow TCP stream que no sólo mostrará la información contenida en el paquete si no que reconstruirá toda la sesión de envíos TCP a la que pertenece dicho paquete:

![Captura 8](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/followTCPSorpresaExcelente.jpeg)

Otro modo de acceder a esta información es haciendo doble click sobre el paquete, que también mostrará la información contenida de una forma más clara que la anterior:

![Captura 9](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/dobleclickSorpresaExcelente.jpeg)

Como vemos se nos muestra toda la información contenida en el paquete: el host, la URI de la petición y muchos datos más, que en esta ocasión no nos son de utilidad.

### Prácticas en funcionamiento:

Pasamos a continuación a analizar el funcionamiento de las distintas prácticas desarrolladas en la asignatura con WS. En primer lugar vamos a mostrar un esquema con la configuración de red interna que tenemos entre las distintas máquinas virtuales y nuestro ordenador, de modo que sea más sencillo interpretar los paquetes que capturemos (conociendo la IP en la red interna creada por VMware de cada máquina):

![Captura 10](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/confRedEsquema.jpeg)

Nota: En el esquema anterior hemos omitido la parte de la dirección IP 192.168 común a todas las máquina que conforman la red interna.

La red interna que conforman las máquina que hemos descrito, se identifica, en el caso de este ejemplo, con la interfaz vmnet8, así que será esta red la que escanearemos ahora con WS, igual que antes hemos escaneado la wlan0.

#### Práctica 2: Copia de carpeta

Si recordamos en la práctica dos usamos la herramienta rsync para poder copiar el contenido de un directorio de la Máquina 1 en la Máquina 2, programamos para ello una tarea con crontab de modo que cada x tiempo se copiase dicho contenido. 
Además establecimos un par de claves pública-privada de modo que una máquina pudiese conectarse a la otra sin tener que introducir una contraseña y de esta forma automatizar el copiado de la carpeta mediante un pequeño script.

En la siguiente captura podemos observar el intercambio de llaves al inicio de la conexión (señalado en verde) y también vemos como los tres primero paquetes de la traza se corresponden a las tres fases del Three-Way Handshake (señalado en azul):

![Captura 11](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/P2TWHSyIntercambioLlaves.jpeg)

Ahora vamos a ver simplemente un segmento de la traza donde se ve el continuo envío de paquetes TCP entre ambas máquinas como producto de la sincronización:

![Captura 12](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/P2intercambio.png)

Y por último vamos a ver cómo ambas máquinas (al final de la secuencia de copiado, que se repetirá cuando esté programada en el crontab) cierran su conexión TCP:

![Captura 13](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/P2FinDeConexion.png)

#### Práctica 3: Balanceador

Lo que vamos a ir haciendo es ver fragmento a fragmento la traza que sigue una petición originada en el host, viendo que el balanceador actúa como intermediario entre el usuario final y los servidores de datos.

![Captura 14](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/P3F1.png)

Los paquetes 1,2 y 3 son el Three-Way Handshake entre el host y el balanceador. En los paquetes 4 y 5 podemos ver la petición HTTP que hace el host al balanceador. Por último como podemos ver los dos últimos paquetes se corresponden con el protocolo ARP (este protocolo se encarga de traducir direcciones de la capa de red a direcciones de la capa de enlace, direcciones MAC), podemos ver cómo el balanceador pide la dirección de enlace de la Máquina2 y en el siguiente paquete recibe la respuesta.

Veamos la petición que hace el host al balanceador, que será la misma que haga el balanceador a la Máquina2, para ello hacemos doble click sobre el paquete HTTP correspondiente al GET, como ya hemos explicado anteriormente:

![Captura 15](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/P3peticion.png)

Como podemos ver se está pidiendo la página inicial del servidor.

![Captura 16](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/P3F2.png)

El esquema es el mismo que el visto entre el Host y el Balanceador, pero ahora el Balanceador actúa como Cliente y la Máquina2 como servidor. En el paquete 13 podemos ver como la Máquina2 le envía la página seleccionada al Balanceador y por ultimo ambas maquina cierran su conexión TCP.

Aquí tenemos la respuesta que contiene el paquete 13:

![Captura 17](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/P3respuesta.png)

Que como ya hemos dicho antes es la página por defecto del servidor.

![Captura 18](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/P3F3.png)

Por último tenemos el paquete de envio de la respuesta del Balanceador al Host así como el cierre de conexión (observemos que también hay dos paquetes correspondientes al cierre de conexión entre la Máquina2 y el Balanceador, el orden en que los vemos no siempre es el mismo).

#### Práctica 5: Maestro - Esclavo MySQL

A continuación vamos a ver cómo funciona la configuración maestro-esclavo que realizamos para la replicación de un base de datos. Aquí simplemente vamos a mostrar los mensaje que se envían comprobando cómo el esclavo le indica al maestro la acción que quiere realizar sobre la base de datos, de modo que ambas copias mantenga la consistencia:

![Captura 19](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/P5F1.png)

Vemos como la Máquina1 que actúa de maestro permite la conexión a la Máquina2 y a continuación la Máquina2 le envía a ésta a través de TCP la sentencia SQL que ha ejecutado, para ver qué sentencia a enviado hacemos click derecho sobre el paquete y seleccionamos Follow TCP Stream:

![Captura 20](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/P5sentenciaSQL.png)

Y como vemos lo que se ha hecho es borrar los Datos cuyo nombre sea ‘Pedro’.

#### Detectando un ataque de denegación de servicio:

A continuación vamos a ver cómo detectar o al menos sospechar si estamos sufriendo un ataque de denegación de servicio. Wireshark no nos va a avisar de ello pero sí que podemos notar algunas irregularidades en los paquetes que estamos enviando y recibiendo.

Vamos a hacer la simulación usando la herramienta httping3. Comentar que la herramienta está pensada para ayudar a analizar una red, no para un uso malintencionado como es nuestro caso. La sentencia `hping3 -c 50 -d 120 -S -w 64 -p 80 192.168.159.128` inicia una serie de handshakes con la máquina 1, pero el software de hping3, al recibir la respuesta de la máquina 1, responde con un mensaje a la máquina 1, diciendole que cancele la conexión. Para evitar esto, y poder simular de verdad un ataque básico DDOS, una solución sencilla es utilizar iptables para filtrar esos mensajes. Para ello podemos usar la orden `iptables -A OUTPUT -p tcp -d 192.168.159.128 -m tcp --tcp-flags RST RST -j DROP`.

Aquí tenemos la traza de la simulación:

![Captura 21](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/DDSF1.png)

Como podemos ver nuestro servidor está enviando una gran cantidad de paquetes de `[SYN, ACK]`, además si hacemos doble click en los paquetes que está enviando el Host podemos ver cómo envía el FLAG SYN, iniciando la conexión TCP:

![Captura 22](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/DDSSYN.jpeg)

Pero tras recibir el ACK no envía el tercer mensaje necesario para completar el Three-way Handshake, dejando una conexión abierta y así sucesivamente. Además podemos ver esquemáticamente este envio de paquetes con una opción que nos ofrece WS, no tenemos más que seleccionar un paquete y luego seleccionar de la pestaña Statistics la opción Flow graph… la cual muestra el envio de mensajes de forma gráfica:

![Captura 23](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/DDSTCPflow.png)

Elegimos la opción TCP flow para que sólo muestre el tráfico de paquetes TCP, y obtenemos lo siguiente al Aceptar:

![Captura 23](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/DDSflow.png)

Como hemos dicho no se llegan a completar las tres fases del acuerdo y la conexión TCP queda abierta. 

Pues bien, una vez que hemos detectado la IP que creemos que nos está atacando, una medida estándar es bloquearla en nuestro cortafuegos de modo que no pueda seguir enviándonos paquetes. WS ofrece una opción para crear reglas de cortafuegos a partir de los datos de un paquete, de modo que el administrador no tenga más que tomar dicha regla y añadirla a su cortafuegos, veamos en este caso cómo bloquear la IP del Host que es la que nos está atacando:

No tenemos más que seleccionar uno de los paquetes que nos ha enviado el Host, luego ir a Tools > Firewall ACL Rules. Aquí podemos elegir el tipo de dispositivo que tenemos, la IP que queremos que se vea afectada (la de origen o la de destino) y lo que queremos que se haga con dicha IP (en este caso denegarle el acceso):

![Captura 24](https://github.com/LuisSuall/swap1415/blob/master/Trabajo_Wireshark/Capturas/DDSRegla.png)

Si pulsamos Copiar tendremos la siguiente regla en nuestro portapapeles:

	! Cisco IOS (standard)
	access-list NUMBER deny host 192.168.159.1

Nota: En este caso aparece el host porque estamos trabajando con una red interna.

## Bibliografía:

Algunos libros de introducción a Wireshark:
http://proquest.safaribooksonline.com/9781783554638
http://proquest.safaribooksonline.com/9781593272661?uicode=goliat

http://bencore.ugr.es/iii/encore/record/C__Rb1916169__Swireshark__P0%2C12__Orightresult__X4;jsessionid=FBF1C1DC1DA97C116E74CEEAE23A1297?lang=spi&suite=pearl


¿Cómo robar contraseñas con Wireshark?
http://www.blackmoreops.com/2015/04/11/website-password-hacking-using-wireshark/
http://mile2.com/latest-news/password-hacking-with-wireshark.html

Aquí hay algunos vídeos en los que se ve como alguien analiza el tráfico usando Wiresharks y otras herramientas externas:
https://www.wireshark.org/docs/

Breve reseña histórica:
http://en.wikipedia.org/wiki/Wireshark#History
https://www.wireshark.org/docs/wsug_html/#ChIntroHistory

Siguiendo tráfico TCP con Wireshark:

https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowTCPSection.html
http://www.binarytides.com/sniff-http-form-post-data-wireshark/
https://www.youtube.com/watch?v=XmbMrStH630

Para capturar el tráfico a través de una red de máquinas virtuales:

https://ask.wireshark.org/questions/41843/live-traffic-capture-of-two-vms-running-in-virtualbox
http://superuser.com/questions/836146/capture-network-traffic-between-vms-virtualbox-using-wireshark
https://ask.wireshark.org/questions/755/wireshark-with-virtual-box


http://www.howtogeek.com/106191/5-killer-tricks-to-get-the-most-out-of-wireshark/

http://null-byte.wonderhowto.com/how-to/spy-your-buddys-network-traffic-intro-wireshark-and-osi-model-0133807/

https://evilzone.org/tutorials/basic-forensics-with-wireshark/
http://www.techrepublic.com/blog/linux-and-open-source/using-the-flow-graph-feature-on-wireshark/

https://www.incibe.es/CERT/guias_estudios/guias/guia_wireshark

http://www.blackmoreops.com/2015/04/21/denial-of-service-attack-dos-using-hping3-with-spoofed-ip-in-kali-linux/


Robando contraseñas:

http://tipstrickshack.blogspot.com.es/2012/10/how-to-sniff-http-post-password-via.html

Pequeño cheatset de los filtros que podemos aplicar en Wireshark:

https://seguridadyredes.wordpress.com/2008/03/24/analisis-de-red-con-wireshark-filtros-de-captura-y-visualizacian/



