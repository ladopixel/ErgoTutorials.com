function heightCreation(){
    fetch('https://api.ergoplatform.com/api/v1/info')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            document.body.style.backgroundColor = "#" + data.height
        })
        .catch(error => console.error('Error:', error))
}