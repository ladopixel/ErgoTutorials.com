Tutorial 23 - ES

Título - Nodo Ergo con Mac
Descripción - En este tutorial veremos cómo ejecutar el nodo de Ergo con Mac.
JDK/JRE: https://www.oracle.com/technetwork/java/javase/overview/index.html
Repositorio Ergo: https://github.com/ergoplatform/ergo/releases/
Hash Blake2b: 127.0.0.1:9053/swagger#/utils/hashBlake2b
Información para Raspberry Pi: https://docs.ergoplatform.com/node/install/pi/
Si quieres ver más tutoriales sobre Ergo visita: https://ergotutorials.com/


1 - En este tutorial veremos cómo ejecutar el nodo de Ergo. Antes de nada debemos saber que para ejecutar un nodo de Ergo en nuestro equipo no hace falta ser un ninja de la programación ni un mago alquimista. Tampoco tener un ordenador de la NASA ni conocimientos de ErgoScript o Scala. Con una Raspberry Pi y este sencillo tutorial es suficiente. Sí, es correcto lo que estás pensando, poder correr este nodo en una Raspberry Pi es increíble. Ergo es increíble.


2 - Para correr el nodo en nuestro sistema debemos tener instalado una versión de JDK/JRE superior a la 9 (enlace de descarga https://www.oracle.com/technetwork/java/javase/overview/index.html), se instala como cualquier programa en tu equipo. 

3 - Podemos verificar la correcta instalación mirando la versión desde consola.

4 - Una vez instalado vamos al repositorio Ergo para descargar la versión más reciente del nodo.
https://github.com/ergoplatform/ergo/releases/

5 - Vamos a crear una carpeta llamada Ergo Nodo en nuestro escritorio y copiamos el archivo que acabamos de descargar del repositorio.
ergo-4.0.27.jar

6 - Ahora crearemos un archivo llamado ergo.conf y copiaremos estas líneas de código en su interior.

ergo {
    node {
        mining = false
    }
}

7 - Con este archivo creado ejecutaremos nuestro nodo por primera vez, situándonos en la carpeta que hemos creado, podremos escribirlo de dos formas diferentes:

"java -jar ergo-<release>.jar --mainnet -c ergo.conf" una para no establecer ningún límite, como vemos en la parte superior y otra forma "java -jar -Xmx4G ergo-<release>.jar --mainnet -c ergo.conf" si queremos establecer un límite de 4GB, como vemos en la parte inferior.


8 - <release> tendremos que sustituirlo por la versión del nodo que hayamos descargado del repositorio, en nuestro caso quedaría de la siguiente forma: java -jar -Xmx4G ergo-4.0.27.jar --mainnet -c ergo.conf

9 - Una vez que tenemos nuestro nodo en funcionamiento, pasaremos a darle seguridad eligiendo una palabra y pasándole la función hash Blake2b como aparece en el vídeo. 

10 - Abrimos un navegador y nos dirigimos a la siguiente URL: 127.0.0.1:9053/swagger#/utils/hashBlake2b

11 - El resultado que genere no se debe compartir con nadie.

12 - Detenemos el nodo.

13 - Copiamos el resultado que hemos generado anteriormente en nuestro archivo de configuración ergo.conf, junto a otros parámetros.
Quedando como resultado algo parecido a esto:

ergo {
	Directory = ${ergo.directory}"/.ergo"
     	node {
        	mining = false
      	}
	Wallet.secretStorage.secretDir = ${ergo.directory}"/wallet/keystore"
}

scorex {
	restApi {
        	apiKeyHash = "Tu resultado generado"
	}
}

14 - Una vez que hemos modificado nuestro archivo de configuración, arrancamos nuevamente el nodo.

15 - Con nuestro archivo de configuración actualizado y el nodo en funcionamiento nos dirigimos a la siguiente URL: 127.0.0.1:9053/panel 

16 - Podemos ver el interface de nuestro nodo y que la sincronización está en proceso.

17 - Configuramos la API key. En este valor introduciremos la palabra a la que le pasamos anteriormente la función hash Blake2b.

18 - Si todo está correcto nos mostrará una alerta indicando que la API key se ha configurado correctamente.

19 - Desde este panel podemos inicializar una wallet, ya sea creando una nueva o restaurando una que tengamos creada anteriormente. 
Nosotros crearemos una nueva.

20 - Para crear esta billetera lo único que introduciremos será una contraseña y hacemos click en enviar. Existe la posibilidad de agregar seguridad añadiendo una contraseña mnemotécnica.

21 - Nos aparecerá un mensaje indicando que se ha inicializado correctamente junto a nuestra frase semilla. Recuerda copiar en papel y mantener en secreto esta frase semilla.

22 - Para ver el estado de nuestra wallet únicamente debemos seleccionar en el panel de nuestro nodo la opción Wallet e introducir la contraseña con la que la hemos configurado anteriormente.

23 - La sincronización de nuestro nodo se puede demorar algún tiempo si queremos sincronizarlo de forma completa. 
Para hacer esto más liviano, por ejemplo para que funcione más fluido en una Raspberry Pi, existe la posibilidad de agregar algunos parámetros a nuestro archivo de configuración, quedando de la siguiente forma:

ergo {
  directory = ${ergo.directory}"/.ergo"
  node {
    mining = false
    skipV1TransactionsValidation = true
    blocksToKeep = 1440
    stateType = digest
  }
  Wallet.secretStorage.secretDir = ${ergo.directory}"/wallet/keystore"
}

scorex {
  restApi {
    apiKeyHash = "Tu resultado generado"
  }
  network {
    maxConnections = 10
  }
}

24 - Una vez que tengamos nuestro archivo modificado arrancamos nuevamente el nodo, podremos ver que se sincroniza en mucho menos tiempo. Crearemos una nueva billetera para dejar todo bien sincronizado.