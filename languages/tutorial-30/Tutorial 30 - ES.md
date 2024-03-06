Tutorial 30 - ES

Título - Enviar NFT con Fleet SDK
Descripción - Enviaremos un nft utilizando Fleet-sdk y una pequeña aplicación escrita con Chakra y typescript.

1 - En este tutorial enviaremos un nft utilizando Fleet-sdk y una pequeña aplicación escrita con Chakra y typescript. Para este tutorial debes disponer de la cartera Nautilus, algo de saldo en ERG y el NFT que quieras enviar.

2 - Vamos a crear un mini sitio web que generará una transacción con la que realizaremos el envío de un NFT a otra cartera.

3 - No explicaré nada del código porque no puede estar mejor explicado en el sitio de FleetSDK, desde este tutorial únicamente encajaremos algunas piezas que pueden resultar complicadas si nunca jugaste con este tipo de aplicaciones.

4 - Lo primero será crear nuestra aplicación con Chakra y Create React App desde un terminal.

npx create-react-app sendnft --template @chakra-ui/typescript

5 - Ahora instalaremos la increíble librería Fleet-sdk.

npm install @fleet-sdk/core

6 - Puedes ver toda la documentación en su sitio web. 

https://fleet-sdk.github.io/docs/

7 - Una vez creada la estructura nos colocamos en el directorio de nuestra aplicación y la ejecutamos por primera vez.

cd sendnft
npm start

8 - Podemos ver que se abre una ventana de nuestro navegador con la aplicación en funcionamiento. Por el momento no hace nada, únicamente la imagen por defecto da vueltas.

localhost:3000

9 - Ahora vamos a realizar algunas modificaciones en el código de nuestra aplicación. Usaremos el archivo App.tsx dentro de la carpeta src.

/src/App.tsx

10 - Yo realizaré estas modificaciones detrás del vídeo para que no se alargue mucho y en el enlace a Github lo puedes copiar y pegar en tu proyecto. Recuerda que debes modificar la wallet de destino y el id del token que quieras enviar.

https://github.com/ladopixel/fleet-sdk-sendnft

11 - Entre las líneas de código añadidas podemos distinguir lo siguiente:

import { OutputBuilder, TransactionBuilder } from "@fleet-sdk/core";

12 - Hacemos algunas declaraciones. 

13 - Estoy seguro que se podrán hacer de forma más correcta, estoy poco familiarizado con typescript.

declare global {
      interface Window {
          ergoConnector: any;
      }
}
declare var ergo: any;
var connected: any;

14 - La función que hace la magia de enviar nuestro NFT.

    async function send_token(): Promise<void> { 
      connected = await window.ergoConnector.nautilus.connect(); 
      if (connected) {
        const height = await ergo.get_current_height();
        const unsignedTx = new TransactionBuilder(height)
          .from(await ergo.get_utxos())
          .to(
            new OutputBuilder(
              "1000000", "9gBYZrMRNX66uN5VhLnTw6absspsarXPxcWSi5fuE5EesBfQC6s"
            )
            .addTokens({ 
              tokenId: 
                "bb010d9816e8371b6d3889eb2afeecfd8d79c391aa2ed2ff908774a9f3e32c2d",
              amount: "1", 
            }) 
          )
          .sendChangeTo(await ergo.get_change_address())
          .payMinFee()
          .build()
          .toEIP12Object();
        const signedTx = await ergo.sign_tx(unsignedTx);
        const txId = await ergo.submit_tx(signedTx);
        setTx(txId);
      }
    }

15 - Actualizamos nuestro navegador o ejecutamos nuevamente la aplicación.

npm start

