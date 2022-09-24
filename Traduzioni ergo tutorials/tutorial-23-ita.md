Tutorial 23 - ita

Titolo - nodo ergo con Mac
Descrizione - In questo tutorial vedremo come eseguire il nodo Ergo con Mac.
JDK/JRE: https://www.oracle.com/technetwork/java/javase/overview/index.html
Repository ergo: https://github.com/ergoplatform/ergo/releases/
HASH BLAKE2B: 127.0.0.1:9053/Swagger#/utils/Hashblake2b
Informazioni per Raspberry Pi: https://docs.ergoplatform.com/node/install/pi/
Se vuoi vedere altri tutorial su Ergo Visit: https://ergotorials.com/


1 - In questo tutorial vedremo come eseguire il nodo Ergo. Prima di tutto dobbiamo sapere che per eseguire un nodo Ergo sul nostro computer non abbiamo bisogno di essere un ninja di programmazione o un mago alchimista. Né devi avere un computer NASA o una conoscenza di ErgScript o Scala. Con un Raspberry Pi e questo semplice tutorial è sufficiente. Sì, è vero quello che stai pensando, essere in grado di eseguire questo nodo su un Raspberry Pi è fantastico. Ergo è fantastico.


2 - Per eseguire il nodo sul nostro sistema dobbiamo avere una versione JDK/JRE superiore a 9 installata (Download Link https://www.oracle.com/technetwork/java/javase/overview/index.html) Qualsiasi altro programma sul tuo computer.

3 - Possiamo verificare l'installazione corretta osservando la versione dalla console.

4 - Una volta installato andiamo al repository Ergo per scaricare l'ultima versione del nodo.
https://github.com/ergoplatform/ergo/releases/

5 - Creiamo una cartella chiamata Ergo Node sul nostro desktop e copia il file che abbiamo appena scaricato dal repository.
ergo-4.0.27.jar

6 - Ora creeremo un file chiamato ergo.conf e copiemo queste righe di codice in esso.

ergo {
    nodo {
        mining = false
    }
}

7 - Con questo file creato eseguiremo il nostro nodo per la prima volta, posizionandoci nella cartella che abbiamo creato, possiamo scriverlo in due modi diversi: uno per non stabilire alcun limite, come vediamo in alto e un altro modo se vogliamo stabilire un limite di 4 GB, come vediamo in fondo.

8 -<Selesa> Dovremo sostituirlo con la versione del nodo che abbiamo scaricato dal repository, nel nostro caso sarebbe il seguente: Java -jar -xmx4g ergo -4.0.27.jar -mainnet - C ergo.conf

9 - Una volta che abbiamo il nostro nodo attivo e funzionante, continueremo a renderlo sicuro scegliendo una parola e passandola la funzione hash Blake2B come mostrato nel video.

10 - Apriamo un browser e andiamo al seguente URL: 127.0.0.1:9053/swagger#/utils/hashblake2b

11 - Il risultato che genera non dovrebbe essere condiviso con nessuno.

12 - Fermiamo il nodo.

13 - Copiamo il risultato che abbiamo generato in precedenza nel nostro file di configurazione, insieme ad altri parametri. Il risultato è qualcosa di simile a questo:

ergo {
Directory = $ {ergo.directory} "/. Ergo"
     nodo {
        mining = false
      }
Wallet.secretStorage.secretdir = $ {ergo.directory} "/wallet/keystore"
}

SCOPEX {
Ristapi {
        ApikeyHash = "Tuo Risultato"
}
}

14 - Una volta modificato il nostro file di configurazione, avviamo di nuovo il nodo.

15 - Con il nostro file di configurazione aggiornato e il nodo in esecuzione, andiamo al seguente URL: 127.0.0.1:9053/Panel

16 - Possiamo vedere l'interfaccia del nostro nodo e che la sincronizzazione è in corso.

17 - Configuriamo la chiave API. In questo valore introdurremo la parola a cui in precedenza abbiamo superato la funzione hash Blake2B.

18 - Se tutto è corretto, ci mostrerà un avviso che indica che la chiave API è stata configurata correttamente.

19 - Da questo pannello possiamo inizializzare un portafoglio, creando uno nuovo o ripristinando uno che abbiamo precedentemente creato.
Ne creeremo uno nuovo.

20 - Per creare questo portafoglio, l'unica cosa in cui inseriremo è una password e fare clic su Invia. Esiste la possibilità di aggiungere sicurezza aggiungendo una password mnemonica.

21 - Verrà visualizzato un messaggio che indica che è stato inizializzato correttamente accanto alla nostra frase di semi. Ricorda di copiare su carta e mantenere segreta questa frase di semi.

22 - Per vedere lo stato del nostro portafoglio, dobbiamo solo selezionare l'opzione del portafoglio nel pannello del nostro nodo e inserire la password con cui abbiamo precedentemente configurato.

23 - La sincronizzazione del nostro nodo può richiedere del tempo se vogliamo sincronizzarlo completamente.
Per rendere questo più leggero, ad esempio per farlo funzionare in modo più fluido su un Raspberry Pi, c'è la possibilità di aggiungere alcuni parametri al nostro file di configurazione, essendo il seguente:

ergo {
  Directory = $ {ergo.directory} "/. ergo"
  nodo {
    mining = false
    skipv1TransactionSValidation = true
    BlockStokeep = 1440
    StateType = Digest
  }
  Wallet.secretStorage.secretdir = $ {ergo.directory} "/wallet/keystore"
}

SCOPEX {
  Ristapi {
    ApikeyHash = "Tu Risadolo Generado"
  }
  Rete {
    maxconnections = 10
  }
}

24 - Una volta che abbiamo il nostro file modificato, ricominciamo il nodo, saremo in grado di vedere che è sincronizzato in molto meno tempo. Creeremo un nuovo portafoglio per ottenere tutto bene sincronizzato.
