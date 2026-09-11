const input = document.getElementById("messageInput");
const sendButton = document.getElementById("sendButton");
const messages = document.getElementById("messages");
const welcome = document.getElementById("welcome");

sendButton.addEventListener("click", sendMessage);

input.addEventListener("keydown", function (event) {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
});

function askQuestion(question) {
    input.value = question;
    sendMessage();
}

async function sendMessage() {
    const message = input.value.trim();

    if (!message) {
        return;
    }

    welcome.style.display = "none";

    addMessage("You", message, "user");

    input.value = "";
    sendButton.disabled = true;

    addMessage("AI", "Thinking...", "assistant");

    try {
        const response = await fetch("https://ai-assistant-v-1.onrender.com/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();

        const assistantMessages =
            document.querySelectorAll(".message.assistant");

        const lastMessage =
            assistantMessages[assistantMessages.length - 1];

        lastMessage.querySelector(".message-content").textContent =
            data.answer;

    } catch (error) {
        console.error("Error:", error);

        const assistantMessages =
            document.querySelectorAll(".message.assistant");

        const lastMessage =
            assistantMessages[assistantMessages.length - 1];

        lastMessage.querySelector(".message-content").textContent =
            "Sorry, something went wrong. Please try again.";
    }

    sendButton.disabled = false;
}

function addMessage(sender, text, type) {
    const messageDiv = document.createElement("div");

    messageDiv.className = `message ${type}`;

    const avatar = document.createElement("div");
    avatar.className = "avatar";
    avatar.textContent = sender === "You" ? "You" : "AI";

    const content = document.createElement("div");
    content.className = "message-content";
    content.textContent = text;

    messageDiv.appendChild(avatar);
    messageDiv.appendChild(content);

    messages.appendChild(messageDiv);

    messages.scrollTop = messages.scrollHeight;
}