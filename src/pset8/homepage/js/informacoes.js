const element = (e) => document.getElementById(e)

const dados = [
    [" Hond", " Civic", " 150 cv", " 3 anos", " 9,7 km/l"],
    [" Ford", " Troller", " 200 cv", " 3 anos", " 7,7 km/l"],
]

function carregar() {
    const carro = JSON.parse(window.localStorage["dados"])
    const lista = element("lista")
    carro.passatempo--

    element("nome").innerText = carro.nome
    element("imagem").src = `img/${["civic", "troller"][carro.passatempo]}.jpg`

    dados[carro.passatempo].map((dado, index) => {
        lista.children[index].innerHTML += dado
    })
}
