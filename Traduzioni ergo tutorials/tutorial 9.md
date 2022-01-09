Tutorial 9 - IT

Titolo - Crea mini web per il tuo NFT

Descrizione - In questo tutorial creeremo un mini sito Web per mostrare l'NFT che ti piace di più.
Github: https://github.com/ladopixel/ErgoTutorials.com/tree/master/tutorial-2
Gettoni Ergo: https://ergotokens.org/
Se vuoi vedere altri tutorial su Ergo visita: https://ergotutorials.com/

1 - In questo tutorial creeremo un mini sito web che mostra un NFT della blockchain di Ergo. Dovremo solo creare 2 file: 1 index.html e un altro file javascript molto semplice.

2 - La prima cosa che faremo è creare un file con struttura HTML5.

3 - Abbiamo aggiunto il CSS Bootstrap per poter modellare la nostra Card in modo facile e veloce.

4 - Abbiamo modificato il titolo.

5 - Sul sito Bootstrap copiamo la struttura della Card e la modifichiamo secondo le nostre esigenze. Includerò un'immagine, un pulsante e alcuni paragrafi per i dati che salviamo.

6 - Aggiungi il nostro file .js

7 - Dal body chiameremo la funzione getInfoToken() tramite un onLoad.

8 - Nel file javascript salveremo alcuni valori dalla blockchain di Ergo tramite una semplice query al suo API Explorer.

9 - Avremo bisogno dell'ID dell'NFT da visualizzare, vado sul sito ErgoTokens.org per cercarlo. Se conosci già l'ID del tuo token puoi saltare questo passaggio.

10 - Nel file javascript creiamo la funzione getInfoToken() e memorizziamo l'ID in una variabile.

11 - Ora faremo una query all'Ergo API Explorer.

12 - Per questa query utilizzeremo l'endpoint e la variabile in cui abbiamo memorizzato l'ID del nostro token.

13 - Mostriamo i dati ricevuti nella console per verificare che la nostra query sia corretta.

14 - Osserviamo il risultato e vediamo di quali valori abbiamo bisogno per visualizzare la nostra carta NFT.

15 - Creiamo 4 variabili per memorizzare le informazioni sui token.

16 - Archiviamo in ogni variabile il risultato restituito dall'API.

17 - Alcuni dei valori che riceviamo sono codificati, qui puoi dare un'occhiata più da vicino alle diverse codifiche per questo tipo di token.

18 - Aggiungiamo una funzione per decodificare i valori restituiti dall'API in modo da comprenderli correttamente.

19 - Il percorso dell'immagine, il titolo e la descrizione del nostro token devono essere decodificati dalla funzione.

20 - Sebbene il percorso dell'immagine sia stato decodificato, dall'ultima modifica apportata per l'archiviazione IPFS, per mostrarci il percorso corretto dobbiamo passare un'altra funzione chiamata resolveIpfs che è stata creata da Anon_real. Grazie a questa funzione le immagini verranno visualizzate correttamente indipendentemente dal tipo di memoria che hai.

21 - Passiamo la funzione al percorso della nostra immagine.

22 - Ora non ci resta che visualizzare il contenuto delle nostre variabili nei diversi elementi HTML della nostra Card. Ci riferiremo a loro tramite il loro ID.

23 - Andiamo nel browser per vedere il risultato e potremo vedere una scheda della nostra NFT.

24 - Ricorda che il codice per questo tutorial può essere scaricato da Github, il link è nella descrizione del video e su ErgoTutorials.com.