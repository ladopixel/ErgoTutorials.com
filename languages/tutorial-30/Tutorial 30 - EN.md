Tutorial 30 - EN

Título - Send NFT with Fleet SDK
Descripción - We will send an NFT using Fleet-sdk and a small application written with Chakra and typescript.

1 - In this tutorial we will send an NFT using Fleet-sdk and a small application written with Chakra and typescript.
For this tutorial you must have the Nautilus wallet, some balance in ERG and the NFT you want to send.

2 - We are going to create a mini website that will generate a transaction with which we will send an NFT to another wallet.

3 - I will not explain any of the code because it can not be better explained in the FleetSDK site, from this tutorial we will only fit some pieces that can be complicated if you never played with this type of applications.

4 - The first thing to do is to create our application with Chakra and Create React App from a terminal.

npx create-react-app sendnft --template @chakra-ui/typescript

5 - Now we will install the amazing Fleet-sdk library.

npm install @fleet-sdk/core

6 - You can see all the documentation on their website.

https://fleet-sdk.github.io/docs/

7 - Once the structure is created we place it in the directory of our application and we execute it for the first time.

cd sendnft
npm start

8 - We can see that a browser window opens with the application running. At the moment it does nothing, only the default image is spinning.

localhost:3000


9 - Now we are going to make some modifications in the code of our application. We will use the App.tsx file inside the src folder.

/src/App.tsx

10 - I will make these modifications behind the video so that it does not take too long and in the link to Github you can copy and paste it into your project. Remember to modify the destination wallet and the id of the token you want to send.

https://github.com/ladopixel/fleet-sdk-sendnft

11 - Among the lines of code added we can distinguish the following:

import { OutputBuilder, TransactionBuilder } from "@fleet-sdk/core";

12 - We make some declarations.

13 - I'm sure they can be done more correctly, I'm not very familiar with typescript.

declare global {
      interface Window {
          ergoConnector: any;
      }
}
declare var ergo: any;
var connected: any;

14 - The function that does the magic of sending our NFT.

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

15 - We refresh our browser or run the application again.

npm start

