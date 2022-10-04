Tutoriel 9 - FR

Titre - Créer un mini site web pour votre NFT

Description - Dans ce tutoriel, nous allons créer un mini site web pour montrer le NFT que vous aimez le plus. Github: Github: https://github.com/ladopixel/ErgoTutorials.com/tree/master/tutorial-2 Ergo Tokens: https://ergotokens.org/ Si vous voulez voir plus de tutoriels à propos d'Ergo, rendez-vous sur : https://ergotutorials.com/

1 - Dans ce tutoriel, nous allons créer un mini site web qui affiche un NFT de la blockchain Ergo. Nous aurons seulement besoin de créer 2 fichiers: 1 index.html et un autre fichier javascript très simple.

2 - La première chose que nous ferons est de créer un fichier avec une structure HTML5.

3 - Nous avons ajouté le CSS Bootstrap pour être capable de concevoir notre carte rapidement et facilement.

4 - Nous avons modifié le titre.

5 - Sur le site web Bootstrap, nous copions la structure de la carte et la modifions pour qu'elle s'adapte à nos besoins. Je vais inclure une image, un bouton et quelques paragraphes pour les données que nous gardons.

6 - Ajoutons notre fichier .js

7 - Depuis la partie body, nous appellerons la fonction getInfoToken() grâce à un onLoad.

8 - Dans le fichier javasript, nous allons récupérer des valeurs depuis la blockchain Ergo au moyen d'une simple requête à son API Explorer.

9 - Nous aurons besoin de l'ID du NFT à afficher. Je vais sur le site ErgoTokens.org pour la recherche. Si vous connaissez déjà l'ID de votre token, vous pouvez passer cette étape.

10 - Dans le fichier javascript, nous créons la fonction getInfoToken() et stockons l'ID dans une variable.

11 - Maintenant nous créons une requête pour l'API Explorer d'Ergo.

12 - Pour cette requête, nous utiliserons l'endpoint et la variable dans laquelle nous avons stocké l'ID de notre token.

13 - Nous affichons les données reçues dans la console pour vérifier que notre requête est correcte.

14 - Nous observons le résultat et voyons de quelles valeurs nous avons besoin pour afficher notre carte NFT.

15 - Nous créons 4 variables pour sauvegarder les informations du token.

16 - Nous stockons dans chaque variable, le résultat retourné par l'API.

17 - Certaines des valeurs que nous recevons sont encodées. Ici, vous pouvez regarder attentivement les différents encodages pour ce type de tokens.

18 - Nous ajoutons une fonction pour décoder les valeurs retournées par l'API dans le but de bien les comprendre.

19 - Le chemin de l'image, le titre et la description de notre token doivent être décodés par la fonction.

20 - Bien que le chemin de l'image ait bien été décodé, depuis la derniere modification qui a été faite sur le stockage IPFS, pour nous montrer le chemin correct, nous devons ajouter une autre fonction appelée resolveIpfs qui a été créée par Anon_real. Grâce à cette fonction, les images seront affichées correctement peu importe le type de stockage que nous avons.

21 - Nous ajoutons la fonction au chemin de notre image.

22 - Maintenant, il ne nous reste plus qu'à visualiser le contenu de nos variables dans les différents éléments HTML de notre carte. Nous ferons référence à eux à travers leur ID.

23 - Nous allons sur le navigateur pour voir le résultat et nous sommes capables de voir la carte de notre NFT

24 - Souvenez-vous que le code de ce tutoriel peut être téléchargé depuis Github, le lien est dans la description de la vidéo et sur ErgoTutorials.com.
