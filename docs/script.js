const BACKEND_URL = "https://chatbot-rag-production.up.railway.app/"; // Reemplaza con tu URL de Railway

document.addEventListener("DOMContentLoaded", function () {
    const chatForm = document.getElementById("chat-form");
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const typingIndicator = document.createElement("div");
    typingIndicator.id = "typing";
    typingIndicator.innerText = "Marco Aurelio está escribiendo...";
    chatBox.appendChild(typingIndicator);

    chatForm.addEventListener("submit", async function (event) {
        event.preventDefault();

        const userMessage = userInput.value.trim();
        if (!userMessage) return;

        addMessage("Tú", userMessage, "user");

        typingIndicator.style.display = "block";

        try {
            const response = await fetch(`${BACKEND_URL}/chat`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ query: userMessage }),
            });

            if (!response.ok) {
                throw new Error("Error en la respuesta del servidor");
            }

            const data = await response.json();
            typingIndicator.style.display = "none";
            addMessage("Marco Aurelio", formatResponse(data.respuesta), "bot");
        } catch (error) {
            typingIndicator.style.display = "none";
            addMessage("Error", "No se pudo conectar con el servidor.", "bot");
        }

        userInput.value = "";
    });

    function addMessage(sender, text, type) {
        const messageElement = document.createElement("div");
        messageElement.classList.add("message", type);
        messageElement.innerHTML = `<strong>${sender}:</strong><br>${text}`;
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function formatResponse(text) {
        return text.replace(/\n/g, "<br>").replace(/"(.*?)"/g, "<blockquote>$1</blockquote>");
    }
});
