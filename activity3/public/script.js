// Função para resolver a equação do segundo grau
function resolverEquacao() {
    // Obtém os coeficientes da entrada do usuário
    const a = parseFloat(document.getElementById("a").value);
    const b = parseFloat(document.getElementById("b").value);
    const c = parseFloat(document.getElementById("c").value);
    const resultadoElement = document.getElementById("resultadoEquacao");

    // Calcula o discriminante (delta)
    const delta = b * b - 4 * a * c;

    // Verifica se a solução é possível e calcula as raízes
    if (delta > 0) {
        const x1 = (-b + Math.sqrt(delta)) / (2 * a);
        const x2 = (-b - Math.sqrt(delta)) / (2 * a);
        resultadoElement.innerText = `As raízes são x1 = ${x1.toFixed(2)} e x2 = ${x2.toFixed(2)}`;
    } else if (delta === 0) {
        const x = -b / (2 * a);
        resultadoElement.innerText = `A raiz única é x = ${x.toFixed(2)}`;
    } else {
        resultadoElement.innerText = "Não existem raízes reais.";
    }
}

// Função para ordenar números aleatórios
function ordenarNumeros() {
    const quantidade = parseInt(document.getElementById("quantidadeNumeros").value);
    if (isNaN(quantidade) || quantidade <= 0) {
        document.getElementById("resultadoOrdenacao").innerText = "Por favor, insira um número válido.";
        return;
    }

    // Gera os números aleatórios
    let numeros = [];
    for (let i = 0; i < quantidade; i++) {
        numeros.push(Math.floor(Math.random() * 100)); // Números de 0 a 99
    }

    // Ordena os números
    const numerosOrdenados = [...numeros].sort((a, b) => a - b);

    // Exibe o resultado
    document.getElementById("resultadoOrdenacao").innerText = `Números gerados: ${numeros.join(", ")}\nNúmeros ordenados: ${numerosOrdenados.join(", ")}`;
}
