function getInfoToken(){
    idToken = '5462442b70013b2770966c7266b2fce35be8b97a110b3f0dd08222d2b40d58dc'
    fetch('https://api.ergoplatform.com/api/v1/boxes/byTokenId/' + idToken)
        .then(response => response.json())
        .then(data => {
            console.log(data)

            // API Values
            let imagePath = resolveIpfs(toUtf8String(data.items[0].additionalRegisters.R9.renderedValue))
            let idToken = data.items[0].assets[0].tokenId
            let tituloToken = toUtf8String(data.items[0].additionalRegisters.R4.renderedValue)
            let artworkChecksum = data.items[0].additionalRegisters.R8.renderedValue
            let descriptionToken = toUtf8String(data.items[0].additionalRegisters.R5.renderedValue)
            
            // Display values in HMTL
            document.getElementById("imageToken").src = imagePath
            document.getElementById("nameToken").innerText = tituloToken
            document.getElementById("idToken").innerText = idToken
            document.getElementById("descriptionToken").innerText = descriptionToken
            document.getElementById("artworkChecksum").innerText = artworkChecksum
            
        })
        .catch(error => console.error('Error:', error))
}

function toUtf8String(hex) {
    if(!hex){ hex = ''}
    var str = ''
    for (var i = 0; i < hex.length; i += 2) {
        str += String.fromCharCode(parseInt(hex.substr(i, 2), 16))
    }
    return str
}

function resolveIpfs(url) {
    const ipfsPrefix = 'ipfs://'
    if (!url.startsWith(ipfsPrefix)) return url
    else return url.replace(ipfsPrefix, 'https://cloudflare-ipfs.com/ipfs/')
}