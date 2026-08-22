document.addEventListener("DOMContentLoaded", function () {
  const codeBlocks = document.querySelectorAll(".highlight");

  codeBlocks.forEach((highlightDiv) => {
    // Evita duplicar o botão caso o template já o insira
    if (highlightDiv.querySelector(".copy-code-button")) return;

    const button = document.createElement("button");
    button.className = "copy-code-button";
    button.innerText = "Copiar";

    button.addEventListener("click", () => {
      const codeElement = highlightDiv.querySelector("code");
      const code = codeElement ? codeElement.innerText : highlightDiv.innerText;

      navigator.clipboard.writeText(code).then(() => {
        button.innerText = "Copiado!";
        setTimeout(() => {
          button.innerText = "Copiar";
        }, 2000);
      });
    });

    highlightDiv.appendChild(button);
  });
});