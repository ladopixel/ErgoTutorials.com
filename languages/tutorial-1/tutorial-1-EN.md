Tutorial 1 - Inglés


1 - In this tutorial we are going to rescue some values from the Ergo blockchain. We will use a simple function to query Ergo Explorer API version 1.

2 - We are going to see how with very few lines of code and very basic knowledge of HTML and JavaScript, we can interact with the Ergo blockchain. 

3 - The first thing we will do is create a file with an HTML5 structure called index.html. We will modify its title, from its body tag we will call the heightCreation function through an onload and we will add a Javascript file called getInfo.js that we will create later.

3.1 - We modified the title.

3.2 - We call the function with onload.

3.3 - We include our Javascript file.

4 - Now we are going to create the Javascript function to receive the values of the Ergo blockchain through its API.

5 - For our function we will use an endpoint that will be in charge of providing us with the information we need. The endpoint is the following.

6 - The values that I will receive from the API will be shown in the console through console.log.

7 - From the console of our browser we can see that the API response returns the data correctly, we make the comparison with the documentation.

8 - Now we will add one more line of code to use one of the received values to color the background of our website, this color will be defined by the current block height.

9 - With this last line we have our example finished. Now we go to the browser and refresh to observe how the background of our website changes color and takes the color of the current Ergo block height.

10 - The code for this tutorial can be downloaded from Github.

