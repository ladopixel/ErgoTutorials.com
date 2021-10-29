Tutorial 1 - ES


1 - En este tutorial vamos a rescatar algunos valores del blockchain de Ergo. Utilizaremos una sencilla función para consultar la versión 1 de Ergo Explorer API.

2 - Vamos a ver cómo con muy pocas líneas de código y conocimientos muy básicos de HTML y JavaScript, podremos interactuar con el blockchain de Ergo. 

3 - Lo primero que haremos será crear un archivo con una estructura HTML5 llamado index.html. Modificaremos su título, desde su etiqueta body llamaremos a la función heightCreation() mediante un onload y agregaremos un archivo Javascript llamado getInfo.js que crearemos posteriormente.

3.1 - Modificamos el título.

3.2 - Llamamos a la función con onload.

3.3 - Incluimos nuestro archivo Javascript.

4 - Ahora vamos a crear la función Javascript para recibir los valores del blockchain de Ergo mediante su API.

5 - Para nuestra función utilizaremos un endpoint que será el encargado de facilitarnos la información que necesitamos. El endpoint es el siguiente.

6 - Los valores que recibiré de la API los vamos a mostrar en la consola mediante console.log.

7 - Desde la consola de nuestro navegador podemos ver que la respuesta de la API nos devuelve los datos correctamente, hacemos la comparación con la documentación.

8 - Ahora agregaremos una línea más de código para utilizar uno de los valores recibidos y colorear el fondo de nuestro sitio web, este color lo definirá la altura de bloque actual.

9 - Con esta última línea ya tenemos nuestro ejemplo terminado. Ahora vamos al navegador y actualizamos para observar cómo el fondo de nuestro sitio web cambia de color y toma el color de la altura de bloque actual de Ergo.

10 - El código de este tutorial lo puedes descargar desde Github.

