Tutorial 23 - EN

Title - Ergo node with Mac
Description - In this tutorial we will see how to run the Ergo node with Mac.
JDK/JRE: https://www.oracle.com/technetwork/java/javase/overview/index.html
Repository Ergo: https://github.com/ergoplatform/ergo/releases/
Hash Blake2b: 127.0.0.1:9053/swagger#/utils/hashBlake2b
Information for Raspberry Pi: https://docs.ergoplatform.com/node/install/pi/
If you want to see more tutorials about Ergo visit: https://ergotutorials.com/


1 - In this tutorial we will see how to run the Ergo node. First of all we must know that to run an Ergo node on our computer we don't need to be a programming ninja or an alchemist magician. Nor do you need to have a NASA computer or knowledge of ErgoScript or Scala. With a Raspberry Pi and this simple tutorial is enough. Yes, that's right what you are thinking, being able to run this node on a Raspberry Pi is amazing. Ergo is amazing.


2 - To run the node on our system we must have a JDK/JRE version higher than 9 installed (download link https://www.oracle.com/technetwork/java/javase/overview/index.html), is installed like any other program on your computer. 

3 - We can verify the correct installation by looking at the version from the console.

4 - Once installed we go to the Ergo repository to download the latest version of the node.
https://github.com/ergoplatform/ergo/releases/

5 - Let's create a folder called Ergo Node on our desktop and copy the file we just downloaded from the repository.
ergo-4.0.27.jar

6 - We will now create a file called ergo.conf and copy these lines of code into it.

ergo {
    node {
        mining = false
    }
}

7 - With this created file we will execute our node for the first time, placing ourselves in the folder that we have created, we can write it in two different ways: One to not establish any limit, as we see at the top and another way if we want to establish a limit of 4GB, as we see at the bottom.

8 - <release> we will have to replace it with the version of the node that we have downloaded from the repository, in our case it would be as follows: java -jar -Xmx4G ergo-4.0.27.jar --mainnet -c ergo.conf

9 - Once we have our node up and running, we'll go on to make it secure by choosing a word and passing it the Blake2b hash function as shown in the video.

10 - We open a browser and go to the following URL: 127.0.0.1:9053/swagger#/utils/hashBlake2b

11 - The result you generate should not be shared with anyone.

12 - We stop the node.

13 - We copy the result that we have generated previously in our configuration file, along with other parameters. The result is something similar to this:

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

14 - Once we have modified our configuration file, we start the node again.

15 - With our configuration file updated and the node running, we go to the following URL: 127.0.0.1:9053/panel 

16 - We can see the interface of our node and that the synchronization is in progress.

17 - We configure the API key. In this value we will introduce the word to which we previously passed the Blake2b hash function.

18 - If everything is correct, it will show us an alert indicating that the API key has been configured correctly.

19 - From this panel we can initialize a wallet, either creating a new one or restoring one that we have previously created.
We will create a new one.

20 - To create this wallet, the only thing we will enter is a password and click on send. There is the possibility of adding security by adding a mnemonic password.

21 - A message will appear indicating that it has been initialized correctly next to our seed phrase. Remember to copy on paper and keep this seed phrase secret.

22 - To see the status of our wallet, we only have to select the Wallet option in the panel of our node and enter the password with which we have previously configured it.

23 - The synchronization of our node can take some time if we want to synchronize it completely.
To make this lighter, for example to make it work more fluidly on a Raspberry Pi, there is the possibility of adding some parameters to our configuration file, being as follows:

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

24 - Once we have our modified file, we start the node again, we will be able to see that it is synchronized in much less time. We will create a new wallet to get everything well synchronized.
