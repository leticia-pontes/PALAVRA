document.addEventListener("DOMContentLoaded", function() {
    const elemento = document.getElementById("texto-animado");
    const texto = elemento.textContent.trim();
    elemento.textContent = "";

    let indice = 0; // Índice para controlar a posição do caractere atual

    function typingEffect() {
        if (indice < texto.length) {
            elemento.textContent += texto.charAt(indice); // Adiciona o próximo caractere
            indice++;
            setTimeout(typingEffect, 38); // Tempo de digitação
        } else {
            setTimeout(deletingEffect, 1500); // Aguarda antes de iniciar a deleção
        }
    }

    function deletingEffect() {
        if (indice > 0) {
            elemento.textContent = texto.slice(0, indice - 1); // Remove o último caractere
            indice--;
            setTimeout(deletingEffect, 22); // Tempo de deleção
        } else {
            indice = 0; // Reinicia o índice
            setTimeout(typingEffect, 1500); // Aguarda antes de reiniciar a digitação
        }
    }

    typingEffect(); // Inicia o efeito de digitação
});
