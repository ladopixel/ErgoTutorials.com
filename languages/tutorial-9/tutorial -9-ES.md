Tutorial 9 - ES

Título - Crea mini web para tu NFT
Descripción - En este tutorial vamos a crear un mini sitio web para mostrar el NFT que más te guste.
Github: https://github.com/ladopixel/ErgoTutorials.com/tree/master/tutorial-2
Ergo Tokens: https://ergotokens.org/
Si quieres ver más tutoriales sobre Ergo visita: https://ergotutorials.com/

1 - En este tutorial vamos a crear un mini sitio web que muestre un NFT del blockchain de Ergo. Solo vamos a necesitar crear 2 archivos: 1 index.html y otro muy sencillo de javascript.

2 - Lo primero que haremos será crear un archivo con estructura HTML5.

3 - Agregamos el CSS de Bootstrap para poder dar forma a nuestra Card de forma sencilla y rápida.

4 - Modificamos el título.

5 - En el sitio web de Bootstrap copiamos la estructura de Card y la modificamos según nuestras necesidades. Voy a incluir una imagen, un botón y algunos párrafos para los datos que rescatemos.

6 - Añadimos nuestro archivo .js

7 - Desde el body llamaremos a la función getInfoToken() mediante un onLoad.

8 - En el archivo javascript rescataremos algunos valores del blockchain de Ergo mediante una sencilla consulta a su API Explorer.

9 - Necesitaremos el ID del NFT a mostrar, voy al sitio web de ErgoTokens.org para buscarlo. Si ya conoces el ID de tu token puedes omitir este paso.

10 - En el archivo javascript creamos la función getInfoToken() y almacenamos el ID en una variable.

11 - Ahora realizaremos una consulta a la API Explorer de Ergo.

12 - Para esta consulta utilizaremos el endpoint y la variable en la que hemos almacenado el ID de nuestro token.

13 - Mostramos los datos recibidos en consola para verificar que nuestra consulta está correcta.

14 - Observamos el resultado y vemos cuales son los valores que nos hacen falta para mostrar nuestra Card del NFT.

15 - Creamos 4 variables para almacenar la información del token.

16 - Guardamos en cada variable el resultado que nos devuelve la API.

17 - Algunos de los valores que recibimos están codificados, aquí puedes ver un poco más a fondo las diferentes codificaciones para este tipo de tokens.

18 - Agregamos una función para decodificar los valores que nos devuelve la API y poderlos entender correctamente.

19 - La ruta de la imagen, el título y la descripción de nuestro token deben ser decodificados mediante la función.

20 - Aunque la ruta de la imagen ha quedado decodificada, desde el último cambio que se realizó para el almacenamiento IPFS, para que nos muestre la ruta correcta debemos pasarle otra función llamada resolveIpfs que ha sido creada por Anon_real. Gracias a esta función se mostrarán correctamente las imágenes independientemente del tipo de almacenamiento que tenga.

21 - Le pasamos la función a la ruta de nuestra imagen.

22 - Ahora únicamente tendríamos que visualizar el contenido de nuestras variables en los diferentes elementos HTML de nuestra Card. Haremos referencia a ellos mediante su ID.

23 - Vamos al navegador para ver el resultado y podremos ver una ficha de nuestro NFT.

24 - Recuerda que el código de este tutorial puedes descargarlo de Github, el enlace lo tienes en la descripción del vídeo y en ErgoTutorials.com.
