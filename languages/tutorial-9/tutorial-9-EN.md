Tutorial 9 - EN

Title - Create mini web for your NFT

Description - In this tutorial we are going to create a mini website to show the NFT that you like the most.
Github: https://github.com/ladopixel/ErgoTutorials.com/tree/master/tutorial-2
Ergo Tokens: https://ergotokens.org/
If you want to see more tutorials about Ergo visit: https://ergotutorials.com/

1 - In this tutorial we are going to create a mini website that shows a NFT of the Ergo blockchain. We will only need to create 2 files: 1 index.html and another very simple javascript file.

2 - The first thing we will do is to create a file with HTML5 structure.

3 - We added the Bootstrap CSS to be able to shape our Card easily and quickly.

4 - We modified the title.

5 - On the Bootstrap website we copy Card's structure and modify it according to our needs. I'm going to include an image, a button and some paragraphs for the data we rescue.

6 - Add our .js file

7 - From the body we will call the getInfoToken() function through an onLoad.

8 - In the javascript file we will rescue some values from the Ergo blockchain by means of a simple query to its API Explorer.

9 - We will need the ID of the NFT to display, I go to the ErgoTokens.org website to look it up. If you already know the ID of your token you can skip this step.

10 - In the javascript file we create the function getInfoToken() and store the ID in a variable.

11 - Now we will make a query to the Ergo API Explorer.

12 - For this query we will use the endpoint and the variable in which we have stored the ID of our token.

13 - We display the data received in the console to verify that our query is correct.

14 - We look at the result and see what values we need to display our NFT Card.

15 - We create 4 variables to store the token information.

16 - We store in each variable the result returned by the API.

17 - Some of the values we receive are encoded, here you can take a closer look at the different encodings for this type of tokens.

18 - We add a function to decode the values returned by the API in order to understand them correctly.

19 - The image path, title and description of our token must be decoded by the function.

20 - Although the image path has been decoded, since the last change that was made for IPFS storage, to show us the correct path we must pass another function called resolveIpfs that has been created by Anon_real. Thanks to this function the images will be displayed correctly regardless of the type of storage you have.

21 - We pass the function to the path of our image.

22 - Now we would only have to visualize the content of our variables in the different HTML elements of our Card. We will refer to them by their ID.

23 - We go to the browser to see the result and we will be able to see a card of our NFT.

24 - Remember that the code for this tutorial can be downloaded from Github, the link is in the video description and at ErgoTutorials.com.