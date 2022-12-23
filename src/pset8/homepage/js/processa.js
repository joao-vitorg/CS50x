let timer, interval, segundos

function processa() {
    timer = document.getElementById("timer")
    segundos = Math.floor(Math.random() * 6) + 5
    atualiza()

    interval = setInterval(atualiza, 1000)
}

function atualiza() {
    timer.innerText = segundos

    if (segundos === 3) timer.style.color = "red"
    else if (segundos === 0) {
        clearInterval(interval)
        window.open("verVeiculo.html", "_self")
    }

    segundos--
}
