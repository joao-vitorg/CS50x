const element = (e) => document.getElementById(e)

const inputs = {
    nome: /^[A-Z][A-Za-z ]{2,29}$/,
    idade: /^([1-9]|\d{2}|1[0-2]\d|130)$/,
}

function valida() {
    const nome = element("nome").value
    const idade = element("idade").value
    const passatempo = element("passatempo").selectedIndex

    if (!inputs["nome"].test(nome)) alert("Nome errado!!")
    else if (!inputs["idade"].test(idade)) alert("Idade errada!!")
    else if (!passatempo) alert("Informe um passatempo!!")
    else {
        guarda({nome, idade, passatempo})
        window.open("aguarde.html", "_self")
    }
}

function guarda(dados) {
    window.localStorage["dados"] = JSON.stringify(dados)
}
