Tutorial 1 - French

1 - Dans ce tutoriel, nous allons récupérer des valeurs depuis la blockchain Ergo. Nous utiliserons une simple fonction pour interroger l'API Ergo Explorer version 1.

2 - Nous allons voir comment avec quelques petites lignes de code et des connaissances basiques en HTML et JavaScript, nous pouvons intéragir avec la blockchain Ergo. 

3 - La première chose que nous allons faire est de créer un fichier avec une structure HTML5 appelé index.html. Nous modifierons son titre, depuis balise body, nous appellerons la fonction heightCreation au moyen d'un onload et nous ajouterons un fichier JavaSript appelé getInfo.js que nous créerons plus tard.

3.1 - Nous avons modifié le titre.

3.2 - Nous appelons la fonction avec onload

3.3 - Nous intégrons notre fichier JavaScript.

4 - Maintenant, nous allons créer la fonction JavaScript pour recevoir les valeurs de la blockchain Ergo grâce à son API.

5 - Pour notre fonction, nous utiliserons un endpoint qui sera en charge de nous fournir les informations dont nous avons besoin. Le endpoint sera le suivant.

6 - Les valeurs que je recevrai depuis l'API seront affichées dans la console grâce à console.log

7 - Depuis la console de notre navigateur, nous pouvons voir que la réponse de l'API renvoie les données correctement. Faisons la comparaison avec la documentation.

8 - Maintenant, nous allons ajouter une ligne de code en plus pour utiliser une des valeurs reçues afin de modifier la couleur du fond de notre site internet. Cette couleur sera définie par la hauteur du bloc actuel.

9 - Avec cette dernière ligne, notre exemple est terminé. Nous pouvons maintenant aller sur notre navigateur et rafraîchir afin d'observer comment l'arrière plan de notre site change de couleur et prend la couleur de la hauteur du bloc Ergo actuel.

10 - Le code de ce tutoriel peut être téléchargé depuis Github
